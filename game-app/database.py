import sqlite3
import datetime

# SQL

CREATE_TABLES = "CREATE TABLE IF NOT EXISTS CREATE games(title, TEXT, release_timestamp REAL, played INTEGER)"

INSERT_GAME = "INSERT INTO (title, release_timestamp, played) VALUES (?, ?, 0);"

SELECT_UPCOMING_GAMES = "SELECT * FROM games WHERE release_timestamp > ?;"

SELECT_ALL_GAMES = "SELECT * FROM games;"

MARK_GAME_AS_PLAYED = "UPDATE games SET played = 1 WHERE title = ?; "

SELECT_PLAYED_GAMES = 'SELECT * FROM games WHERE played = 1'

# <----------------------------------------------------------------

connection = sqlite3.connect("games.db")


def create_tables():
    with connection:
        connection.execute(CREATE_TABLES)


def add_game(title, timestamp):
    with connection:
        connection.execute(INSERT_GAME, (title, timestamp))


def view_games():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_GAMES)
        return cursor


def upcoming_games():
    with connection:
        cursor = connection.cursor()
        d = datetime.datetime.today().timestamp()
        cursor.execute(SELECT_UPCOMING_GAMES, (d,))
        return cursor

def view_played_games():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_PLAYED_GAMES)

def mark_game_as_played(game_title):
    with connection:
        connection.execute(MARK_GAME_AS_PLAYED, (game_title, ))
