# ######## Basic 1 ########

# ## 1) Basic - Print all integers from 0 to 150.

# for x in range(0, 151):
#     print(x)

# ## 2) Multiples of Five - Print all the multiples of 5 from 5 to 1,000

# for x in range(5, 1005, 5):
#     print(x)

# ## 3) Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print 
# ##    "Coding" instead. If divisible by 10, print "Coding Dojo".

# for x in range(1, 101):
#     if x % 5 == 0:
#         print("Coding")
#     else: 
#         print(x)

# ## 4) Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

# i = 0
# for x in range(0, 500000):
#     if x % 2 == 1:
#         i += x
# print(i)

# ## 5) Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

# for x in range(2018, 0, -4):
#     print(x)

# ## 6) Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
# ##    going through highNum, print only the integers that are a multiple of mult. For example, if 
# ##    lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

# lowNum = 2
# highNum = 9
# mult = 3
# for x in range(lowNum, highNum):
#     if x % mult == 0:
#         print(x)


######## Basic 2 ########

# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#       Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(biggie_size_array):
    for i in range(0, len(biggie_size_array)):
        if biggie_size_array[i] > 0:
            biggie_size_array[i] = "big"
    print(biggie_size_array)
    return biggie_size_array
biggie_size([-1, 3, 5, -5])

# 2) Count Positives - Given a list of numbers, create a function to replace the last value with the number of 
#   positive values. (Note that zero is not considered to be a positive number).
#       Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#       Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(count_positives_array):
    count = 0
    for i in range(0, len(count_positives_array)):
        if i > 0:
            count += 1
    count_positives_array[(len(count_positives_array)-1)] = count
    print(count_positives_array)
    return count_positives_array
count_positives([-1,1,1,1])     # [-1,1,1,3]
count_positives([-1,6,-4,-2,-7,-2])     # [1,6,-4,-2,-7,2]

# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#       Example: sum_total([1,2,3,4]) should return 10
#       Example: sum_total([6,3,-2]) should return 7

def sum_total(sum_total_array):
    array_sum = 0
    for i in range(len(sum_total_array)):
        array_sum += sum_total_array[i]
    print(array_sum)
sum_total([1,2,3,4])
sum_total([6,3,-2])



# 4) Average - Create a function that takes a list and returns the average of all the values.
#       Example: average([1,2,3,4]) should return 2.5

def average(average_array):
    average_sum = 0
    for i in range(len(average_array)):
        average_sum += average_array[i]
    average = average_sum / len(average_array)
    print(average)
average([1,2,3,4])



# 5) Length - Create a function that takes a list and returns the length of the list.
#       Example: length([37,2,1,-9]) should return 4
#       Example: length([]) should return 0

def length(length_array):
    length_count = 0
    for i in range(len(length_array)):
        length_count += 1
    print(length_count)
length([37, 2, 1, -9])
length([])



# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value 
# in the list. If the list is empty, have the function return False.
#       Example: minimum([37,2,1,-9]) should return -9
#       Example: minimum([]) should return False

def minimum(minimum_array):
    minimum = 0
    for i in range(len(minimum_array)):
        if minimum_array[i] < minimum:
            minimum = minimum_array[i]
    if minimum_array == []:
        print("False")
        return False
    print(minimum)
minimum([37,2,1,-9])
minimum([])


# 7) Maximum - Create a function that takes a list and returns the maximum value in the array. 
#   If the list is empty, have the function return False.
#       Example: maximum([37,2,1,-9]) should return 37
#       Example: maximum([]) should return False

def maximum(maximum_array):
    maximum = 0
    for i in range(len(maximum_array)):
        if maximum_array[i] > maximum:
            maximum = maximum_array[i]
    if maximum_array == []:
        print("False")
        return False
    print(maximum)
maximum([37,2,1,-9])
maximum([])


# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has 
#   the sumTotal, average, minimum, maximum and length of the list.
#       Example: ultimate_analysis([37,2,1,-9]) should return 
#       {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(ultimate_analysis_array):
    result = {}
    sumTotal = 0
    minimun = 0
    maximum = 0
    for i in range(len(ultimate_analysis_array)):
        sumTotal += ultimate_analysis_array[i]
        if maximum < ultimate_analysis_array[i]:
            maximum = ultimate_analysis_array[i]
        elif minimun > ultimate_analysis_array[i]:
            minimun = ultimate_analysis_array[i]
    result['sumTotal'] = sumTotal 
    result['average'] = sumTotal/len(ultimate_analysis_array)
    result['minimum'] = minimun
    result['length'] = len(ultimate_analysis_array)
    print(result)
    return result
ultimate_analysis([37,2,1,-9])

# 9) Reverse List - Create a function that takes a list and return that list with values reversed. 
#   Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#       Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(reverse_list_array):
    for i in range(len(reverse_list_array)//2):
        temp = reverse_list_array[i]
        reverse_list_array[i] = reverse_list_array[len(reverse_list_array) - 1 - i]
        reverse_list_array[len(reverse_list_array) - 1 - i] = temp
    print(reverse_list_array)
    return reverse_list_array
reverse_list([37,2,1,-9])