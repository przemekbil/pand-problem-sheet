# A simple program to calculate BMI based on user input
# Author Przemyslaw Bil

# Get user's weight in kilograms. Catch ValueError thrown when user input is not a number
while True:
    try:
        m=int(input("\nEnter your weight in kilograms: "))
        break
    except ValueError:
        print("\n\tThis is not a vlid number. Try Again.\n")

# Get user's heigh in centimetres . Catch ValueError thrown when user input is not a number
while True:
    try:
        h=int(input("Enter your height in cm: "))
        break
    except ValueError:
        print("\n\tThis is not a vlid number. Try Again.\n")

# recalculate user's height to metres 
h=h/100

# calculate BMI value
bmi=m/(h**2)

# create msg out string
bmiOut = "\nYour MBI is {:.2f}"

# add comment, underweight, normal, overweight or obese depending on the BMI value:
# underweight < 18.5 < normal < 25 < overweight < 30 < obese
if bmi < 18.5:
    bmiOut = bmiOut + ", underweight\n"
elif bmi < 25:
    bmiOut = bmiOut + ", normal\n"
elif bmi < 30:
    bmiOut = bmiOut + ", overweight\n"
else:
    bmiOut = bmiOut + ", obese\n"

#print the result
print(bmiOut.format(bmi))
