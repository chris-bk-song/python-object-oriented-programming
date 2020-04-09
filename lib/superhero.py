from lib.character import Character

class Superhero(Character):
    def strike(self, target):
        # they can strike 3 times
        super().strike(target)
        super().strike(target)
        super().strike(target)


    def super_strike(self, target):
        # super().strike(target)
        # Since .strike() does not accept a power argument
        # we cannot write super_strike() in terms
        # of .strike()
        target.receive_damage(self.power * 10)