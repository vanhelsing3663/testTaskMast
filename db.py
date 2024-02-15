import sqlite3

import requests

def create_connection():
    return sqlite3.connect('database.db')

def execute_query(query, params=None, fetch_all=False):
    with create_connection() as conn:
        cursor = conn.cursor()

        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        conn.commit()

        if fetch_all:
            result = cursor.fetchall()
        else:
            result = None

    return result
