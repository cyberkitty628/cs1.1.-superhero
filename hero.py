from random import choice

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
        heroes_list = [self.name, opponent.name]
        print(choice(heroes_list) + " wins!")

if __name__ == "__main__":
     # If you run this file from the terminal
     # this block is executed.
    hero_1 = Hero("Catwoman")
    hero_2 = Hero("Batman")

    hero_1.fight(hero_2)