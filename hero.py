from random import choice
from ability import Ability
from weapon import Weapon
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
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.is_alive() and opponent.is_alive():
                hero_total_damage = self.attack()
                opponent.take_damage(hero_total_damage)

                opponent_total_damage = opponent.attack()
                self.take_damage(opponent_total_damage)

                if not self.is_alive() or not opponent.is_alive():
                    print("Both died :(")
                elif not self.is_alive():
                    print(f"{opponent.name} won!")
                elif not opponent.is_alive():
                    print(f"{self.name} won!")
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
        if self.current_health <= 0:
            return False
        else:
            return True
    
    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

if __name__ == "__main__":
     # If you run this file from the terminal
     # this block is executed.
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())