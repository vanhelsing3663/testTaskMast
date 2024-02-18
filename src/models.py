from datetime import datetime
from db import execute_query


def create_table_click() -> None:
    query = """
        CREATE TABLE IF NOT EXISTS Information (
            press_count INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT NOT NULL,
            press_date DATE NOT NULL,
            press_time TIME NOT NULL
        );
    """
    execute_query(query)


def get_now_date():
    return datetime.now().date()


def get_now_time():
    return datetime.now().time()


def insert_data(text) -> None:
    press_date = get_now_date()
    press_time = get_now_time()
    press_time_str = press_time.strftime("%H:%M:%S")

    query = """
        INSERT INTO Information (press_date, press_time, text)
        VALUES (?, ?, ?);
    """
    params = (press_date, press_time_str, text)
    execute_query(query, params)


def get_all() -> None:
    query = """
        SELECT 
            * 
        FROM 
            Information
    """
    return execute_query(query, fetch_all=True)
