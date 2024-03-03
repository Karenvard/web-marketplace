

class type_handler:

    @staticmethod
    def get_all(payload: dict) -> Dict[str, str]:
        # 1. get types
        # 2. return types
        pass

    @staticmethod
    def add(payload: dict) -> Dict[str, str]:
        # 1. get type
        # 2. check if type exists
        # 3. insert type into database
        # 4. return success message {"message": "Type was created successfully."}
        pass

    @staticmethod
    def get(payload: dict) -> Dict[str, str]:
        # 1. check if type exists
        # 2. get type
        # 3. return type
        pass

    @staticmethod
    def update(payload: dict) -> Dict[str, str]:
        # 1. get type
        # 2. check if type exists
        # 3. update type
        pass

    @staticmethod
    def delete(payload: dict) -> Dict[str, str]:
        # 1. get type
        # 2. check if type exists
        # 3. delete type
        pass
