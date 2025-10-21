'''
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636, 
wherein the month in the latter might be any of the values in the list below:
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
Then output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; 
no need to validate whether a month has 28, 29, 30, or 31 days.
'''

#import datetime function to handle date formatting
import datetime

#define months list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#define numeric data function
def parse_numeric(date_str):
    try:
        parts = date_str.strip().split("/") #split based on /
        if len(parts) != 3:
            raise ValueError("Invalid format.  Expected mm/dd/yyyy")
        month, day, year = map(int,parts) #  apply the int() function to every element in the list parts
        return datetime.date(year, month, day) # returns date in iso format
    except Exception as e:
        raise ValueError ("Invalid numeric format")

#define string date function
def parse_named(date_str):
    try:
        if "," not in date_str: # checks for comma separator in input
            raise ValueError(" Invalid format.  Expected comma in Month D, YYYY")
        month_day, year = date_str.strip().rsplit(",",1) #splits the string to 2 from last comma into year and month+date
        month_day = month_day.strip().split() #splits the month+date into 2 
        if len(month_day) != 2:
            print("Invalid format.  Expected Month and Day")
        
        month_name, day = month_day
        if month_name not in months:
            raise ValueError("Invalid Month Name")
        day = int(day)
        year = int(year)
        month = months.index(month_name) + 1
        return datetime.date(year, month, day)
    except Exception as e:
        raise ValueError("Invalid Date format")

# define get main date function
def get_valid_date():
    while True:
        s = input("Date : ").strip()
        try:
            if "/" in s:
                date = parse_numeric(s)
            else:
                date = parse_named(s)
            return date
        except ValueError:
            print("Invalid Date.  Pls try again")

#define main
def main():
    date = get_valid_date()
    print(date.strftime("%Y-%m-%d"))

#call main
main()