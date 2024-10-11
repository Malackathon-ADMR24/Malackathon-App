import sqlite3
from sqlite3 import Connection

from app import config


class SQLiteDatabaseConnection:
    def __init__(self):
        self.db_name = config("database.path")
        self.connection: Connection = None
        self.last_rowid = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def execute_query(self, query: str, params: tuple = ()) -> [tuple]:
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.last_rowid = cursor.lastrowid
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_script(self, script: str):
        cursor = self.connection.cursor()
        cursor.executescript(script)
        cursor.close()

    def close(self):
        if self.connection:
            self.connection.commit()
            self.connection.close()


class OracleDatabaseConnection:
    def __init__(self):
        raise NotImplementedError()

    def connect(self):
        raise NotImplementedError()

    def execute_query(self):
        raise NotImplementedError()

    def execute_script(self):
        raise NotImplementedError()

    def close(self):
        raise NotImplementedError()


DatabaseConnection = None


def detect_driver():
    global DatabaseConnection
    DatabaseConnection = {
        "sqlite": SQLiteDatabaseConnection,
        "oracle": OracleDatabaseConnection
    }[config("database.type")]
