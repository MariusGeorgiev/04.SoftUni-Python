for hour in range(24):
    for minutes in range(60):
        print(f"{hour}:{minutes}")

# for hour in range(24):
#     for minutes in range(60):
#         if hour < 10 and minutes < 10:
#             print(f"0{hour}:0{minutes}")
#         if hour < 10 and minutes >= 10:
#             print(f"0{hour}:{minutes}")
#         if hour >= 10 and minutes < 10:
#             print(f"{hour}:0{minutes}")
#         if hour >= 10  and minutes >= 10:
#             print(f"{hour}:{minutes}")
