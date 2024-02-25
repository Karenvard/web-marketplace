import psycopg2 as pg
from os import getenv, path
from typing import Type, Optional, Tuple

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv

    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))


class Database:
    conn: pg.extensions.connection = None
    cur: pg.extensions.cursor = None

    @staticmethod
    def setup():
        try:
            Database.conn = pg.connect(
                dbname=getenv("dbname"),
                user=getenv("user"),
                password=getenv("password"),
                host=getenv("host"),
                port=getenv("port"),
            )
            Database.cur = Database.conn.cursor()
            querySQL = open(path.join(path.dirname(__file__), "tables.sql"), "r").read()
            Database.cur.execute(querySQL)
        except Exception as e:
            print(f"Database error: {e}")
        Database.conn.commit()
    


    @staticmethod
    def fetchAll(columns: str, table: str, condition: str):
        Database.cur.execute(f"SELECT {columns} FROM {table} WHERE {condition}")
        return Database.cur.fetchall()
    
    @staticmethod
    def fetchOne(columns: str, table: str, condition: str) -> tuple[any, ...]:
        Database.cur.execute(f"SELECT {columns} FROM {table} WHERE {condition}")
        return Database.cur.fetchone()
    
    @staticmethod
    def insertInto(table: str, columns: str, values: str) -> list:
        Database.cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({values})")
        Database.conn.commit()
    
    def update(table: str, set: str, condition: str) -> list:
        Database.cur.execute(f"UPDATE {table} SET {set} WHERE {condition}")
        Database.conn.commit()
    

    @staticmethod
    def close():
        Database.cur.close()
        Database.conn.close()


    

