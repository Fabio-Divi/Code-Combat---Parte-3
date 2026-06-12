from icebreaker import Icebreaker
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
from chip import Chip
>>>>>>> theirs
=======
from chip import Chip
>>>>>>> theirs
=======
from chip import Chip
>>>>>>> theirs


class Runner:

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
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
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    def __init__(
        self,
        handle: str,
        max_integrity: int,
        power: int,
        finesse: int,
        icebreaker: Icebreaker | None,
        chips: list[Chip] | None = None,
    ):
        if not isinstance(handle, str) or handle == "":
            print("ATTENZIONE: handle non puo essere vuoto, imposto a 'molly'")
            handle = "molly"
        self.__handle = handle

        if not isinstance(max_integrity, int) or max_integrity < 1:
            print("ATTENZIONE: max_integrity deve essere almeno 1, imposto a 1")
            max_integrity = 1
        self.__max_integrity = max_integrity

        self.__integrity = self.__max_integrity
        self.__power = 1
        self.__finesse = 1
        self.__icebreaker = None
        self.__buffs: list[tuple[str, int, int]] = []
        self.__chips: list[Chip] = []
        self.__damage_log = []

        self.power = power
        self.finesse = finesse
        self.icebreaker = icebreaker
        if chips is not None:
            self.chips = chips

    @property
    def handle(self) -> str:
        return self.__handle

    @property
    def integrity(self) -> int:
        return self.__integrity

    @integrity.setter
    def integrity(self, value: int) -> None:
        if not isinstance(value, int):
            print("ATTENZIONE: integrity deve essere un intero")
            return
        self.__integrity = value
        self.__clamp_integrity()

    @property
    def max_integrity(self) -> int:
        return self.__max_integrity

    @property
    def power(self) -> int:
        return self.__power

    @power.setter
    def power(self, value: int) -> None:
        if not isinstance(value, int) or not 1 <= value <= 20:
            print("ATTENZIONE: power deve essere compreso tra 1 e 20, imposto a 1")
            value = 1
        self.__power = value

    @property
    def finesse(self) -> int:
        return self.__finesse

    @finesse.setter
    def finesse(self, value: int) -> None:
        if not isinstance(value, int) or not 1 <= value <= 20:
            print("ATTENZIONE: finesse deve essere compreso tra 1 e 20, imposto a 1")
            value = 1
        self.__finesse = value

    @property
    def icebreaker(self) -> Icebreaker | None:
        return self.__icebreaker

    @icebreaker.setter
    def icebreaker(self, value: Icebreaker | None) -> None:
        if value is not None and not isinstance(value, Icebreaker):
            print("ATTENZIONE: icebreaker deve essere un Icebreaker oppure None")
            return
        self.__icebreaker = value

    @property
    def effective_power(self) -> int:
        return self.__power + self.__buff_total("power")

    @property
    def effective_finesse(self) -> int:
        return self.__finesse + self.__buff_total("finesse")

    @property
    def chips(self) -> list[Chip]:
        return self.__chips

    @chips.setter
    def chips(self, value: list[Chip]) -> None:
        if not isinstance(value, list):
            print("ATTENZIONE: chips deve essere una lista")
            return
        if len(value) > 3:
            print("ATTENZIONE: un Runner puo avere al massimo 3 chip")
            return
        for chip in value:
            if not isinstance(chip, Chip):
                print("ATTENZIONE: chips puo contenere solo oggetti Chip")
                return
        self.__chips = value

    def get_handle(self) -> str:
        return self.handle

    def get_integrity(self) -> int:
        return self.integrity

    def get_max_integrity(self) -> int:
        return self.max_integrity

    def get_power(self) -> int:
        return self.power

    def get_finesse(self) -> int:
        return self.finesse

    def get_icebreaker(self) -> Icebreaker | None:
        return self.icebreaker
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

    def get_damage_log(self) -> list:
        return list(self.__damage_log)

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    def equip(self, icebreaker: Icebreaker) -> None:
        self.__icebreaker = icebreaker
=======
    def equip(self, icebreaker: Icebreaker | None) -> None:
        self.icebreaker = icebreaker
>>>>>>> theirs
=======
    def equip(self, icebreaker: Icebreaker | None) -> None:
        self.icebreaker = icebreaker
>>>>>>> theirs
=======
    def equip(self, icebreaker: Icebreaker | None) -> None:
        self.icebreaker = icebreaker
