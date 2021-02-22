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

    # Old fight method 
    # def fight(self, opponent):
    #     # Create variable to store both names into a list, pass it into the choice() method to pick random name
    #     heroes_list = [self.name, opponent.name]
    #     print(choice(heroes_list) + " wins!")

    # New fight method
    def fight(self, opponent):
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        pass
        
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
        total_block = 0
        for armors in self.armors:
            total_block += armors.block()
        return total_block

    def take_damage(self, damage):
        #Updates self.current_health to reflect the damage minus the defense.
        damage_after_armors = damage - self.defend()
        print(f'Damage taken: {damage_after_armors}')
        self.current_health -= damage_after_armors
        
    def is_alive(self):
    # Returns true or false statement depending on whether the hero's health falls below zero or not
        if hero.current_health <= 0:
            return False
        else:
            return True

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
    hero.add_armor(Armor("defense", 100))
    print(hero.attack())
    print(hero.defend())
    hero.take_damage(50)
    print(hero.current_health)
    print(hero.is_alive())
    #print(hero.abilities)
    #hero_1.fight(hero_2)