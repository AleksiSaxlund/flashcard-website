from app import app
from flask import render_template
from random import choice

hardcoded_decks = [(choice(["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]), f"Placeholder {i}", i) for i in range(50)]
categories = ["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]
hardocded_reviews = [{"username": "asd", "rating": "12", "comment": "hyva on"}, {"username": "qwe", "rating": "1", "comment": "ei hyva"}]

@app.route("/")
def index():
    return render_template("index.html", logged_in=False, decks=hardcoded_decks, categories=categories)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/deck/<int:id>")
def deck(id):
    return render_template("deck.html", reviews=hardocded_reviews, is_owner=True, deck=hardcoded_decks[id])

@app.route("/deck/<int:id>/edit")
def edit_deck(id):
    return render_template("edit.html", deck=hardcoded_decks[id])

@app.route("/deck/<int:id>/delete")
def delete_deck(id):
    return render_template("delete.html", deck=hardcoded_decks[id])