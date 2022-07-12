# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------
primary_orders = 0
secondary_orders = 0


# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------
print("welcome to Ransom's top tier food shop.")
primary_orders=int (input("is there anything that you want from this fine place?\n 1-for $6sushi   2-for $9cabbage  3-for $5onions\n"))
sushi = 1
cabbage = 2
onions = 3
total = 0.00
if primary_orders == 1:
	print("sushi = $6")
	total = total + 6.00
elif primary_orders == 2:
	print("cabbage = $9")
	total = total + 9.00
elif primary_orders == 3:
	print("onions = $5")
	total = total + 5.00
else:
	print("ok so nothing >:(")
	total = total + 0.00

secondary_orders=int(input("what bev you picking?\n 4-for $10sprite   5-for $11diet sprite  6-for $20chakara in a can\n"))
sprite = 4
diet_sprite = 5
chakara_in_a_can = 6
if secondary_orders == 4:
	print("sprite = $10")
	total = total + 10.00
elif secondary_orders == 5:
	print("diet_sprite = $11")
	total = total + 11.00
elif secondary_orders == 6:
	print("chakara in a can = $20")
	total = total + 20.00
else:
	print("ok so nothing >:(")
	total = total + 0.00
# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------












# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!
# -------------------------------------------- 
tip = int (input("type the amount you want to tip ransom:\n"))
if tip < 0:
	print("this is not acceptable :(")
	tip = 0
print("your oreder's normal cost is:")
print(total)
print("taxes:")
total2 = total * 0.08875
print(total2)
print("your tip will be:")
print(tip)
print("you'll pay:")
total3 = total + total2 + tip 
print(total3)








# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 
print("this is your receipt:")
if primary_orders == 1:
	print("sushi = $6")
	
elif primary_orders == 2:
	print("cabbage = $9")
	
	
elif primary_orders == 3:
	print("onions = $5")
	

	
	

print("drink:")
if secondary_orders == 4:
	print("sprite = $10")
	
elif secondary_orders == 5:
	print("diet_sprite = $11")
	
elif secondary_orders == 6:
	print("chakara in a can = $20")
print(total)
print("taxes:")
print(total2)
print("tip")
print(tip)
print("how much you payed:")
print(total3)



# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
