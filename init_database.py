"""Python script to initialize the database called flashcards for the app.
    Tested on Ubuntu."""

import psycopg2

DB_NAME = "postgres"
username = input("Enter username of your database in postgres: ")
DB_USER = username
DB_HOST = "localhost"
DB_PORT = "5432"
NEW_DB_NAME = "flashcards"

def create_database():
    """Creates a new database and tables from schema.sql file."""
    conn = None

    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            host=DB_HOST,
            port=DB_PORT
        )
        
        print("Database connected successfully")
    
    except psycopg2.OperationalError as e:
        print("Error while connecting to the database: ", e)

    if conn is not None:

        # Creates the database
        conn.autocommit = True
        cur = conn.cursor()

        print("Creating database... with name: ", NEW_DB_NAME, "...")
        sql = f"CREATE DATABASE {NEW_DB_NAME};"
        cur.execute(sql)
        print("Database created successfully")
        print("Creating tables...")

        with psycopg2.connect(dbname=NEW_DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT) as conn:
            with conn.cursor() as cur:
                
                # Reads and creates tables from schema.sql
                with open ("schema.sql", "r", encoding="UTF-8") as file:
                    sql_commands = file.read().split(";")
                    for command in sql_commands:
                        if command.strip():
                            cur.execute(command)
                print("Tables created successfully")
        
    conn.close()

if __name__ == "__main__":
    create_database()
