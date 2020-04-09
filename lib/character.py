
class Character():
    # double underscore is pronounced "dunder" by python programmers
    def __init__(self, name, secret_identity, power=10, health=50, armor=5):
        print('Creating a new character in __init__')
        self.name = name
        self.secret_identity = secret_identity

        self.health = health
        self.power = power   
        self.armor = armor 

    # This is the "representation" function
    def __repr__(self):
        return f'{self.name} has the power of {self.power}'

    def make_entrance(self):
        print(f'{self.name} crashes through the wall')

    def go_to_the_spa(self):
        self.health += 5
        print(f'{self.name} increased their health to {self.health}')

    def status(self):
        if self.health < 50:
            print(f'{self.name} has health {self.health} and looks terrible')
        elif self.health > 150:
            print(f'{self.name} has health {self.health} and looks AMAZING!')
        else:
            print(f'{self.name} has health {self.health} and looks ok')

    def strike(self, target):
        # print(f'you called the strike function of {self.name}!')
        print(f'{self.name} is striking {target.name}')
        # target.health -= self.power
        # A property that is a function is known as a "method"
        target.receive_damage(self.power)
        # We call the target's receive_damage method and pass in self.power

    def receive_damage(self, how_many_points):
        """
        oh hey
        """
        total_damage = how_many_points - self.armor
        self.health -= total_damage
        print(f'{self.name} receives {total_damage} damage')