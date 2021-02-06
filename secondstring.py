# This program that takes asks a user to input a string 
# and outputs every second letter in reverse order
# This is a solution for Weekly Task 03

#Author: Przemyslaw Bil

# define the same sentence as in problem statement. Used for testing
# inputString = 'The quick brown fox jumps over the lazy dog.']

# Read user input
inputString = input('Please enter a sentence: ')

# Define empty output string. characters will be added to it in the loop below
outputString=''

# loop counter 'i' for finding odd positions in the reversed string (last letter, thrirds last etc..)
i=1

# loop through reversed input string
for c in reversed(inputString):
    if i%2==1: outputString = outputString + c #add every other letter starting from position 1
    i=i+1                                      #increment loop counter

# Output the result string
print(outputString)