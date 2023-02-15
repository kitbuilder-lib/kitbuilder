class Meta:
    __meta: dict = {}

    def get(self) -> dict:
        return self.__meta

    def add(self, key: str, value: str) -> None:
        self.__meta[key] = value
