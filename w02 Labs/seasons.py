# input month and day
month = input("Enter the name of the month: ").title()
day = int(input("Enter the day: "))

# seasonal range
if (month == "March" and day >= 20) or month in ("April", "May") or (month == "June" and day <= 20):
    season = 'Spring'
    
elif (month == "June" and day >= 21) or month in ("July", "August") or (month == "September" and day <= 21):
    season = 'Summer'
elif (month == "September" and day >= 22) or month in ("October", "November") or (month == "December" and day <= 20):
    season = 'Fall'
elif (month == "December" and day >= 21) or month in ("January", "February") or (month == "March" and day <= 19):
    season = 'Winter'

# Output the result
print(f'The season on {month} {day} is {season}.')
