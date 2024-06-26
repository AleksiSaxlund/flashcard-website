CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL
);

CREATE TABLE decks (
  id SERIAL PRIMARY KEY,
  deck_name VARCHAR(255) NOT NULL,
  category_id INTEGER REFERENCES categories,
  user_id INTEGER REFERENCES users,
  visible BOOLEAN NOT NULL
);

CREATE TABLE cards (
  id SERIAL PRIMARY KEY,
  front TEXT NOT NULL,
  back TEXT NOT NULL,
  deck_id INTEGER REFERENCES decks,
  visible BOOLEAN NOT NULL
);

CREATE TABLE reviews (
  id SERIAL PRIMARY KEY,
  deck_id INTEGER REFERENCES decks,
  user_id INTEGER REFERENCES users,
  comment TEXT NOT NULL,
  rating INTEGER NOT NULL
);

CREATE TABLE favourites (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users,
  deck_id INTEGER REFERENCES decks,
  visible BOOLEAN NOT NULL
);

INSERT INTO categories (category_name) VALUES ('Language');
INSERT INTO categories (category_name) VALUES ('Geography');
INSERT INTO categories (category_name) VALUES ('Math');
INSERT INTO categories (category_name) VALUES ('Chemistry');