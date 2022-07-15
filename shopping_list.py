#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True

print("Welcome to Shopping List!")

welcome_message = "Hi! I'm your shopping assistant. Let me take your order. \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list
shopping_list = []


def prompt_user():

    reply = input("What do you want to add or remove?  >>  ")

    return reply

def check_answer(ans):
    #print(input(check_answer))

    input_list = ans.split(" ")
    #print(str (B))
    add_or_remove = input_list[0]
    food = input_list[1]
    if add_or_remove == "add":
        add_item(food)
    elif add_or_remove == "remove":
        remove_item(food)
    else:
        print("type add or remove. >:(")
        

        #print("i have added an item")




def add_item(food_item):
    shopping_list.append(food_item)
    


    

def remove_item(food_item):
    shopping_list.remove(food_item)


     
while active:

    check_answer(prompt_user()) #this makes the program continously prompt and check response while the boolean 'active' returns True
    print(shopping_list)