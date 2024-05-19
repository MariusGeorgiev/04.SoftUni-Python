book = input()

count_check = 0
while True:
    next_book = input()

    count_check += 1

    if book == next_book:
        count_check -= 1
        print(f"You checked {count_check} books and found it.")
        break

    if next_book == "No More Books":
        count_check -= 1
        print(f"The book you search is not here!")
        print(f"You checked {count_check} books.")
        break




