# This program that takes asks a user to input a string 
# and outputs every second letter in reverse order
# This is a solution for Weekly Task 03

#Author: Przemyslaw Bil

# define the same sentence as in problem statement. Used for testing
# inputString = 'The quick brown fox jumps over the lazy dog.']

# Read user input
inputString = input('Please enter a sentence: ')

# the slice statement [::-2] means start at the end of the string and end at position 0, move with the step -2, negative one, which two steps backwards
print(inputString[::-2])
