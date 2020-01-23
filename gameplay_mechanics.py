from game_characters import Orderus, WildBeast
from typing import Union

CHARACTER_TYPE = Union[Orderus, WildBeast]
TOTAL_FIGHT_ROUNDS = 20


class Gameplay:
    def __init__(self):
        self.last_attacker = None

    def simulate_round(self,
                       attacker: CHARACTER_TYPE,
                       defender: CHARACTER_TYPE):
        if defender.is_lucky:
            print(f"{defender.name} s-a ferit!")
            self.last_attacker = attacker
            return
        damage_dealt = attacker.strength - defender.defence
        if isinstance(attacker, Orderus):
            damage_dealt = attacker.rapid_strike_damage(damage_dealt)
        else:
            damage_dealt = defender.magic_shield_mitigation(damage_dealt)
        print(
            f"{attacker.name} loveste {defender.name} cu {damage_dealt} damage"
        )
        defender.health -= damage_dealt
        self.last_attacker = attacker
        return

    def simulate_fight(self,
                       emag_hero: Orderus = Orderus(),
                       emagia_beast: WildBeast = WildBeast()):
        if emag_hero.speed == emagia_beast.speed:
            if emag_hero.luck >= emagia_beast.luck:
                print(f"{emag_hero.name} loveste primul (mai norocos)")
                self.simulate_round(attacker=emag_hero, defender=emagia_beast)
            else:
                print(f"{emagia_beast.name} loveste primul (mai norocos)")
                self.simulate_round(attacker=emagia_beast, defender=emag_hero)
        elif emag_hero.speed > emagia_beast.speed:
            print(f"{emag_hero.name} loveste primul (mai rapid)")
            self.simulate_round(attacker=emag_hero, defender=emagia_beast)
        else:
            print(f"{emagia_beast.name} loveste primul (mai rapid)")
            self.simulate_round(attacker=emagia_beast, defender=emag_hero)

        for fight_round in range(1, TOTAL_FIGHT_ROUNDS):
            if isinstance(self.last_attacker, WildBeast):
                self.simulate_round(attacker=emag_hero, defender=emagia_beast)
                if emagia_beast.health <= 0:
                    print(f"Lupta a luat sfarsit, {emag_hero.name} a castigat")
                    return
            else:
                self.simulate_round(attacker=emagia_beast, defender=emag_hero)
                if emag_hero.health <= 0:
                    print(f"Lupta a luat sfarsit, {emagia_beast.name} castiga")
                    return
        if emag_hero.health >= emagia_beast.health:
            print(f"Lupta a luat sfarsit, {emag_hero.name} a castigat")
        else:
            print(f"Lupta a luat sfarsit, {emagia_beast.name} a castigat")
