hour_exam = int(input())
minutes_exam = int(input())

hour_arrive = int(input())
minutes_arrive = int(input())

exam_time_in_minutes = (hour_exam * 60) + minutes_exam
arrive_time_in_minutes = (hour_arrive * 60) + minutes_arrive

status = ""

if exam_time_in_minutes - arrive_time_in_minutes > 30:
    status = "Early"
elif 0 <= (exam_time_in_minutes - arrive_time_in_minutes) <= 30:
    status = "On time"
elif exam_time_in_minutes < arrive_time_in_minutes:
    status = "Late"

if exam_time_in_minutes == arrive_time_in_minutes:
    print(status)
    exit()

if 0 <= (exam_time_in_minutes - arrive_time_in_minutes) < 60:
    print(status)
    print(f"{exam_time_in_minutes - arrive_time_in_minutes} minutes before the start")
elif (exam_time_in_minutes - arrive_time_in_minutes) >= 60:
    print(status)
    time_hour = ((exam_time_in_minutes - arrive_time_in_minutes) // 60)
    time_minutes = ((exam_time_in_minutes - arrive_time_in_minutes) % 60)
    if time_minutes < 10:
        print(f"{time_hour}:0{time_minutes} hours before the start")
    else:
        print(f"{time_hour}:{time_minutes} hours before the start")


if 0 <= (arrive_time_in_minutes - exam_time_in_minutes) < 60:
    print(status)
    print(f"{arrive_time_in_minutes - exam_time_in_minutes} minutes after the start")

elif (arrive_time_in_minutes - exam_time_in_minutes) >= 60:
    print(status)
    time_hour = ((arrive_time_in_minutes - exam_time_in_minutes) // 60)
    time_minutes = ((arrive_time_in_minutes - exam_time_in_minutes) % 60)
    if time_minutes < 10:
        print(f"{time_hour}:0{time_minutes} hours after the start")
    else:
        print(f"{time_hour}:{time_minutes} hours after the start")