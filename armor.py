import random

class Armor:

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
      # Pick a random value between 0 and self.block
      random_value = random.randint(0,self.max_block)
      return random_value

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    defense = Armor("Debugging Shield", 50)
    print(defense.name)
    print(defense.block())