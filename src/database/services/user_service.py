from database.db import Database
from typing import Optional
import re

class UserService:

    @staticmethod
    def _validateEmail(email: str):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email:
            raise Exception("Email is required.")
        elif not re.match(pattern, email):
            raise Exception("Email is not valid.")
        elif len(email) > 40:
            raise Exception("Email is too long (0 to 40 characters).")
        
    
    @staticmethod
    def _validateFullname(fullname: str):
        pass

    @staticmethod
    def addNew(id: int, email: str, fullname: str, seller_id: int, basket_id: int, password: str):
        UserService._validateEmail(email)
        
        

    @staticmethod
    def getUserById(id: int):
        Database.cur.execute(f"""--sql SELECT * FROM users WHERE id = {id}""")
        return Database.cur.fetchone()
    
    @staticmethod
    def getUserFieldById(id: int, field: str):
        Database.cur.execute(f"""--sql SELECT {field} FROM users WHERE id = {id}""")
        return Database.cur.fetchone()
    