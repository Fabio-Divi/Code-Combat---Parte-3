import random


class Icebreaker:
    VALID_TYPES = ("fracter", "decoder")

    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        self.__name = ""
        self.__min_damage = 1
        self.__max_damage = 1
        self.__type = "fracter"

        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or value == "":
            value = "icebreaker"
        self.__name = value

    @property
    def min_damage(self) -> int:
        return self.__min_damage

    @min_damage.setter
    def min_damage(self, value: int) -> None:
        if not isinstance(value, int) or value < 1:
            value = 1
        self.__min_damage = value
        if self.__max_damage < self.__min_damage:
            self.__max_damage = self.__min_damage

    @property
    def max_damage(self) -> int:
        return self.__max_damage

    @max_damage.setter
    def max_damage(self, value: int) -> None:
        if not isinstance(value, int) or value < self.__min_damage:
            value = self.__min_damage
        self.__max_damage = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str) -> None:
        if value not in self.VALID_TYPES:
            value = "fracter"
        self.__type = value

    def get_name(self) -> str:
        return self.name

    def get_min_damage(self) -> int:
        return self.min_damage

    def get_max_damage(self) -> int:
        return self.max_damage

    def get_type(self) -> str:
        return self.type

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"{self.__name} ({self.__type} {self.__min_damage}-{self.__max_damage} dmg)"
