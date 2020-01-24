"""
Characters used within the game.

Currently includes Orderus and WildBeast, the game's hero and a beast.
"""
import random

from game_hero import game_constants


class GameCharacter:
    """
    Standard Game Character configuration.
    """
    def __init__(self,
                 name=game_constants.STANDARD_PLAYER_CONFIG["name"],
                 health=game_constants.STANDARD_PLAYER_CONFIG["health"],
                 strength=game_constants.STANDARD_PLAYER_CONFIG["strength"],
                 defence=game_constants.STANDARD_PLAYER_CONFIG["defence"],
                 speed=game_constants.STANDARD_PLAYER_CONFIG["speed"],
                 luck=game_constants.STANDARD_PLAYER_CONFIG["luck"]):
        """
        Game Character instance, having a set of stats.

        :param name: Name of the character
        :param health: health points
        :param strength: strength point
        :param defence: defence points
        :param speed: speed points
        :param luck: luck points, with a check for character luck on each round
        """
        self.name = name
        self.health = random.randint(health[0], health[1])
        self.strength = random.randint(strength[0], strength[1])
        self.defence = random.randint(defence[0], defence[1])
        self.speed = random.randint(speed[0], speed[1])
        self.luck = random.randint(luck[0], luck[1])

    @property
    def is_lucky(self):
        """
        :return: Boolean checking if the character is lucky that round
        """
        return random.randint(0, 100) < self.luck


class Orderus(GameCharacter):
    """
    Game Character (Orderus, the Game's hero)
    """
    def __init__(self):
        """
        Call to the base class, using Orderus's pre-defined stats
        """
        super().__init__(
            name=game_constants.ORDERUS_CONFIG["name"],
            health=game_constants.ORDERUS_CONFIG["health"],
            strength=game_constants.ORDERUS_CONFIG["strength"],
            defence=game_constants.ORDERUS_CONFIG["defence"],
            speed=game_constants.ORDERUS_CONFIG["speed"],
            luck=game_constants.ORDERUS_CONFIG["luck"])

    def rapid_strike_damage(self, damage):
        """
        Strike twice while it’s his turn to attack.
        There’s a 10% chance Orderus will use this skill every time he attacks

        :param damage: damage before aplying the skill check.
        :return: damage after skill appliance check
        """
        if random.randint(0, 100) < 10:
            print(f"{self.name} activates Rapid Strike skill !")
            return damage*2
        else:
            return damage

    def magic_shield_mitigation(self, damage):
        """
        Takes only half of the usual damage when an enemy attacks.
        There’s a 20% change Orderus will use this skill every time he defends

        :param damage: damage before aplying the skill check.
        :return: damage after skill appliance check
        """
        if random.randint(0, 100) < 20:
            print(f"{self.name} activates Magic Shield skill !")
            return damage/2
        else:
            return damage


class WildBeast(GameCharacter):
    """
    Game Character (WildBeast, a beast in the forest)
    """
    def __init__(self):
        """
        Call to the base class, using WildBeast's pre-defined stats
        """
        super().__init__(
            name=game_constants.WILDBEAST_CONFIG["name"],
            health=game_constants.WILDBEAST_CONFIG["health"],
            strength=game_constants.WILDBEAST_CONFIG["strength"],
            defence=game_constants.WILDBEAST_CONFIG["defence"],
            speed=game_constants.WILDBEAST_CONFIG["speed"],
            luck=game_constants.WILDBEAST_CONFIG["luck"])
