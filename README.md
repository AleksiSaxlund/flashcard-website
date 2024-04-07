
# Flashcard Website

## Usage guide

This excepts that decently up-to-date versions Poetry, PostgreSQL and Python are already installed on the machine.

The app has been tested on my own ubuntu machine and on fuksiläppäri.

### First time setup
1. Run the command *poetry install* on the terminal in the root folder
2. Run the command *poetry shell* on the terminal in the root folder
3. Create a `.env`-file which has the following arguments:
    1. DATABASE_URL=*your database url*
    2. SECRET_KEY=*your secret key*
4. Run the `init_database.py` script to initialize the database.
    - If the script does not work on your computer, you will have to manually load `schema.sql` into your database.

### Running the app

1. Run the command *poetry shell* on the terminal in the root folder
2. Run the command *flask run* in the rootfolder
3. Open the address indicated by the flask server on your browser

## Currently implemented features

- [X] The user sees flashcard decks on the frontpage of the app.
- [X] The user can play the decks without logging in.
- [ ] The user can search for decks based on keywords or categories.
- [X] The user can create an account and login to it.
- [X] The user can create decks after logging on to an account.
- [X] The user can edit decks that their account owns.
- [X] The users can review decks made by other users.
- [ ] The user can add decks to their favourites.
- [ ] The users can play a quiz mode based on a deck of their choosing. **Will be implemented only if there is enough time**

The user interface is not done. Many parts have just the basic elements to get the base functionality.

There is no defence for SQL injections or vulnerabilities and the security might be lacking otherwise too.

Please report any bugs you find. :)
