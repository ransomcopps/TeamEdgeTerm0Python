is_alive = True
Locations = []

class Player:
    def __init__(self,name):
        self.name = name
        self.water_meter = 5
        self.is_alive = True


name = input("hello there, what is your name?\n")
player = Player(name)

print(f"Hello there, {player.name}. You woke up in one faithful morning, and looked at your phone cuz you was bored. Looking at instagram, you looked at a instagram baddy, and her name is Lover. Lover DMed you and said she wants you to link up with her in her crib. You, being down bad decides you want to go slide without any questions involved, so you got up and is about to get ready, cuz you are literally naked right now.\n type move ____ to go somewhere. ")

class Locations:
    def __init__(self,name,items,rooms):
        self.name = name
        self.items = items
        self.rooms = rooms




#def water_health():
    #water_meter = 5
#while water_meter > 0 and is_alive:
class Rooms:
    def __init__(self, name=None, description=None, items=None, options=None):
        self.name = name
        self.description = description
        self.items = items
        self.options = options

# answer = input("Where to move?")
# splitting = aswer.split(" ")
# if splitting[0] == "move":
#     if splitting[1] == "kitchen":
#         kitchen.description()


name = "Kitchen"
description = f"The kitchen is where people go to eat.{player} probably wants to grab something to eat before he leaves."
items =["peanut butter", "jelly"]
kitchen = Rooms(name, description,items)


name = "living room"
description = "you are in thr living room, and you see your nice cute dog... even though turtles are better."
items =["cash", "pet dog"]
living_room = Rooms(name, description, items)

name = "hallway"
description = "this is a hallway... duh."
items = [""]
hallway = Rooms(name, description, items)

name1 = "bedroom1"
description = "this is your bedroom"
items = ["comb", "cloths"]
bedroom = Rooms(name, description, items)

name = "bedroom2"
description = "this is your other bedroom, maybe lover would sleep here one day"
items = ["gun", "water bottle"]
bedroom2 = Rooms(name, description, items)

name = "bathroom"
description = f"this is where you sh*t and p*ss in... oh and shower, i forgot cuz {player}'s smelly a** doesn't take any. sorry for my language."
items = ["note"]
bathroom = Rooms(name, description, items) 

hallway.options = [kitchen , bedroom , bedroom2 , bathroom , living_room]
living_room.options = [kitchen , hallway]
bathroom.options = [hallway]
bedroom2.options = [hallway]
bedroom.options = [hallway]
kitchen.options = [living_room , hallway]




#you_house = Locations(f"{player}'s house", ["gun", "money", "comb", "cloths", "water bottle", "note", "peanut butter", "jelly", "cash"], [bedroom1,bedroom2,bathroom,living room,kitchen])
#shop = Locations("gun shop", ["bullets water", "bottle"],[buy area] )
#other_dude_house = Locations("neighbor's house", ["demon slaying sword", "cup of water", "money"], [lving room, bathroom, Bedroom, secret area, trap room])
#trap_house = Locations("gang house", ["water bottle"],[entrance area, living room, kitchen, Bedroom, Bathroom] )
#karen_house = Locations("karen's house", ["gate key, water bottle, money"], [living room,twitter room, locked room, karens room,bathroom] )
#park = Locations("the mid park", ["map, gallon of water"], [playground, swings, benches])
#crush_house = Locations("crush's house", [""],[])
#win_area = Locations("Lover's house", [""],[])

current_room = bedroom
answer = input("What you want to do?")
splitting = answer.split(" ")
if splitting[0] == "move":
    if splitting[1] == "hallway":
        for move in current_room.options:
        
            
            

            print(hallway.description)
    
else:
    print("i don't know that command")

while player.water_meter > 0:
    pass
        




    