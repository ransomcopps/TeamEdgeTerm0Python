is_alive = True
#Locations = []
cloths_on = False

class Player:
    def __init__(self,name):
        self.name = name
        self.water_meter = 5
        self.is_alive = True

class Item:
    def __init__(self,name,use_description):
        self.name = name
        self.use_description = use_description

name = "water bottle"
use_description = "you increased your water meter by 10. :D"
water_bottle = Item(name, use_description) 
      
name = "cloths"
use_description = "you can finally go outside without getting arrested. type exit house from the hallway to leave. :D"
cloths = Item(name, use_description)

name = "gun"
use_description = "this is america, so guns are meta for protection. :D"
gun = Item(name, use_description)

name = input("hello there, what is your name?\n")
player = Player(name)

print(f"Hello there, {player.name}. You woke up in one faithful morning, and looked at your phone cuz you was bored. Looking at instagram, you looked at a instagram baddy, and her name is Lover. Lover DMed you and said she wants you to link up with her in her crib. You, being down bad decides you want to go slide without any questions involved, so you got up and is about to get ready, cuz you are literally naked right now.\n type move ____ to go somewhere. \n you can only access the hallway, but from there you can acess the bedroom, bathroom, living_room, kitchen, bedroom2. \n use ___ is needed to use your items. like WATERBOTTLE!")
print("items: waterbottle, gun, clothes")

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
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name
# answer = input("Where to move?")
# splitting = aswer.split(" ")
# if splitting[0] == "move":
#     if splitting[1] == "kitchen":
#         kitchen.description()


name = "Kitchen"
description = f"The kitchen is where people go to eat.{player.name} probably wants to grab something to eat before he leaves."
items =["peanut butter", "jelly"]
kitchen = Rooms(name, description,items)


name = "living_room"
description = "you are in thr living room, and you see your nice cute dog... even though turtles are better."
items =["cash", "pet dog"]
living_room = Rooms(name, description, items)

name = "hallway"
description = "this is a hallway... duh.btw you can go to bedroom1, bedroom2, kitchen, bathroom, and living room. if you go to any of those, you can only go to hallway."
items = [""]
hallway = Rooms(name, description, items)

name = "bedroom"
description = "this is your bedroom"
items = ["comb", "cloths"]
bedroom = Rooms(name, description, items)

name = "bedroom2"
description = "this is your other bedroom, maybe lover would sleep here one day"
items = ["gun", "water bottle"]
bedroom2 = Rooms(name, description, items)

name = "bathroom"
description = f"this is where you sh*t and p*ss in... oh and shower, i forgot cuz {player.name}'s smelly a** doesn't take any. sorry for my language."
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


while player.water_meter > 0:
    #input(answer)
    answer = input("What you want to do?")
    splitting = answer.split(" ")
    if splitting[0] == "move":
        player.water_meter=player.water_meter-1
        for room in current_room.options:
            if splitting[1] == room.name:
                print(room.description)
                current_room = room
    elif splitting[0] == "use":
        if splitting[1] == "waterbottle":
            player.water_meter += 10
            print(water_bottle.use_description)

        elif splitting[1] == "clothes":
            print(cloths.use_description)
            cloths_on = True

        
        elif splitting[1] == "gun":
            print(gun.use_description)


    elif answer == "kill_dog":
        print("You have attempted to kill the dog but dog is too strong!:D")
    else:
        print("i don't know that command")

    if player.water_meter <= 0:
        print("you died from dehydration")
    
    if cloths_on == True:
        if splitting[0] == "exit":
            if splitting[1] == "house":
                print("you have completed the demon. congrats")
                exit()
        
   
    
 




#make elif statements for items
    
    