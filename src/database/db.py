import psycopg2 as pg
from os import getenv, path
from typing import Type, Optional

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
            Database.conn.commit()
        except Exception as e:
            print(f"Database error: {e}")


    

