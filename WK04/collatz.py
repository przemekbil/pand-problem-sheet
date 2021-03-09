# A simple program to demonstrate a Collatz conjecture
# PAND Weekly Task 4
# Author: Przemyslaw Bil

# Define a function that returns n+1 value of the Collatz sequence:
# 2*n if n is even
# 3n+1 if n is odd
def nPlus1(n):
    if n%2==0:        
        return n/2
    else:
        return n*3+1

# get input from user. Check if it is a positive integer.
while True:
    try:
        n = int(input("Please enter any positive integer: "))
        if n>0:
             break
        else:
            print("\n\tInput value has to be greater than 0\n")
    except ValueError:
        print("\n\tThis is not a vlid integer. Try Again.\n")

# step counter
step=0
# The main loop of the program.
# Calculates and prints next value in Collatz sequence until it reaches 1
while n!=1:
    n=nPlus1(n)
    print('{:n}'.format(n))
#   increase step by one in each iteration to count the steps    
    step=step+1

# Print number os steps needed to reach 1
print('{:n} steps to reach 1'.format(step)) 