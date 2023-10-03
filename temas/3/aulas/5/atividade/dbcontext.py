import sqlite3


__connection: sqlite3.Connection


def connect():
    global __connection
    __connection = sqlite3.connect('my_database.db')


def commit(sql: str):
    cursor = __connection.cursor()
    cursor.execute(sql)
    __connection.commit()
    cursor.close()


def select(sql: str):
    cursor = __connection.cursor()
    cursor.execute(sql)
    select = cursor.fetchall()
    cursor.close()
    return select


def find(sql: str):
    cursor = __connection.cursor()
    cursor.execute(sql)
    select = cursor.fetchone()
    cursor.close()
    return select


def close():
    __connection.close()
