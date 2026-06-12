class Chip:
    VALID_EFFECTS = ("repair", "overclock", "sharpen")

    def __init__(self, name: str, effect: str, amount: int, duration: int = 0):
        self.__name = ""
        self.__effect = "repair"
        self.__amount = 1
        self.__duration = 0
        self.__burned = False

        self.name = name
        self.effect = effect
        self.amount = amount
        self.duration = duration

        if self.__effect == "repair":
            self.__duration = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str) or value == "":
            print("ATTENZIONE: name non puo essere vuoto, imposto a 'chip'")
            value = "chip"
        self.__name = value

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, value: str) -> None:
        if value not in self.VALID_EFFECTS:
            print("ATTENZIONE: effect deve essere 'repair', 'overclock' o 'sharpen', imposto a 'repair'")
            value = "repair"
        self.__effect = value
        if self.__effect == "repair":
            self.__duration = 0

    @property
    def amount(self) -> int:
        return self.__amount

    @amount.setter
    def amount(self, value: int) -> None:
        if not isinstance(value, int) or value < 1:
            print("ATTENZIONE: amount deve essere un intero >= 1, imposto a 1")
            value = 1
        self.__amount = value

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            print("ATTENZIONE: duration deve essere un intero >= 0, imposto a 0")
            value = 0
        if self.__effect == "repair":
            value = 0
        self.__duration = value

    def apply_to(self, target) -> dict:
        if self.__burned:
            print("ERRORE: chip gia bruciato")
            return {"error": "already_burned"}

        if self.__effect == "repair":
            if not self.__has_method(target, "heal"):
                print("ERRORE: il target non espone un metodo 'heal' richiamabile")
                return {"error": "unsupported_target"}

            self.__apply_repair(target)
        else:
            if not self.__has_method(target, "add_buff"):
                print("ERRORE: il target non espone un metodo 'add_buff' richiamabile")
                return {"error": "unsupported_target"}

            stat = "power" if self.__effect == "overclock" else "finesse"
            self.__apply_boost(target, stat)

        self.__burned = True
        return {
            "effect": self.__effect,
            "amount": self.__amount,
            "duration": self.__duration,
        }

    def __apply_repair(self, target) -> int:
        return target.heal(self.__amount)

    def __apply_boost(self, target, stat: str) -> int:
        target.add_buff(stat, self.__amount, self.__duration)
        return self.__amount

    def __has_method(self, target, method_name: str) -> bool:
        return hasattr(target, method_name) and callable(getattr(target, method_name))

    def __str__(self) -> str:
        if self.__duration == 0:
            return f"Chip({self.__effect} +{self.__amount})"
        return f"Chip({self.__effect} +{self.__amount} x{self.__duration}t)"
