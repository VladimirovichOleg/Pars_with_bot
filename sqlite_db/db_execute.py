import sqlite3 as sq
from datetime import datetime

from sqlite_db.db_create import DbKeramag


class DbExecute(DbKeramag):
    # PATH_TO_DB = "/home/oleg/python_progect/keramag/sqlite_db/db_for_keramag.db"
    PATH_TO_DB = "/home/pars_with_teleg_bot/sqlite_db/db_for_keramag.db"
    TUPLE_OF_VAR = (
        'position',
        'name',
        'article',
        'price_now',
        'discount',
        'old_price',
        'unit_of_value',
        'country',
        'size',
        'in_stock',
        'url_individual_page',
        'url_small_picture'
    )

    def get_price_on_the_name(self, name_table, name_or_article_prod):
        with sq.connect(self.PATH_TO_DB) as connect:
            cursor = connect.cursor()
            return cursor.execute(f"SELECT * FROM {name_table} WHERE name LIKE '%{name_or_article_prod}%' "
                                  f"OR article LIKE '%{name_or_article_prod}%'").fetchmany(10)

    def check_max_id(self, name_table: str) -> int:
        max_id = self.cursor.execute(f"SELECT MAX(id) FROM {name_table}").fetchone()[0]
        if max_id:
            return max_id
        else:
            return 0

    def prod_availability(self, name_table: str, param_: dict):
        with self.con:
            return self.cursor.execute(f"SELECT * FROM {name_table} WHERE name = ?", (param_['name'],)).fetchone()

    def update_price(self, name_table: str, param: dict) -> None:
        with self.con:
            self.cursor.execute(f"UPDATE {name_table} SET price_now=?, discount=?, old_price=? WHERE name=?",
                                (param['price_now'], param['discount'], param['old_price'], param['name']))

    def add_prod_on_FIRST_pos(self, name_table: str, param: dict) -> None:
        with self.con:
            self.cursor.execute(f"UPDATE {name_table} SET position = position + 1")
            self.cursor.execute(
                f"INSERT INTO {name_table} {self.TUPLE_OF_VAR} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (1,
                 param['name'],
                 param['article'],
                 param['price_now'],
                 param['discount'],
                 param['old_price'],
                 param['unit_of_value'],
                 param['country'],
                 param['size'],
                 param['in_stock'],
                 param['url_individual_page'],
                 param['url_small_picture'],)
            )

    def add_prod_on_LAST_pos(self, name_table: str, param: dict) -> int:
        with self.con:
            max_id = self.check_max_id(name_table)
            self.cursor.execute(
                f"INSERT INTO {name_table} {self.TUPLE_OF_VAR} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (max_id + 1,
                 param['name'],
                 param['article'],
                 param['price_now'],
                 param['discount'],
                 param['old_price'],
                 param['unit_of_value'],
                 param['country'],
                 param['size'],
                 param['in_stock'],
                 param['url_individual_page'],
                 param['url_small_picture'],)
            )
            return max_id + 1

    def check_date(self, name_table) -> int:
        with self.con:
            date = self.cursor.execute(f"SELECT * FROM {name_table} WHERE id = ?", (1,)).fetchone()
            if date:
                if date[13] == datetime.today().strftime('%Y-%m-%d'):
                    return 0
                else:
                    return 1
            else:
                return 0
