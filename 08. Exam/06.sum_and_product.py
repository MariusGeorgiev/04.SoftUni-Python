n = int(input())

for a in range(1, 9 + 1):
    for b in range(9, a - 1, -1):
        for c in range(0, 9 + 1):
            for d in range(9, c - 1, -1):

                sum_of_combination = a + b + c + d
                multiplication_of_combination = a * b * c * d

                if sum_of_combination == multiplication_of_combination:
                    if n % 10 == 5:
                        print(f"{a}{b}{c}{d}")
                        exit()

                if sum_of_combination != 0:
                    if multiplication_of_combination // sum_of_combination == 3:
                        if n % 3 == 0:
                            print(f"{d}{c}{b}{a}")
                            exit()


print("Nothing found")

