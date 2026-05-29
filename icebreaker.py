import random


class Icebreaker:
    def __init__(self, name: str, min_damage: int, max_damage: int, type: str):
        # attributi privati
        self.__name = name

        # validazione minima per i danni
        if not isinstance(min_damage, int) or min_damage < 0:
            print("ATTENZIONE: min_damage deve essere un intero non negativo, imposto a 0")
            min_damage = 0
        self.__min_damage = min_damage

        if not isinstance(max_damage, int) or max_damage < self.__min_damage:
            print("ATTENZIONE: max_damage deve essere un intero >= min_damage, imposto a min_damage")
            max_damage = self.__min_damage
        self.__max_damage = max_damage

        if type not in ("fracter", "decoder"):
            print("ATTENZIONE: type deve essere 'fracter' o 'decoder', imposto a 'fracter'")
            self.__type = "fracter"
        else:
            self.__type = type

    # getters
    def get_name(self) -> str:
        return self.__name

    def get_min_damage(self) -> int:
        return self.__min_damage

    def get_max_damage(self) -> int:
        return self.__max_damage

    def get_type(self) -> str:
        return self.__type

    # setters con validazione
    def set_min_damage(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            print("ATTENZIONE: min_damage deve essere un intero non negativo")
            return
        if value > self.__max_damage:
            print("ATTENZIONE: min_damage non può superare max_damage")
            return
        self.__min_damage = value

    def set_max_damage(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            print("ATTENZIONE: max_damage deve essere un intero non negativo")
            return
        if value < self.__min_damage:
            print("ATTENZIONE: max_damage non può essere minore di min_damage")
            return
        self.__max_damage = value

    def get_damage(self) -> int:
        return random.randint(self.__min_damage, self.__max_damage)

    def __str__(self) -> str:
        return f"{self.__name} ({self.__type} {self.__min_damage}–{self.__max_damage} dmg)"
