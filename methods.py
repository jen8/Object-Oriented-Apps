class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    def attack(self, other_guy):
        other_guy.health = other_guy.health - self.damage
        print ("{} attacks {}!".format(self.name, other_guy.name))
        print ("{} loses {}!".format(other_guy.name, self.damage))

    def __str__(self):
        return "{}: {}".format(self.name, self.health)



qazi = Fighter("Qazi")
you = Fighter("Matt")

print(qazi) # prints <__main__.Fighter object at 0X102142668>
print (you)

you.attack(qazi)
print(qazi) # prints 90, which is 100 - 10


class Boxer(Fighter): # Boxer inherits from Fighter Class
    def heal(self):
        self.health += 10 
    

boxer_qazi = Boxer("Boxer Qazi") # Boxer requires names bc it inherits from Fighter
print(boxer_qazi)  # since boxer inherits from fighter, has these attributes + __str
print(boxer_qazi.damage)
print(boxer_qazi.health)

boxer_qazi.heal()

print(boxer_qazi)
