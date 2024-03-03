

class role_handler:

    @staticmethod
    def add(payload: dict) -> Dict[str, str]:
        # 1. get role
        # 2. check if role exists
        # 3. insert role into database
        # 4. return success message {"message": "Role was created successfully."}
        pass

    @staticmethod
    def get(payload: dict) -> Dict[str, str]:
        # 1. check if role exists
        # 2. get role
        # 3. return role
        pass

    @staticmethod
    def update(payload: dict) -> Dict[str, str]:
        # 1. get role
        # 2. check if role exists
        # 3. update role
        pass

    @staticmethod
    def get_all(payload: dict) -> Dict[str, str]:
        # 1. get roles
        # 2. return roles
        pass

    @staticmethod
    def give(payload: dict) -> Dict[str, str]:
        # 1. get role
        # 2. check if role exists
        # 3. give role
        pass

    @staticmethod
    def delete(payload: dict) -> Dict[str, str]:
        # 1. get role
        # 2. check if role exists
        # 3. delete role
        pass
