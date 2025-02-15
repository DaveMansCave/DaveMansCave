import datetime
def age_calculator():
    try:
        year = int(input("What year were you born?"":"))
        month = int(input("What month were you born? No leading zeros"":"))
        day = int(input("What's the day you were born? Don't include any leading zeros."":"))
        todays_date = datetime.date.today()
        birthday = datetime.date(year, month, day)
        todays_year = todays_date.year
        todays_month = todays_date.month
        todays_day = todays_date.day
        time_difference = todays_date - birthday
        time_difference_years = time_difference.days // 365
        print("You are" + " " + str(time_difference_years) + " " + "years old")
    except ValueError:
        print("Only numbers are accepted!!!")
age_calculator()
    


