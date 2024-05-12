nums = int(input())

first_sum = 0
second_sum = 0

for i in range(0, nums):

    num = int(input())

    if i % 2 == 0:
        first_sum += num
    else:
        second_sum += num


if first_sum == second_sum:
    print("Yes")
    print(f"Sum = {first_sum}")

if first_sum < second_sum:
    print("No")
    print(f"Diff = {second_sum - first_sum}")

if second_sum < first_sum:
    print("No")
    print(f"Diff = {first_sum - second_sum}")

