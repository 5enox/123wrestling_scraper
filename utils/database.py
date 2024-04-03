import sqlite3
import json


class DatabaseHandler:
    def __init__(self, db_name='videos.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS videos
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            site TEXT,
                            title TEXT,
                            url TEXT,
                            other_details JSON)''')
        self.conn.commit()

    def save_video(self, data):
        site, title, url, other_details = data
        other_details = json.dumps(other_details)
        self.cursor.execute('''INSERT INTO videos (site, title, url, other_details)
                            VALUES (?, ?, ?, ?)''', (site, title, url, other_details))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
