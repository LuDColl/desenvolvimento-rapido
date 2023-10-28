import sqlite3
from typing import Any


_connection: sqlite3.Connection


def connect() -> None:
    global _connection
    _connection = sqlite3.connect('my_database.db')


def commit(sql: str) -> None:
    cursor = _connection.cursor()
    cursor.execute(sql)
    _connection.commit()
    cursor.close()


def select(sql: str) -> list[Any]:
    cursor = _connection.cursor()
    cursor.execute(sql)
    select = cursor.fetchall()
    cursor.close()
    return select


def find(sql: str) -> Any:
    cursor = _connection.cursor()
    cursor.execute(sql)
    select = cursor.fetchone()
    cursor.close()
    return select


def close() -> None:
    _connection.close()
