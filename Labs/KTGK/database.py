import sqlite3


class Database:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS thiet_bi (
                ma_thiet_bi TEXT PRIMARY KEY,
                ten_thiet_bi TEXT,
                loai TEXT,
                so_luong INTEGER,
                tinh_trang TEXT
            )
        """)
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM thiet_bi")
        return self.cursor.fetchall()

    def insert(self, ma, ten, loai, sl, tt):
        self.cursor.execute(
            "INSERT INTO thiet_bi VALUES (?, ?, ?, ?, ?)", (ma, ten, loai, sl, tt)
        )
        self.conn.commit()

    def update(self, ma, ten, loai, sl, tt):
        self.cursor.execute(
            "UPDATE thiet_bi SET ten_thiet_bi=?, loai=?, so_luong=?, tinh_trang=? WHERE ma_thiet_bi=?",
            (ten, loai, sl, tt, ma),
        )
        self.conn.commit()

    def delete(self, ma):
        self.cursor.execute("DELETE FROM thiet_bi WHERE ma_thiet_bi=?", (ma,))
        self.conn.commit()

    def search(self, tu_khoa):
        query = f"%{tu_khoa}%"
        self.cursor.execute(
            "SELECT * FROM thiet_bi WHERE ma_thiet_bi LIKE ? OR ten_thiet_bi LIKE ?",
            (query, query),
        )
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
