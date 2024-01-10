import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS ram_info (
                        id INTEGER PRIMARY KEY,
                        total REAL,
                        free REAL,
                        used REAL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
        except Exception as e:
            return str(e)

    def insert_ram_data(self, data):
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO ram_info (total, free, used)
                    VALUES (?, ?, ?)
                """, (data[0], data[1], data[2]))
                conn.commit()
                
                return True
        except Exception as e:
           raise Exception(e)
    
    def get_last_n_entries(self, n):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT total, free, used FROM ram_info
                ORDER BY id DESC
                limit ?
            """, (n,))
            return cursor.fetchall()
