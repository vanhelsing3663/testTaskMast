import sqlite3


def create_connection():
    return sqlite3.connect("database.db")


def execute_query(query, params=None, fetch_all=False):
    with create_connection() as conn:
        cursor = conn.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            conn.commit()

            if fetch_all:
                result = cursor.fetchall()
            else:
                result = None
        except sqlite3.Error as e:
            print(f"An exception occurred related to a database query: {e}")
            result = None
    return result
