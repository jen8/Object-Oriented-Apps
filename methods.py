class Competitor:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_competitor):
        other_competitor.health = other_competitor.health - self.damage
        print ("{} attacks {}!".format(self.name, other_competitor.name))
        print ("{} loses {}!".format(other_competitor.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)



Henry = Competitor("Henry")
you = Competitor("Linda")

print(Henry) # prints <__main__.Fighter object at 0X102142668>
print (you)

you.attack(Henry)
print(Henry) # prints 90, which is 100 - 10


class Kick_Boxer(Competitor): # Boxer inherits from Fighter Class
    def heal(self):
        self.health += 10 
    

kick_boxer_henry = Kick_Boxer("Kick_Boxer Henry") # Boxer requires names bc it inherits from Fighter
print(kick_boxer_henry)  # since boxer inherits from fighter, has these attributes + __str
print(kick_boxer_henry.damage)
print(kick_boxer_henry.health)

kick_boxer_henry.heal()

print(kick_boxer_henry)
