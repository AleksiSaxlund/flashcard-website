import os
from db import db
from sqlalchemy.sql import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from secrets import token_hex

class UserInputError(Exception):
    pass


def login(username, password):
    sql = text("SELECT id, username, password FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user == None:
        return False
    if not check_password_hash(user[2], password):
        return False
    
    session["username"] = user[1]
    session["user_id"] = user[0]
    session["csrf_token"] = token_hex(16)
    return True

def logout():
    del session["username"]
    del session["user_id"]
    del session["csrf_token"]

def register(username, password, password_check):

    if validator(username, password, password_check):
        hash_value = generate_password_hash(password)
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()

        return True
    return False

def validator(username, password, password_check):
    if not username or not password or not password_check:
        raise UserInputError("Username and password are required")
    if len(username) < 4:
        raise UserInputError("Username must be atleast 3 characters long")
    if password != password_check:
        raise UserInputError("Passwords are not the same")
    if len(password) < 7:
        raise UserInputError("Password usmt be atleast 5 characters long")
    if not any(char.isdigit() for char in password):
        raise UserInputError("Password must contain atleast 1 number")
    if not any(char in "!@#$%^&*()-_=+[]{};:'\"<>,.?/" for char in password):
        raise UserInputError("Password must contain atleast 1 special character")
    return True
