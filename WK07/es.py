# Program to count specified letter in a text file. If no letter is specified, 'e's will be counted
# This is Solution to the Week 7 task

# Author: Przemyslaw Bil

# import sys package to read the command line arguments
import sys

# simple function to check the Characters: returns 1 if the character is e (or any other specified) and 0 if it's different
def checkChar(c, charToFind):
    if c==charToFind:
        return 1
    else:
        return 0


def openfile(fileName, toFind='e'):


    # Using try-except block to execute opening and reading the specified file
    # This will ensure, that program will execute even if specified file doesn't exist 
    try:
        # my file had utf8 encoding and I had to add encoding="utf8" parameter for this line to work:
        with open(fileName, "rt", encoding="utf8") as textFile:
            # Read the content of the file to the String variable
            txtFileContent = textFile.read()
            # initilize the count variable to count the ocurences of selected character
            count = 0

        # loop through the content of the file character by character
        for ch in txtFileContent:
            # increment counter by 1 if the character is 'e' (or other specified)
            count = count + checkChar(ch, toFind)
        
        # print the result
        print("\nCharacter '{}' is used {} times in the '{}' file\n".format(toFind, count, fileName))

    # Catch the exception FileNotFoundError in cases where specified filename doesn't exist
    except FileNotFoundError:
        print("\n\tFile '{}' not found in the current directory\n".format(fileName))


# main program starts here
# Check number of command line arguments
if len(sys.argv)==1:
    # if no arguments were specified in the command line, print error mesage:
    print("\n\tFile name not specified\n")
elif len(sys.argv)==2:
    # if one arguments was specified in the command line, try to use it as a text file name: 
    openfile(sys.argv[1])
elif len(sys.argv)>2: 
    # if more than one arguments was specified in the command line, use first as a text file name, second as a character to count it's occurences:
    # check if the second argument is a single character:
    if len(sys.argv[2])==1:
        openfile(sys.argv[1], sys.argv[2])
    else:
        # if it was not a single character, print error
        print("\n\t'{}' is not a valid character argument. Please use single character only\n".format(sys.argv[2]))


