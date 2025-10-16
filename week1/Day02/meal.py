# Implement a program that prompts the user for a time and 
# outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. 
# Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. 
# For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
# Structure your program per the below, wherein convert is a function (that can be called by main) 
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

# function to convert time from "HH:MM" format to float hours
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

# main function to prompt user and check meal times
def main():
    time_str = input("Enter time in 24-hour format (e.g., 7:30): ").strip()
    try:
        time_float = convert(time_str)
    except Exception:
        print("Invalid time format.")
        return

    # Meal time checks (inclusive ranges)
    if 7.0 <= time_float <= 8.0:
        print("Time for Breakfast")
    elif 12.0 <= time_float <= 13.0:
        print("Lunch time")
    elif 18.0 <= time_float <= 19.0:
        print("Dinner time")

main()
