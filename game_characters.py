import random


class GameCharacter:
    def __init__(self,
                 name="InGameCharacter",
                 health=(0, 100),
                 strength=(0, 100),
                 defence=(0, 100),
                 speed=(0, 100),
                 luck=(0, 100)):
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
        super().__init__(name="Orderus",
                         health=(70, 100),
                         strength=(70, 80),
                         defence=(45, 55),
                         speed=(40, 50),
                         luck=(10, 30))

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
        super().__init__(name="WildBeast",
                         health=(60, 90),
                         strength=(60, 90),
                         defence=(40, 60),
                         speed=(40, 60),
                         luck=(25, 40))
