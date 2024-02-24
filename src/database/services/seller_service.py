from database.db import Database

class SellerService:

    @staticmethod
    def getSellerById(id: int):
        Database.cur.execute(f"""--sql SELECT * FROM sellers WHERE id = {id}""")
        return Database.cur.fetchone()
    
    @staticmethod
    def getSellerFieldById(id: int, field: str):
        Database.cur.execute(f"""--sql SELECT {field} FROM sellers WHERE id = {id}""")
        return Database.cur.fetchone()
    