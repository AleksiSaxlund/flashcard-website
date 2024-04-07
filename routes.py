from flask import render_template, Blueprint, redirect, request, session
from random import choice
import users
import decks_repository
route = Blueprint("routes", __name__)

hardcoded_decks = [(choice(["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]), f"Placeholder {i}", i) for i in range(50)]
categories = ["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]
hardocded_reviews = [{"username": "asd", "rating": "12", "comment": "hyva on"}, {"username": "qwe", "rating": "1", "comment": "ei hyva"}]

@route.route("/")
def index():
    print(session)
    try:
        log = session["username"]
    except:
        log = False
    decks = decks_repository.get_decks()
    categories = decks_repository.get_categories()
    return render_template("index.html", logged_in=log, decks=decks, categories=categories)

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

@route.route("/deck/<int:deck_id>")
def deck(deck_id):
    deck = decks_repository.get_deck(deck_id)
    is_owner = deck[3] == session.get("user_id")
    return render_template("deck.html", deck=deck, reviews=hardocded_reviews, is_owner=is_owner)

@route.route("/deck/<int:deck_id>/edit")
def edit_deck(deck_id):
    deck = decks_repository.get_deck(deck_id)
    cards = decks_repository.get_cards(deck_id)
    if deck[3] != session.get("user_id"):
        return redirect("/")
    return render_template("edit_deck.html", deck=deck, cards=cards)

@route.route("/deck/<int:deck_id>/edit/<int:card_id>")
def edit_card(deck_id, card_id):
    card = decks_repository.get_card(card_id)
    return render_template("edit_card.html", card_id = card[0], front=card[1], back=card[2], deck_id=card[3])

@route.route("/deck/<int:deck_id>/edit/submit_card", methods=["POST"])
def submit_card(deck_id):
    new = request.form["new_card"]
    front = request.form["front"]
    back = request.form["back"]
    print(new)
    if new == True:
        decks_repository.create_card(deck_id, front, back)
    else:
        card_id = request.form["card_id"]
        decks_repository.edit_card(card_id, front, back)
    return redirect(f"/deck/{deck_id}/edit")

@route.route("/deck/<int:deck_id>/edit/delete", methods=["POST"])
def delete_deck(deck_id):
    deck = decks_repository.get_deck(deck_id)
    if deck[3] != session.get("user_id"):
        return redirect("/")
    decks_repository.delete_deck(deck_id)
    return redirect("/")

@route.route("/deck/<int:deck_id>/edit/<int:card_id>/delete", methods=["POST"])
def delete_card(deck_id, card_id):
    decks_repository.delete_card(card_id)
    return redirect(f"/deck/{deck_id}/edit")

@route.route("/create_deck")
def create_deck():
    categories = decks_repository.get_categories()
    return render_template("create_deck.html", categories=categories)

@route.route("/create_deck/submit", methods=["POST"])
def create_deck_create():
    name = request.form["deckname"]
    category = request.form["category"]
    user_id = session["user_id"]
    decks_repository.create_deck(name, category, user_id)
    return redirect("/")
