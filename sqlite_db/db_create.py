import sqlite3 as sq


class DbKeramag:

    def __init__(self, name_db_file):
        with sq.connect(name_db_file) as self.con:
            self.cursor = self.con.cursor()

    def create_table_tile_data(self):
        with self.con:
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {"tile_data"} (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                position INTEGER,            
                name TEXT DEFAULT 'Неизвестный',
                article INTEGER,                
                price_now REAL,                
                discount REAL,                
                old_price REAL,
                unit_of_value TEXT,
                country TEXT,
                size TEXT,                
                in_stock TEXT,
                url_individual_page TEXT DEFAULT 'Неизвестный',
                url_small_picture TEXT,
                date DATETIME NOT NULL DEFAULT ((DATE('now')))
            )""")

    def create_table_users_requests(self):
        with self.con:
            self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {"users_requests"} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,                
                date DATETIME NOT NULL DEFAULT ((DATE('now'))),   
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL DEFAULT 'Неизвестный',
                price REAL,
                discount REAL,
                article INTEGER,      
                country TEXT                   
                )""")

    def _drop_table(self, name_table: str):
        with self.con:
            self.cursor.execute(f"DROP TABLE IF EXISTS {name_table}")
