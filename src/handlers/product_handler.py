


class product_handler:

    @staticmethod
    def add(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. check if product exists
        # 3. insert product into database
        # 4. return success message {"message": "Product was created successfully."}
        pass

    @staticmethod
    def update(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. update product
        pass

    @staticmethod
    def get(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. return product
        pass

    @staticmethod
    def get_all(payload: dict) -> Dict[str, str]:
        # 1. get products
        # 2. return products
        pass

    @staticmethod
    def delete(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. delete product
        pass

    @staticmethod
    def rate(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. check if already rated by current user
        # 3. rate product
        pass
    
    @staticmethod
    def get_ratings(payload: dict) -> Dict[str, str]:
        # 1. get product
        # 2. get ratings
        pass
