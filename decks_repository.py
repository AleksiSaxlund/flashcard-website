from db import db
from sqlalchemy.sql import text
from flask import session

def create_deck(name, category):
    user_id = session["user_id"]
    sql = text("INSERT INTO decks (name, category_id, user_id, visible) VALUES (:name, :category, :user_id, TRUE)")
    db.session.execute(sql, {"name": name, "category": category, "user_id": user_id})
    db.session.commit()

def get_decks():
    sql = text("SELECT id, deck_name, category_id FROM decks WHERE visible = TRUE")
    result = db.session.execute(sql)
    return result.fetchall()

def get_deck(deck_id):
    sql = text("SELECT id, deck_name, category_id, user_id FROM decks WHERE id = :deck_id")
    result = db.session.execute(sql, {"deck_id": deck_id})
    return result.fetchone()

def get_cards(deck_id):
    sql = text("SELECT id, front, back FROM cards WHERE deck_id = :deck_id")
    result = db.session.execute(sql, {"deck_id": deck_id})
    return result.fetchall()

def get_categories():
    sql = text("SELECT id, category_name FROM categories")
    result = db.session.execute(sql)
    return result.fetchall()