L_R_B = 1111
R_R_B = 9999

number = int(input())

for current_number in range(L_R_B, R_R_B + 1):

    str_from_number = str(current_number)
    is_special = True

    for _, value in enumerate(str_from_number):
        int_val = int(value)
        if int_val == 0:
            is_special = False
            break

        if int_val != 0 and number % int_val != 0:
            is_special = False
            break

    if is_special:
        print(current_number, end=" ")