######## Functions 1 ##########
## For each of the following code snippets, first predict the output (what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!

# #1
# def a():
#     return 5
# print(a())
# # 5

# #2
# def a():
#     return 5
# print(a()+a())
# # 10

# #3
# def a():
#     return 5
#     return 10
# print(a())
# # 5

# #4
# def a():
#     return 5
#     print(10)
# print(a())
# # 5

# #5
# def a():
#     print(5)
# x = a()
# print(x)
# # 5, None

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
# # 3, 5
# # Traceback (most recent call last):
# #   File "Functions.py", line 40, in <module>
# #     print(a(1,2) + a(2,3))
# # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

# #7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))
# # 25

# #8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())
# # 100, 10

# #9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))
# # 7, 14, 21

# #10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))
# # 8

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)
# # 500, 500, 300, 500

# #12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)
# # 500, 500, 300, 500

# #13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)
# # 500, 500, 300, 500

# #14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()
# # 1, 3, 2

# #15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)
# # 1, 2, 5, 10


########## Functions 2 ##########

# # 1) Countdown - Create a function that accepts a number as an input. Return a new list that 
# #   counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# #       Example: countdown(5) should return [5,4,3,2,1,0]

# def countdown(countdownInt):
#     for i in range(countdownInt, -1, -1):
#         print(i)
# countdown(5)



# # 2) Print and Return - Create a function that will receive a list with two numbers. Print the 
# #   first value and return the second.
# #       Example: print_and_return([1,2]) should print 1 and return 2

# def print_and_return(printReturnArray):
#     print(printReturnArray[0])
#     return printReturnArray[1]
# print_and_return([1,2])



# # 3) First Plus Length - Create a function that accepts a list and returns the sum of the first 
# #   value in the list plus the list's length.
# #       Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def first_plus_length(a):
#     x = a[0] + a[(len(a) - 1)]
#     print(x)
#     return x
# first_plus_length([1,2,3,4,5])



# # 4) Values Greater than Second - Write a function that accepts a list and creates a new list 
# #   containing only the values from the original list that are greater than its 2nd value. Print 
# #   how many values this is and then return the new list. If the list has less than 2 elements, have 
# #   the function return False
# #       Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# #       Example: values_greater_than_second([3]) should return False

# def values_greater_than_second(a):
#     b = []
#     if len(a) > 1:
#         for i in range(0, len(a)):
#             if a[i] >= a[2]:
#                 b.append(a[i])
#     else:
#         return False
#     print(len(b))
#     print(b)
# values_greater_than_second([5,3,3,2,1,4])
# values_greater_than_second([3])



# # 5) This Length, That Value - Write a function that accepts two integers as parameters: size and 
# #   value. The function should create and return a list whose length is equal to the given size, and 
# #   whose values are all the given value.
# #       Example: length_and_value(4,7) should return [7,7,7,7]
# #       Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# def length_and_value(size,value):
#     a = []
#     for i in range(size):
#         a.append(value)
#     return a
# print(length_and_value(4,7))
# print(length_and_value(6,2))

########## Intermediate ##########

# import random
# def randInt(min=0 , max=100 ):
#     num = random.random() * max + min
#     return round(num)
# print(randInt())                   # should print a random integer between 0 and 100
# print(randInt(max=50))             # should print a random integer between 0 and 50
# print(randInt(min=50))             # should print a random integer between 50 and 100
# print(randInt(min=500, max= -5))   # BONUS: account for any edge cases (eg. min > max, max < 0)print(randInt(min=50, max=500))   # should pring a random integer between 50 and 500



########## Intermediate II ##########

# # 1) Update Values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ]
# # students = [
# #     {'first_name': 'Michael', 'last_name' : 'Jordan'},
# #     {'first_name': 'John', 'last_name' : 'Rosales'}
# # ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# ## 1) Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]]

# students[0]['last_name'] = 'Bryant'
# print(students[0])

# ## 2) Change the last_name of the first student from 'Jordan' to 'Bryant'

# x[1][0] = 15
# print(x)

# ## 3) In the sports_directory, change 'Messi' to 'Andres'

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory)

# ## 4) Chand the value 20 in z to 30

# z[0]['y'] = 30
# print(z)

# # 2) Iterate Through a List of Dictionaries
#     # Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops throught each dictionary in the list and prints each key and the associated value.

# students = [
#     {'first_name' : 'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'},
#     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#     {'first_name' : 'KB', 'last_name' : 'Tonel'},
# ]
# def iterateDictionary(students):
#     for i in range(len(students)):
#         print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")
# iterateDictionary(students)
#     # should output: (it's okay if each key-value pair ends up on 2 separate lines;)
#     # bonus to get them to appear exactly as below!)
# # first_name - Michael, last_name - Jordan
# # first_name - John, last_name - Rosales
# # first_name - Mark, last_name - Guillen
# # first_name - KB, last_name - Tonel


# 3) Get values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key dictionary. 
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark 
# KB

# def iterateDictionary2(key_name, some_list):
#     for i in range(len(some_list)):
#         print(some_list[i][key_name])
# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)


# 4) Iterate Through a Dictionary with List Values
    # Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key aling with the size of its list, and then prints 
    # the associated values within each key's list.
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    # output:
        # 7 LOCATIONS
        # San Jose
        # Seattle
        # Dallas
        # Chicago
        # Tulsa
        # DC
        # Burbank

        # 8 INSTRUCTORS
        # Michael
        # Amy
        # Eduardo
        # Josh
        # Graham
        # Patrick
        # Minh
        # Devon
    print(f"{len(dojo['locations'])} LOCATIONS")
    for i in range(len(dojo['locations'])):
        print(dojo['locations'][i])
    
    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
    
printInfo(dojo)