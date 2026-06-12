import random

from chip import Chip
from icebreaker import Icebreaker
from runner import Runner


def create_random_icebreaker(name: str) -> Icebreaker:
    ice_type = random.choice(("fracter", "decoder"))
    min_damage = random.randint(2, 5)
    max_damage = random.randint(min_damage, min_damage + 5)
    return Icebreaker(name, min_damage, max_damage, ice_type)


def create_chips() -> list[Chip]:
    return [
        Chip("Patch", "repair", random.randint(4, 7)),
        Chip("Overclock", "overclock", random.randint(2, 4), random.randint(1, 3)),
        Chip("Sharpen", "sharpen", random.randint(2, 4), random.randint(1, 3)),
    ]


def create_runner(handle: str, icebreaker_name: str) -> Runner:
    return Runner(
        handle,
        random.randint(18, 26),
        random.randint(6, 16),
        random.randint(6, 16),
        create_random_icebreaker(icebreaker_name),
        create_chips(),
    )


def format_chip_log(runner: Runner, chip: Chip, result: dict) -> str:
    if "error" in result:
        return f"{runner.get_handle()} prova a usare {chip.name}, ma fallisce ({result['error']})"

    if result["effect"] == "repair":
        return f"{runner.get_handle()} usa {chip.name}: recupera {result['amount']} integrity"

    stat = "power" if result["effect"] == "overclock" else "finesse"
    return (
        f"{runner.get_handle()} usa {chip.name}: +{result['amount']} {stat} "
        f"per {result['duration']} turni"
    )


def play_turn(attacker: Runner, defender: Runner) -> None:
    chip = attacker.should_use_chip(defender)
    if chip is not None:
        log = attacker.use_chip(chip)
        print(format_chip_log(attacker, chip, log))

    damage = attacker.attack(defender)
    print(
        f"{attacker.get_handle()} attacca {defender.get_handle()} "
        f"e infligge {damage} danni "
        f"({defender.get_integrity()}/{defender.get_max_integrity()} integrity)"
    )


if __name__ == "__main__":
    runner1 = create_runner("neo", "BlackIce")
    runner2 = create_runner("trinity", "Pipeline")

    print(f"{runner1} con {runner1.get_icebreaker()}")
    print(f"{runner2} con {runner2.get_icebreaker()}")
    print()

    while runner1.is_alive() and runner2.is_alive():
        play_turn(runner1, runner2)
        if runner2.is_alive():
            play_turn(runner2, runner1)

        runner1.tick_buffs()
        runner2.tick_buffs()
        print()

    if runner1.is_alive() and runner2.is_alive():
        print("Pareggio")
    elif runner1.is_alive():
        print(f"{runner1.get_handle()} wins")
    elif runner2.is_alive():
        print(f"{runner2.get_handle()} wins")
    else:
        print("Pareggio")
