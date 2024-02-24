from database.db import Database

class ProductService:

    @staticmethod
    def getSellerById(id: int):
        Database.cur.execute(f"""--sql SELECT * FROM users WHERE id = {id}""")
        return Database.cur.fetchone()
    
    @staticmethod
    def getSellerFieldById(id: int, field: str):
        Database.cur.execute(f"""--sql SELECT {field} FROM users WHERE id = {id}""")
        return Database.cur.fetchone()
    