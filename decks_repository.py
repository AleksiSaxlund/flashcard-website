from db import db
from sqlalchemy.sql import text
from flask import session

def create_deck(name, category, user_id):
    print(name, category, user_id)
    sql = text("INSERT INTO decks (deck_name, category_id, user_id, visible) VALUES (:name, :category, :user_id, TRUE)")
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

def delete_deck(deck_id):
    sql = text("UPDATE decks SET visible = FALSE WHERE id = :deck_id")
    db.session.execute(sql, {"deck_id": deck_id})
    db.session.commit()

def delete_card(card_id):
    sql = text("UPDATE cards SET visible = FALSE WHERE id = :card_id")
    db.session.execute(sql, {"card_id": card_id})
    db.session.commit()

def get_cards(deck_id):
    sql = text("SELECT id, front, back FROM cards WHERE deck_id = :deck_id AND visible = TRUE")
    result = db.session.execute(sql, {"deck_id": deck_id})
    return result.fetchall()

def get_card(card_id):
    sql = text("SELECT id, front, back, deck_id FROM cards WHERE id = :card_id")
    result = db.session.execute(sql, {"card_id": card_id})
    return result.fetchone()

def edit_card(card_id, front, back):
    sql = text("UPDATE cards SET front = :front, back = :back WHERE id = :card_id")
    db.session.execute(sql, {"front": front, "back": back, "card_id": card_id})
    db.session.commit()

def create_card(deck_id, front, back):
    sql = text("INSERT INTO cards (front, back, deck_id, visible) VALUES (:front, :back, :deck_id, :visible)")
    db.session.execute(sql, {"front": front, "back": back, "deck_id": deck_id, "visible": True})
    db.session.commit()

def get_categories():
    sql = text("SELECT id, category_name FROM categories")
    result = db.session.execute(sql)
    return result.fetchall()

def create_review(deck_id, user_id, comment, rating):
    sql = text("INSERT INTO reviews (deck_id, user_id, comment, rating) VALUES (:deck_id, :user_id, :comment, :rating)")
    db.session.execute(sql, {"deck_id": deck_id, "user_id": user_id, "comment": comment, "rating": rating})
    db.session.commit()

def get_reviews(deck_id):
    sql = text("SELECT (SELECT username FROM users WHERE id = user_id), rating, comment FROM reviews WHERE deck_id = :deck_id")
    result = db.session.execute(sql, {"deck_id": deck_id})
    return result.fetchall()
