from icebreaker import Icebreaker


class Runner:

    def __init__(self, handle: str, max_integrity: int, power: int, finesse: int, icebreaker: Icebreaker | None):
        # attributi privati
        if handle == "":
            print("Handle cannot be empty")
            handle = "molly"
        self.__handle = handle

        if max_integrity >= 1:
            self.__max_integrity = max_integrity
        else:
            print("Max integrity must be at least 1")
            self.__max_integrity = 1

        # integrità corrente inizia pari al massimo
        self.__integrity = self.__max_integrity

        if 1 <= power <= 20:
            self.__power = power
        else:
            print("Power must be between 1 and 20")
            self.__power = 1   

        if 1 <= finesse <= 20:
            self.__finesse = finesse
        else:
            print("Finesse must be between 1 and 20")
            self.__finesse = 1

        self.__icebreaker = icebreaker
        self.__damage_log = []

    # getters
    def get_handle(self) -> str:
        return self.__handle

    def get_integrity(self) -> int:
        return self.__integrity

    def get_max_integrity(self) -> int:
        return self.__max_integrity

    def get_power(self) -> int:
        return self.__power

    def get_finesse(self) -> int:
        return self.__finesse

    def get_icebreaker(self) -> Icebreaker | None:
        return self.__icebreaker

    def get_damage_log(self) -> list:
        return list(self.__damage_log)

    def equip(self, icebreaker: Icebreaker) -> None:
        self.__icebreaker = icebreaker

    def modifier(self, value: int) -> int:
        return (value - 10) // 2

    def is_alive(self) -> bool:
        return self.__integrity > 0

    def take_damage(self, amount: int) -> int:
        if not isinstance(amount, int) or amount < 0:
            print("ATTENZIONE: damage deve essere un intero non negativo")
            return self.__integrity
        self.__integrity -= amount
        if self.__integrity < 0:
            self.__integrity = 0
        self.__damage_log.append(amount)
        return self.__integrity

    def heal(self, amount: int) -> int:
        if not isinstance(amount, int) or amount < 0:
            print("ATTENZIONE: heal deve essere un intero non negativo")
            return self.__integrity
        self.__integrity += amount
        if self.__integrity > self.__max_integrity:
            self.__integrity = self.__max_integrity
        return self.__integrity

    def attack(self, enemy: "Runner") -> int:
        # danno base
        if self.__icebreaker is None:
            damage = 1
        else:
            damage = self.__icebreaker.get_damage()

            # aggiunta modificatore in base al tipo
            ice_type = self.__icebreaker.get_type()
            if ice_type == "fracter":
                damage += self.modifier(self.__power)

            elif ice_type == "decoder":
                damage += self.modifier(self.__finesse)

        # il danno non può essere negativo
        if damage < 0:
            damage = 0

        # applica il danno al nemico
        return enemy.take_damage(damage)
        
    def __str__(self) -> str:
        return f"{self.__handle} ({self.__max_integrity} {self.__power} {self.__finesse})"