import math

record = float(input())
length = float(input())
time_swimming_one_meter = float(input())

time_ivan_needed = length * time_swimming_one_meter

time_delay = math.floor((length / 15)) * 12.5

all_time_needed = time_ivan_needed + time_delay

if record > all_time_needed:
    print(f"Yes, he succeeded! The new world record is {all_time_needed:.2f} seconds.")

if record <= all_time_needed:
    print(f"No, he failed! He was {all_time_needed - record:.2f} seconds slower.")



