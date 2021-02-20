from random import choice
from ability import Ability
from armor import Armor

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()

    def fight(self, opponent):
        # Create variable to store both names into a list, pass it into the choice() method to pick random name
        heroes_list = [self.name, opponent.name]
        print(choice(heroes_list) + " wins!")

    def add_ability(self, ability):
        # Using the append method to add ability objects to our abilities list.
        self.abilities.append(ability)

    def attack(self):
        # Set total damage to start at 0
        total_damage = 0
        # Use for loop to loop through all of hero's abilities
        # and add (+=) damage of each attack to our total
        for ability in self.abilities:
            total_damage += ability.attack()
            # Return the updated total damage
            return total_damage
    
    def add_armor(self, armor):
        # Using the append method to add armor objects to our armors list
        self.armors.append(armor)
    
    def defend(self):
        for armors in self.armors:
            total_block += armors.block()
            return total_block

    def take_damage(self, damage):
    #Updates self.current_health to reflect the damage minus the defense.
    # TODO: Create a method that updates self.current_health to the current
    # minus the the amount returned from calling self.defend(damage).
        

if __name__ == "__main__":
     # If you run this file from the terminal
     # this block is executed.
    #hero_1 = Hero("Catwoman")
    #hero_2 = Hero("Batman")
    ability = Ability("Great Debugging", 50)
    ability_2 = Ability("Great Attack", 100)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(ability_2)
    print(hero.attack())
    print(hero.defend())
    #print(hero.abilities)
    #hero_1.fight(hero_2)