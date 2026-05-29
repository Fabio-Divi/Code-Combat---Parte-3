from runner import Runner
from icebreaker import Icebreaker


if __name__ == "__main__":

    # costruisco due icebreaker (name, min_damage, max_damage, type)
    ice1 = Icebreaker("BlackIce Fracter", 5, 9, "fracter")
    ice2 = Icebreaker("Pipeline Decoder", 4, 8, "decoder")

    runner1 = Runner("neo", 20, 12, 8, ice1)
    runner2 = Runner("trinity", 20, 10, 11, ice2)

    while runner1.is_alive() and runner2.is_alive():

        damage1 = runner1.attack(runner2)
        print(f"{runner1.get_handle()} hits {runner2.get_handle()} for {damage1}")

        if not runner2.is_alive():
            break

        damage2 = runner2.attack(runner1)
        print(f"{runner2.get_handle()} hits {runner1.get_handle()} for {damage2}")

    # outcome finale
    if runner1.is_alive():
        print(f"{runner1.get_handle()} wins")
    else:
        print(f"{runner2.get_handle()} wins")