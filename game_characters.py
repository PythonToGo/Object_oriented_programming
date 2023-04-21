class GameCharacter:
    # class of game characters
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp 
        self.power = power 

    def is_alive(self):
        # check the character is alive or not; method 
        return True if self.hp > 0 else False
    

    def get_attacked(self, damage):
        """
        if character is alive, -damage
        condition:    
            1. if character already dead, print the was already dead.
            2. if rest hp < damage, -> hp == 0.
        """
        if self.is_alive():     
            self.hp = self.hp - damage if self.hp >= damage else 0
        else: 
            print("{} is already dead.".format(self.name))

    def attack(self, other_character):
        # if character is alive, other character get attacked.
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        # return the result of characters
        return "The hp of {} is {}.".format(self.name, self.hp)

# creating instance                        
character_1 = GameCharacter("Left_knights", 210, 30)
character_2 = GameCharacter("Right_knights", 150, 55)

# processing game / instance attacks each other
character_1.attack(character_2)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)
character_2.attack(character_1)

# print the instance
print(character_1)
print(character_2)