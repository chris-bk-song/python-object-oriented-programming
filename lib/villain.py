from lib.character import Character
# from . import character # alternate version

# Villain is a subclass of Character
# Villain inherits from Character
# Character is the super class of Villain
class Villain(Character):
# class Villain(character.Character): # alternate version
    def receive_damage(self, how_much):
        self.health -= how_much
        if self.health <= 0:
            self.health = 5