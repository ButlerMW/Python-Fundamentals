########## Selection Sort ##########

def selection_sort(unsorted_array):
    for i in range(len(unsorted_array)):
        min_value = i
        for j in range(i+1, len(unsorted_array)):
            if unsorted_array[min_value] > unsorted_array[j]:
                min_value = j
        unsorted_array[i], unsorted_array[min_value] = unsorted_array[min_value], unsorted_array[i]
    print(unsorted_array)
selection_sort([3,7,1,0,6,2])


########## Insertion Sort ##########

def insertion_sort(unsorted_array):
    for i in range(1, len(unsorted_array)):
        temp = unsorted_array[i]
        j = i-1
        while j >=0 and temp < unsorted_array[j]:
            unsorted_array[j+1] = unsorted_array[j]
            j -= 1
        unsorted_array[j+1] = temp
    print(unsorted_array)
insertion_sort([3,7,1,0,6,2])

# ########## Underscore ##########

# class Underscore:
#     def map(self, iterable, callback):
#         # your code here
#     def find(self, iterable, callback):
#         # your code here
#     def filter(self, iterable, callback):
#         # your code here
#     def reject(self, iterable, callback):
#         # your code here
# # you just created a library with 4 methods!
# # let's create an instance of our class
# _ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1,2,3,4,5,6]), lambda x: x % 2 == 0
# # should return [2, 4, 6] after you finish implementing the code above
#################################################################################
###                I have absolutly no idea how to start this                 ###
#################################################################################
