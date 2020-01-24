"""
Example of using the `game_hero` module.

Imports the module, instantiates the game,
after which just calls the `start_game()` method,
which handles the gameplay mechanics and functionality.
"""
from game_hero import main_game

hero_game = main_game.HeroGame()
hero_game.start_game()
