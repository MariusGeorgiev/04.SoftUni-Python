day_of_week = int(input())

day = ""

if day_of_week == 1:
    day = "Monday"
elif day_of_week == 2:
    day = "Tuesday"
elif day_of_week == 3:
    day = "Wednesday"
elif day_of_week == 4:
    day = "Thursday"
elif day_of_week == 5:
    day = "Friday"
elif day_of_week == 6:
    day = "Saturday"
elif day_of_week == 7:
    day = "Sunday"
else:
    day = "Error"

print(day)