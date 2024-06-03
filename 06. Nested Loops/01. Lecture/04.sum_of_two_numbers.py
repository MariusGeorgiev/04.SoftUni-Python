start_num = int(input())
end_num = int(input())
magic_num = int(input())

all_combinations = 0

for num in range(start_num, end_num + 1):

    # sum_of_nums = start_num + num
    # print(sum_of_nums)
    for num2 in range(start_num, end_num + 1):
        all_combinations += 1
        sum_of_nums = num + num2
        if sum_of_nums == magic_num:
            print(f"Combination N:{all_combinations} ({num} + {num2} = {sum_of_nums})")
            exit()

print(f"{all_combinations} combinations - neither equals {magic_num}")
