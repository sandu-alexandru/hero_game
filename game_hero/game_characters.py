import random

from game_hero import game_constants


class GameCharacter:
    def __init__(self,
                 name=game_constants.STANDARD_PLAYER_CONFIG["name"],
                 health=game_constants.STANDARD_PLAYER_CONFIG["health"],
                 strength=game_constants.STANDARD_PLAYER_CONFIG["strength"],
                 defence=game_constants.STANDARD_PLAYER_CONFIG["defence"],
                 speed=game_constants.STANDARD_PLAYER_CONFIG["speed"],
                 luck=game_constants.STANDARD_PLAYER_CONFIG["luck"]):
        self.name = name
        self.health = random.randint(health[0], health[1])
        self.strength = random.randint(strength[0], strength[1])
        self.defence = random.randint(defence[0], defence[1])
        self.speed = random.randint(speed[0], speed[1])
        self.luck = random.randint(luck[0], luck[1])

    @property
    def is_lucky(self):
        return random.randint(0, 100) < self.luck


class Orderus(GameCharacter):
    def __init__(self):
        super().__init__(
            name=game_constants.ORDERUS_CONFIG["name"],
            health=game_constants.ORDERUS_CONFIG["health"],
            strength=game_constants.ORDERUS_CONFIG["strength"],
            defence=game_constants.ORDERUS_CONFIG["defence"],
            speed=game_constants.ORDERUS_CONFIG["speed"],
            luck=game_constants.ORDERUS_CONFIG["luck"])

    @staticmethod
    def rapid_strike_damage(damage):
        if random.randint(0, 100) < 10:
            print("Skill-ul Rapid Strike a fost activat!")
            return damage*2
        else:
            return damage

    @staticmethod
    def magic_shield_mitigation(damage):
        if random.randint(0, 100) < 20:
            print("Skill-ul Magic Shield a fost activat!")
            return damage / 2
        else:
            return damage


class WildBeast(GameCharacter):
    def __init__(self):
        super().__init__(
            name=game_constants.WILDBEAST_CONFIG["name"],
            health=game_constants.WILDBEAST_CONFIG["health"],
            strength=game_constants.WILDBEAST_CONFIG["strength"],
            defence=game_constants.WILDBEAST_CONFIG["defence"],
            speed=game_constants.WILDBEAST_CONFIG["speed"],
            luck=game_constants.WILDBEAST_CONFIG["luck"])
