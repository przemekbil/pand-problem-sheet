# Program to calculate a square root using Newton-Raphson algorythm
# Slighty overcomplicated exercise on use of functions in Python ;)

# Author: Przemyslaw Bil

# This function accept 2 parameters: number to be squared and optional precission
def sqrRoot(num, precision = 0.00001):

    # if precision is equal or smaller than 0, the 'while' loop below would run forever
    # to prevent that, setting precision to defualt value if passes argument <=0
    if (precision <=0):
        precision = 0.00001

    # print(precision) # for debugging only

    # initial value of difference variable, has to be larger than precision
    # to make sure the 'while' loop will run at least once. Setting up larger than any reasonable precission:
    dif = 100

    # first guesstimate
    est = num/2.

    # Below loop will run until difference between the entered number and squared estimate is smaller than precission
    while (dif>precision):
        # calculate the next value using Newton-Raphson method
        est=(est+num/est)/2.
        # calculate the absolute difference between the entered number and squared estimate
        dif = abs(num-est*est)

    #return the fist calculated value, where the difference between the entered number and squared estimate was smaller than precission     
    return est

# This function asks user for a positive number. 
# It will catch ValueError thrown when user input is not a number
# This function has optional argument interrupt, which allows to press 0 or Q to return no value
def askForNumber(msg1, interrupt=False):
    while True:
        try:
            usrInput = input(msg1)
            x = float(usrInput)
            # exit the 'while' loop using 'break' when positive number was entered
            if x>0:
                 break
            # Return NoneType if interrupt is allowed and 0 was selected
            elif(interrupt and x==0):                
                return
            else:
                # print error message if number smaller or equal to 0 was entered
                print("\n\tInput value has to be greater than 0\n")
        except ValueError:
                # Return NoneType if interrupt is allowed q key was selected
                if(interrupt and (usrInput=="Q" or usrInput=="q")):
                    return
                else:
                    # print error message if string was entered
                    print("\n\tThis is not a valid number. Please try Again.\n")
    return x

# Ask user for number to be squared and precision (optional, can be skipped by pressing 0)
number_input=askForNumber("Please enter any positive number: ")
precision_input =askForNumber("Please enter precision (press '0' or 'q' to use default precission): ", True)

# Check if calculation precission was selected
if(precision_input is None):
    # if it wasn't entered, call sqrRoot with one argument only
    result = sqrRoot(number_input)
else:
    # if ot was selected, call sqrRoot with both arguments
    result = sqrRoot(number_input, precision_input)

# print the result
print("\n\tThe square root of {} is approximately {:.4f}\n".format(number_input, result))