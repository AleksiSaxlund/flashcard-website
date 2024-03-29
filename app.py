from flask import Flask
from flask import render_template
from random import choice

app = Flask(__name__)

hardcoded_decks = [(choice(["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]), f"Placeholder {i}") for i in range(50)]
categories = ["😳","💀","🐸","😃","🐛","👨‍👩‍👧‍👦","🎞","🚲","🍠","🥩"]

@app.route("/")
def index():
    asd = [i for i in range(50)]
    return render_template("index.html", logged_in=False, decks=hardcoded_decks, categories=categories)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")