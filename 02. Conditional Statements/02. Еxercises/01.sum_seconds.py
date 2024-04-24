first_contestant = int(input())
second_contestant = int(input())
third_contestant = int(input())

all_time = first_contestant + second_contestant + third_contestant
all_minutes = all_time // 60
all_seconds = all_time % 60

if all_seconds < 10:
    print(f"{all_minutes}:0{all_seconds}")
else:
    print(f"{all_minutes}:{all_seconds}")