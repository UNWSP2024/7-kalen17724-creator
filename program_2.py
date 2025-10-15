# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def display_greater_than(numbers, n):
    for number in numbers:
        if number > n:
            print(number)

# Ask user for input
user_input = input("Enter a list of numbers separated by commas: ")
number_list = [float(num.strip()) for num in user_input.split(',')]

n = float(input("Enter a number to compare: "))

# Call the function
display_greater_than(number_list, n)

    
