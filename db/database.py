import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db/recipes.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_data(self):
        self.cursor.execute("SELECT * FROM items ORDER BY RANDOM() LIMIT 1")
        return self.cursor.fetchone()

