from flask import render_template, Blueprint, redirect, request, session
from random import choice
import users
route = Blueprint("routes", __name__)

hardcoded_decks = [(choice(["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]), f"Placeholder {i}", i) for i in range(50)]
categories = ["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]
hardocded_reviews = [{"username": "asd", "rating": "12", "comment": "hyva on"}, {"username": "qwe", "rating": "1", "comment": "ei hyva"}]

@route.route("/")
def index():
    try:
        log = session["username"]
    except:
        log = False
    return render_template("index.html", logged_in=log, decks=hardcoded_decks, categories=categories)

@route.route("/login")
def login():
    return render_template("login.html")

@route.route("/login/check", methods=["POST"])
def login_check():
    username = request.form["username"]
    password = request.form["password"]

    if not users.login(username, password):
        return redirect("/login")

    session["username"] = username
    return redirect("/")

@route.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@route.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

@route.route("/register/check", methods=["POST"])
def register_check():
    username = request.form["username"]
    password = request.form["password"]
    password_check = request.form["password_check"]

    try:
        users.register(username, password, password_check)
        return redirect("/login")
    except:
        return redirect("/register")

@route.route("/deck/<int:id>")
def deck(id):
    return render_template("deck.html", reviews=hardocded_reviews, is_owner=True, deck=hardcoded_decks[id])

@route.route("/deck/<int:id>/edit")
def edit_deck(id):
    return render_template("edit.html", deck=hardcoded_decks[id])

@route.route("/deck/<int:id>/delete")
def delete_deck(id):
    return render_template("delete.html", deck=hardcoded_decks[id])