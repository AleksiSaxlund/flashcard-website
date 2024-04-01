from db import db
from sqlalchemy.sql import text

def get_all_users():
    sql = text("SELECT * FROM users")
    result = db.session.execute(sql)
    users = result.fetchall()
    return users