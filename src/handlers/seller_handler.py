

class seller_handler:

    @staticmethod
    def create(payload: dict) -> Dict[str, str]:
        # 1. get candidate
        # 2. check if candidate exists
        # 3. insert seller into database
        # 4. return success message {"message": "Seller was created successfully."}
        pass

    @staticmethod
    def update(payload: dict) -> Dict[str, str]:
        # 1. get seller
        # 3. update seller
        pass

    @staticmethod 
    def get_authenticated(payload: dict) -> Dict[str, str]:
        # 1. get seller
        # 2. return seller
        pass

    @staticmethod
    def get(payload: dict) -> Dict[str, str]:
        # 1. get seller
        # 3. return seller
        pass

    @staticmethod
    def delete(payload: dict) -> Dict[str, str]:
        # 1. get seller
        # 3. delete seller
        pass
