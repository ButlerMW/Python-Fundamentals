# 1) Task: proint "Hello World"
print("Hello World")

# 2) Print "Hello Noelle!" with the name in a variable
name = "Michael"
print("Hello", name) # with a comma
print("Hello " + name) # with a +

# 3) print "Hello 42!" with the number in a variable
num = 88
print("Hello", num) # with a comma
print("Hello " + f"{num}") # with a +  **This on should give us an error //Must be a string and not and int
print(f"Hello {num}") # or you can do it this way

# 4) print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "breakfast burrito"
fave_food2 = "sushi"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with f string 


# Create a new Python file called hello_world.py
# Write the code to print a literal string saying "Hello World" (#1)
# Run the file
# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a comma in the print function (#2a)
# Run the file
# Store your name in a variable, and then use it to print the string “Hello {{your name}}!” using a + in the print function (#2b)
# Run the file
# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a comma in the print function (#3a)
# Run the file
# Store your favorite number in a variable, and then use it to print the string “Hello {{num}}!” using a + in the print function (#3b)
# Run the file
# NINJA BONUS: Figure out how to resolve the error from above, without changing the + sign to a comma
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with the format method (#4a)
# Run the file
# Store 2 of your favorite foods in variables, and then use them to print the string “I love to eat {{food_one}} and {{food_two}}.” with f-strings (#4b)
# Run the file
# NINJA BONUS: Spend a few minutes playing around with other string methods to see what’s out there!