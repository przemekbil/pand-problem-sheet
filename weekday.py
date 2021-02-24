# A simple program program that outputs whether or not today is a weekday
# Since this homework was on a week where we learned about lists and dictionaries
# I'm going to solve it using lists and dictionaries. Lots of them ;)

# PAND Weekly Task 5
# Author: Przemyslaw Bil

from datetime import date

# Create empty month list
month=[]

# Fill month with numbers from 1 to 31 (days of a month)
for day in range(31):
    month.append(day + 1)

# Define months jan-dec as a slice of month[] list
jan = month[:31]
feb = month[:28]
mar = month[:31]
apr = month[:30]
may = month[:31]
jun = month[:30]
jul = month[:31]
aug = month[:31]
sep = month[:30]
oct = month[:31]
nov = month[:30]
dec = month[:31]

# Define a year dictionary with a key being month number and a value being 
# a list with predefined month days
year2021 = {1:jan, 2:feb, 3:mar, 4:apr, 5:may, 6:jun, 7:jul, 8:aug, 9:sep, 10:oct, 11:nov, 12:dec}

# Define a daysOfWeek dictonary, with a key from 0-6 being the the day of the week
# And the Value being another dictionary with the Keys for Day, isWeekend and CountDown
daysOfWeek = {
    0:{"Day": "Monday", "isWeekend":False, "countDown": "5 days"}, 
    1:{"Day": "Tuesday", "isWeekend":False, "countDown": "4 days"}, 
    2:{"Day": "Wednesday", "isWeekend":False, "countDown": "3 days"}, 
    3:{"Day": "Thursday", "isWeekend":False, "countDown": "2 days"}, 
    4:{"Day": "Friday", "isWeekend":False, "countDown": "1 day"}, 
    5:{"Day": "Saturday", "isWeekend":True}, 
    6:{"Day": "Sunday", "isWeekend":True}
    }


# Check what date is today and store it as a dictionary with 2 keys: Day and Month
today =  {
    "day": date.today().day, 
    "month": date.today().month
    }

# Define a variable DayOfYear. I'll be using it to count which day of the year is today
dayOfYear = 0

# Loop over the year2021 dictionary until the last month
for month_it in range(today["month"]-1):
    # loop over the days in the iterated month. Have to add 1 to month iterator month_it as the for loop will iterate from 0 until current month-2
    # and we want to iterate throug months from 1 until last (current -1)
    for day_it in year2021[month_it + 1]:
        # increase dayOfYear by 1 in each iteration of the inner loop to sum the days that already passed in the year
        # Could have achieve the same effect by using only month loop and increasing dayOfYear by len(year2021[month_it + 1])
        dayOfYear = dayOfYear + 1
        
# We didn't iterate through current month, so have to add current day of month to dayOfYear to calculate which day of year is it
dayOfYear = dayOfYear + today["day"]

# Calculating day of week using Modulo 7 operator. dayOfWeek variable can have only values from 0-6, Monday being 0 and Sunday 6
# For this to be correct, I have to substract 4 from the dayOfYear, as the first Monday of this Year was on day 4 (4th of January)
dayOfWeek = (dayOfYear-4) % 7

# Checking if today is weekend, by calling 'daysOfWeek' dictionary Key 'dayOfWeek'. The returning Value for that Key will be another 
# dictionary and we'll check the value of its 'isWeekend' Key (which is false for Weekdays and True for the weeken)
if(daysOfWeek[dayOfWeek]['isWeekend']):
    # prints the 'Weekend' message
    print("Today is " + daysOfWeek[dayOfWeek]['Day'] + " so it's a Weekend! " )
else:
    # prints the 'Weekday' message
    print("Today is " + daysOfWeek[dayOfWeek]['Day'] + ", unfortunately it's a weekday. " + daysOfWeek[dayOfWeek]['countDown']  + " until weekend")


# Now, if I didn't have to use lists adn dictionaries, this is what I would do using imported datetime module:
'''
if(date.today().isoweekday()<6):
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")
'''