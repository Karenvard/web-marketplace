import psycopg2 as pg
from os import getenv, path
from typing import Any

if path.exists(path.join(path.dirname(__file__), "..", "..", ".env")):
    from dotenv import load_dotenv

    load_dotenv(path.join(path.dirname(__file__), "..", "..", ".env"))


class Database:
    conn: pg.extensions.connection
    cur: pg.extensions.cursor
    
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
            Database.cur.execute("SELECT COUNT(*) FROM roles")
            count = len(Database.cur.fetchall())
            if count < 2:
                Database.cur.execute("DELETE FROM roles")
                Database.cur.execute("INSERT INTO roles (name) VALUES ('ADMIN')")
                Database.cur.execute("INSERT INTO roles (name) VALUES ('USER')")
        except Exception as e:
            print(f"Database error: {e}")
        finally:
            Database.conn.commit()
    
    @staticmethod
    def setupForTest():
        try:
            Database.conn = pg.connect(
                dbname="test",
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
        finally:
            Database.conn.commit()

    @staticmethod
    def fetchAll(query: str) -> list[tuple[Any, ...]]:
        Database.cur.execute(query)
        return Database.cur.fetchall()
    
    @staticmethod
    def fetchOne(query: str) -> tuple[Any, ...]:
        Database.cur.execute(query)
        return Database.cur.fetchone() or ()

    @staticmethod
    def commit(query: str):
        Database.cur.execute(query)
        Database.conn.commit()


    @staticmethod
    def close():
        Database.cur.close()
        Database.conn.close()


    

