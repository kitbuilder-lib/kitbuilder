class Environment:
    __data: dict = {}

    def add(self, key: str, value: str) -> None:
        self.__data[key] = value

    def get(self, key: str) -> str:
        return self.__data[key]

    def list_all(self) -> dict:
        return self.__data

    def merge(self, env_obj) -> None:
        self.__data = { **self.__data, **env_obj.__data }
