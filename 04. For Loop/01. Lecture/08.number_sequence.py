numbers = int(input())

min_num = ""
max_num = ""

for i in range(0, numbers):

    num = int(input())

    if i == 0:
        min_num = num
        max_num = num

    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num


print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
