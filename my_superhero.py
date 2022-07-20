import random


class Superhuman:
    def __init__(self, name,side, super_power, moves, goal, hp):
        self.name = name
        self.side = side 
        self.super_power = super_power
        self.moves = []
        self.goal = goal
        self.hp = hp

    def attacks(self, opponent):
        
        
        

superhuman1a = Superhuman("super glitter boy", "hero", "poors glitter out of his hand", ["glitter smack","glitter smash","glitter blinding","glitter smash"], "to make the city sparkle",250)
superhuman1b = Superhuman("the janitor","villain","cleans things quickly", ["brinkeling broom", "moodiness mop", "sadness sanitizer", "bar of death"], "to see the city bland and clean", 400)
superhuman2a = Superhuman("the good kid","hero", "can talk things out with anyone", ["look, we all got problems", "think about it","i can see where you are comming from","i can respect that, but...","is this really the person you want to be?"],"to create world peace with no violence", 200)
superhuman2b = Superhuman("the bad kid", "villian","can instigate and create any fight", ["nah, that's wild", "me personally...","woooow","you can't let that rock"], "to make the world hectic and cause war", 150)


print("welcome to the super human fight!")