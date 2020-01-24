from typing import Union

from game_hero import game_characters
from game_hero import game_constants


CHARACTER_TYPE = Union[game_characters.Orderus, game_characters.WildBeast]


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Gameplay(metaclass=Singleton):
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
        if isinstance(attacker, game_characters.Orderus):
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
                       game_hero: game_characters.Orderus,
                       magical_beast: game_characters.WildBeast):
        if game_hero.speed == magical_beast.speed:
            if game_hero.luck >= magical_beast.luck:
                print(f"{game_hero.name} loveste primul (mai norocos)")
                self.simulate_round(attacker=game_hero, defender=magical_beast)
            else:
                print(f"{magical_beast.name} loveste primul (mai norocos)")
                self.simulate_round(attacker=magical_beast, defender=game_hero)
        elif game_hero.speed > magical_beast.speed:
            print(f"{game_hero.name} loveste primul (mai rapid)")
            self.simulate_round(attacker=game_hero, defender=magical_beast)
        else:
            print(f"{magical_beast.name} loveste primul (mai rapid)")
            self.simulate_round(attacker=magical_beast, defender=game_hero)

        for fight_round in range(1, game_constants.TOTAL_FIGHT_ROUNDS):
            if isinstance(self.last_attacker, game_characters.WildBeast):
                self.simulate_round(attacker=game_hero, defender=magical_beast)
                if magical_beast.health <= 0:
                    print(f"Lupta a luat sfarsit, {game_hero.name} a castigat")
                    return
            else:
                self.simulate_round(attacker=magical_beast, defender=game_hero)
                if game_hero.health <= 0:
                    print(f"Lupta s-a sfarsit, {magical_beast.name} castiga")
                    return
        if game_hero.health >= magical_beast.health:
            print(f"Lupta a luat sfarsit, {game_hero.name} a castigat")
        else:
            print(f"Lupta a luat sfarsit, {magical_beast.name} a castigat")
