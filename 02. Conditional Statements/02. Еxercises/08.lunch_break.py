import math

name_series = input()
length_episode = int(input())
length_break = int(input())

time_launch = length_break / 8
time_relax = length_break / 4

left_time_for_episode = length_break - time_launch - time_relax

if left_time_for_episode >= length_episode:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(left_time_for_episode - length_episode)} minutes free time.")
elif left_time_for_episode < length_episode:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(length_episode - left_time_for_episode)} more minutes.")