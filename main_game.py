import game_characters
import gameplay_mechanics

orderus = game_characters.Orderus()
wild_beast = game_characters.WildBeast()

game_instance = gameplay_mechanics.Gameplay()
game_instance.simulate_fight(emag_hero=orderus, emagia_beast=wild_beast)
