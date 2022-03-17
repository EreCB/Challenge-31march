## Activity Python 2: Writing a function that sums elements in an array

# The array's length will be determined by the user

import random

# Array sum function
def array_sum(array):
    sum = 0
    for i in array:
        sum = sum + i

    return sum


print('================================================================================')
print('================================================================================')
print('                       Welcome to the array sum function!\n')
print('In this game we will make the sum of all the elements contained in an array.')
print("You will determine the array's lenght.")
print('It cannot contain more than 1,000 elements.')
print('Are you ready? Here we go!')


# Creating an empty array and requesting the array's lenght to the user
array = []
length = int(input('\nWrite an integer number between 2 and 1000: '))


# Filling the array with a serie of randon numbers
for i in range(length):
    array.append(random.randint(1,1000))

# Printing the array
print('\nThis is your array:\n')
print(array)

# Calling the array sum function
sum_result = array_sum(array)

# Printing the results
print('\nYou created an array with a lenght of ', str(length), 'elements.')
print('The sum of all the elements in the array is equal to ', str(sum_result), '.')
print('\nThanks for participating in this game. See you soon!')
print('================================================================================')
print('================================================================================')
