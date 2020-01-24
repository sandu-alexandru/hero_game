from game_hero import game_characters
from game_hero import gameplay_mechanics


class HeroGame(metaclass=gameplay_mechanics.Singleton):
    def __init__(self):
        self._gameplay_functionality = gameplay_mechanics.Gameplay()

    def start_game(self):
        self._gameplay_functionality.simulate_fight(
            game_hero=game_characters.Orderus(),
            magical_beast=game_characters.WildBeast())
