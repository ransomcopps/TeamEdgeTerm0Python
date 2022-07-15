# -------------------------------------------- 
x= 5
y= 10
	# You've just learned all about functions. 
	# Now take what you've learned to create your own

					# CALCULATOR!

	# We'll guide you through the first few steps,
	# then you'll have a chance to add your own features
	# that will make this your new go-to calculator!

  # -------------------------------------------- 

print("My Simple Calculator")

# -------------------------------------------- 

# Part 1: 

	# The first features of any simple calculator is that
	# it should be able to perform the basic math operations. 
	# Let's start by writing the functions we'll need to execute 
	# the following operations:

		# Addition
		# Subtraction

# -------------------------------------------- 

# Write a function called add_numbers that will take two numbers and return the sum.
def add_numbers(x,y):
	return x+y
sum = add_numbers(x,y)
print(sum)





# Write a function called sub_numbers that will take two numbers and return the difference.
def sub_numbers(x,y):
	return x-y
difference = sub_numbers(x,y)
print(difference)


# ------------
# Testing Code - Uncomment the code below to test your code!

#(add_numbers(5, 15), 20)
#(add_numbers(3, 18), 21)
#(add_numbers(12, 28), 40)

#(sub_numbers(18, 7), 11)
#(sub_numbers(11, 9), 2)


# -------------------------------------------- 

# Part 2: 

	# Now that you have addition and subtraction down, let's add the other operators we learned!

	# Finish off your basic calculator by writing the functions 
	# for the following operations:

		# Multiplication
		# Division 

# -------------------------------------------- 

# Write a function called multiply_numbers that will take two numbers and return the product.
def multiply_numbers(x,y):
	return x*y
product = multiply_numbers(x,y)
print(product)


# Write a function called divide_numbers that will take two numbers and return the quotient.
def divide_numbers(x,y):
	return x/y
quotient = divide_numbers(x,y)
print(quotient)





# ------------
# Testing Code - Uncomment the code below to test your code!

# check_answers(multiply_numbers(10, 3), 30); 
# check_answers(multiply_numbers(21, 7), 147);
# check_answers(multiply_numbers(4, 16), 64); 

# check_answers(divide_numbers(24, 100), `.24`);
# check_answers(divide_numbers(21, 7), `3`);
# check_answers(divide_numbers(15, 4), `3.75`);

# -------------------------------------------- 

# Part 3: 

	# Now that you have your basic functions in place, you need to get some user input.
	# What's a calculator for if no one is using it?

# Write a function that will prompt the user for the operation they want to call and the values they are inputting.

# -------------------------------------------- 
def calculator():
	number1 = int (input("which number do you want to use? \n"))
	number2 = int (input("which other number do you want to use? \n"))
	total = 0
	choice = input("use + to add, - to subtract, * to multiply, and / to divide.\n")
	if choice == "+":
		total = add_numbers(number1,number2)

		
	elif choice == "-":
		total = sub_numbers(number1,number2)

	elif choice == "*":
		total = multiply_numbers(number1,number2)

	elif choice == "/":
		total = divide_numbers(number1,number2)
	
	print(total)

calculator()










# -------------------------------------------- 

# Part 4: 

	# Now that you have all of the basic four operations completed, you get to add your own features!
	# What will you add to make this your go-to calculator? 

	# Stuck? : Think about what you count/calculate on a (almost) daily basis.
	# Can you write a function that will take in the data you need and do the calculation for you? 

	# (I know I calculate how many hours of sleep I get every day... ｡(*^▽^*)ゞ )

# -------------------------------------------- 

# Write a function or functions that will add some unique features to your calculator. 
# Don't forget to:
		# Give your function an name and parameters that are self explanatory and written in camelcase!
		# Use comments throughout your code
		# Test your code!
  
# -------------------------------------------- 





















# -------------------------------------------- 
# Ignore this section. This is just for checking your work

def check_answers(gen_answer, correct_answer):
    if gen_answer == correct_answer:
        print("Your code works!")
    else:
	    print(f"Try again, your code generated {gen_answer} but the correct answer is {correct_answer}")