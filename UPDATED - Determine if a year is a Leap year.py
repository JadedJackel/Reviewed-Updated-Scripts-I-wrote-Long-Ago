'''================================================================='''
#                  <====|--  Jaded $ Jackel  --|====>                 #
'''=================================================================>>>
Date:       08-13-25                                                  
Project:    Updating some Old-OLd-OLD, sripts I wrote long ago  ;)     
Notes:      The original script is listed below the updated version
            Green comments are original notes, single line are current             
<<<================================================================='''
#--------|--------|----------------|--------------------------------!64


# Written*  02.25.2021
# Purpose*  Determine if a year is a leap year. AND, as an extra credit bonus :) if so, display Feburary has 29 days 




''' Starting the first index with 0 because the user won't likely know to use 0 as the index for January '''
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Going to create a dictionary as well, works perfectly for a month day cformat
months_and_days = {
"January" : 31, "February" : 28, "March" : 31, "April" : 30, "May" : 31, "June" : 30, 
"July" : 31, "August" : 31, "September" : 30, "October" : 31, "November" : 30, "December" : 31
}




def main():
    users_year = get_year()
    users_month = get_month()
    answer_leap = is_leap(users_year)
    days_in_month(users_year, users_month)




def get_year():
    year = int(input("Please enter a year: "))
    return year




def get_month():
    month = (input("Please enter a month: "))
    if month == 'January' or ' February' or 'March' or 'April' or 'May' or 'june' or 'July' or 'August' or 'September' or 'October' or 'November' or 'December':
        return month.capitalize()
    elif month == 'Jan' or 'Feb' or 'Mar' or 'Apr' or 'Jun' or 'Jul' or 'Aug' or 'Sep' or 'Oct' or 'Nov' or 'Dec':
        return abr_month.capitalize()
    elif month == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        month = int(month)
        return int_month
    else:
        print("That is not a valid month")
        get_month()




''' Returns True for leap years, and false for non-leap years '''
# I am going to edit this a bit, and have it return a sting that's a little more friendly

def is_leap(year):
    # Leap years that are divisable by 100 are NOT a leap year, EXCEPT!- when they are also divisable by 400
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("That year qualifies as a leap year.")
        return year
    else:
        print("That year does not qualifiy as a leap year.")
        main()




''' Returns the number of days in that month in that year '''
def days_in_month(year, month):
    if month == 'January' or ' February' or 'March' or 'April' or 'May' or 'june' or 'July' or 'August' or 'September' or 'October' or 'November' or 'December':
        print(f"{year}{month}")
    elif month == 'Jan' or 'Feb' or 'Mar' or 'Apr' or 'Jun' or 'Jul' or 'Aug' or 'Sep' or 'Oct' or 'Nov' or 'Dec':
        print(f"{year}{month}")
    elif month < 1 or month > 12:
        print("Invalid Month")
        get_month()
    elif month == (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        print(f"{year}{month}")
    elif is_leap(year) and month == 2:
        print(f"This year...{year}and{month}")


main()

    
        






'''================================|================================'''
#                   Original - is it a leap year - script
'''================================|================================>>>

"""
Author      Darren Gibson
Date        02.25.2021
Category    Small Programs
Purpose     Is it a leap year
"""


# We are beginning our variable with a 0 because the first value
# will be a 0 because we really want it to start at the 1 index
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """ Return True for leap years, and false for non-leap years """

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """ Returns the number of days in that month in that year """

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):

        return 29

    return month_days[month]

# There's probably a gazillion ways we could do this, but I wanted to see this way in action 
# print(is_leap(2019), days_in_month(is_leap(2019),2))
# However, I am trying somethig  different now

<<<================================================================='''





# As a side project, I created this bullshit while I was working on this
'''
def get_year():
    users_year = int(input("please enter a year: "))
    results = is_leap(users_year)
    if results == 1:
        print("That year qualifies as a leap yaer")
    elif results == 2:
        print("That year does not qualify as a leap year, try again")
        get_year()

def is_leap(year):
    # Leap years that are divisable by 100 are NOT a leap year, EXCEPT!- when they are also divisable by 400
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 2

get_year()
'''















































