import math

number_of_pages = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())

total_time_for_reading_book = number_of_pages // pages_for_one_hour
needed_hours_per_day = total_time_for_reading_book // number_of_days

print(needed_hours_per_day)