>>>>>>> theirs

    def modifier(self, value: int) -> int:
        return (value - 10) // 2

    def is_alive(self) -> bool:
        return self.__integrity > 0

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    def take_damage(self, amount: int) -> int:
        if not isinstance(amount, int) or amount < 0:
            print("ATTENZIONE: damage deve essere un intero non negativo")
            return self.__integrity
        self.__integrity -= amount
        if self.__integrity < 0:
            self.__integrity = 0
        self.__damage_log.append(amount)
        return self.__integrity

=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
    def heal(self, amount: int) -> int:
        if not isinstance(amount, int) or amount < 0:
            print("ATTENZIONE: heal deve essere un intero non negativo")
            return self.__integrity
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
        self.__integrity += amount
        if self.__integrity > self.__max_integrity:
            self.__integrity = self.__max_integrity
        return self.__integrity

    def attack(self, enemy: "Runner") -> int:
        # danno base
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
        self.integrity = self.__integrity + amount
        return self.__integrity

    def add_buff(self, stat: str, amount: int, duration: int) -> None:
        if stat not in ("power", "finesse"):
            print("ATTENZIONE: stat deve essere 'power' o 'finesse'")
            return
        if not isinstance(amount, int) or amount < 1:
            print("ATTENZIONE: amount deve essere un intero >= 1")
            return
        if not isinstance(duration, int) or duration < 1:
            print("ATTENZIONE: duration deve essere un intero >= 1")
            return
        self.__buffs.append((stat, amount, duration))

    def tick_buffs(self) -> None:
        active_buffs = []
        for stat, amount, duration in self.__buffs:
            duration -= 1
            if duration > 0:
                active_buffs.append((stat, amount, duration))
        self.__buffs = active_buffs

    def use_chip(self, c: "Chip") -> dict:
        if not isinstance(c, Chip):
            print("ERRORE: puoi usare solo oggetti Chip")
            return {"error": "invalid_chip"}
        if c not in self.__chips:
            print("ERRORE: chip non presente nell'inventario")
            return {"error": "chip_not_owned"}

        result = c.apply_to(self)
        if "error" not in result:
            self.__chips.remove(c)
        return result

    def should_use_chip(self, enemy: "Runner") -> "Chip | None":
        if self.__integrity <= self.__max_integrity // 2:
            for chip in self.__chips:
                if chip.effect == "repair":
                    return chip

        if self.__icebreaker is None:
            return None

        preferred_effect = "overclock"
        if self.__icebreaker.get_type() == "decoder":
            preferred_effect = "sharpen"

        for chip in self.__chips:
            if chip.effect == preferred_effect:
                return chip

        return None

    def attack(self, enemy: "Runner") -> int:
        chip = self.should_use_chip(enemy)
        if chip is not None:
            self.use_chip(chip)

        damage = self.__calculate_damage()
        enemy.__take(damage)
        return damage

    def take_damage(self, amount: int) -> int:
        return self.__take(amount)

    def __take(self, damage: int) -> int:
        if not isinstance(damage, int) or damage < 0:
            print("ATTENZIONE: damage deve essere un intero non negativo")
            return self.__integrity
        self.integrity = self.__integrity - damage
        self.__damage_log.append(damage)
        return self.__integrity

    def __calculate_damage(self) -> int:
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
        if self.__icebreaker is None:
            damage = 1
        else:
            damage = self.__icebreaker.get_damage()
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours

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
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
            ice_type = self.__icebreaker.get_type()

            if ice_type == "fracter":
                damage += self.modifier(self.effective_power)
            elif ice_type == "decoder":
                damage += self.modifier(self.effective_finesse)

        if damage < 0:
            damage = 0
        return damage

    def __clamp_integrity(self) -> None:
        if self.__integrity < 0:
            self.__integrity = 0
        elif self.__integrity > self.__max_integrity:
            self.__integrity = self.__max_integrity

    def __buff_total(self, stat: str) -> int:
        total = 0
        for buff_stat, amount, duration in self.__buffs:
            if buff_stat == stat and duration > 0:
                total += amount
        return total

    def __str__(self) -> str:
        return (
            f"{self.__handle} "
            f"({self.__integrity}/{self.__max_integrity} "
            f"P{self.effective_power} F{self.effective_finesse})"
        )
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
