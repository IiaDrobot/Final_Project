
import sqlite3
import pymysql
from config import sakila_dbconfig


class DBConnector:
    def __init__(self, db_config=None, db_name=None):
        self.db_config = db_config
        self.db_name = db_name
        self._connection = None
        self._cursor = None

    def _set_connection(self):
        if self.db_config:
            return pymysql.connect(**self.db_config)
        elif self.db_name:
            def dict_factory(cursor, row):
                d = {}
                for idx, col in enumerate(cursor.description):
                    d[col[0]] = row[idx]
                return d

            connection = sqlite3.connect(self.db_name)
            connection.row_factory = dict_factory
            return connection

    def _set_cursor(self):
        return self._connection.cursor()

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()

    def execute_query(self, query, params=None):
        try:
            self._connection = self._set_connection()
            self._cursor = self._set_cursor()
            if params:
                self._cursor.execute(query, params)
            else:
                self._cursor.execute(query)
            return self._cursor.fetchall()
        except Exception as e:
            print(f"Ошибка выполнения запроса: {e}")
        finally:
            self.close()

    def execute_insert(self, query, params=None):
        try:
            self._connection = self._set_connection()
            self._cursor = self._set_cursor()
            self._cursor.execute(query, params)
            self._connection.commit()
        except Exception as e:
            print(f"Ошибка выполнения вставки: {e}")
        finally:
            self.close()
