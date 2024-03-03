

class basket_handler:

    @staticmethod
    def add_product(payload: dict) -> Dict[str, str]:
        # 1. check if product in basket with given id exists
        # 2. get product
        # 3. add product to basket
        # 4. return success message {"message": "Product was added to basket successfully."}
        pass

    @staticmethod
    def get(payload: dict) -> Dict[str, str]:
        # 1. get basket
        # 2. return basket
        pass

    @staticmethod
    def delete_product(payload: dict) -> Dict[str, str]:
        # 1. check if product in basket with given id exists
        # 2. get product
        # 3. delete product from basket
        # 4. return success message {"message": "Product was deleted from basket successfully."}
        pass
