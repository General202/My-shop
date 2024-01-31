import sqlite3

class BlogDB:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor() #створюєм курсор

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_all_posts(self):
        self.open()
        self.cursor.execute("SELECT * FROM posts")
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_posts_by_category(self, category_id):
        self.open()
        self.cursor.execute("SELECT * FROM posts WHERE category_id = ?", [category_id])
        data = self.cursor.fetchall()
        self.close()
        return data

    def get_all_categories(self):
        self.open()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
