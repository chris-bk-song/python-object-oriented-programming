# class String():
#     def upper(self):
#         return upper_case_version_of self.text

class Superhero():
    def __init__(self, hero_name, secret_identity, power='being nice', health=50):
        self.hero_name = hero_name
        self.secret_identity = secret_identity

        self.health = health
        self.power = power

    # This is the "representation" function
    def __repr__(self):
        return f'{self.hero_name} has the power of {self.power}'
    
    def make_entrance(self):
        print(f'{self.hero_name} crashes through the wall')

    def go_to_the_spa(self):
        self.health += 5
        print(f'{self.hero_name} increased their health to {self.health}')
        
    def status(self):
        if self.health < 50:
            print(f'{self.hero_name} has health {self.health} and looks terrible')
        elif self.health > 150:
            print(f'{self.hero_name} has health {self.health} and looks AMAZING!')
        else:
            print(f'{self.hero_name} has health {self.health} and looks ok')

ww = Superhero('Wonder Woman', 'Diana Prince', 'badassery', 100)
hulk = Superhero('Huuuulk', 'Dr Bruce Banner', 'smash', 500)