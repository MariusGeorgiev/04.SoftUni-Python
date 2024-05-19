width = int(input())
length = int(input())
height = int(input())

count_cubic = 0

while True:
    num_boxes = input()
    if num_boxes != "Done":
        count_cubic += int(num_boxes)
        if count_cubic > (width * length * height):
            print(f"No more free space! You need {count_cubic - (width * length * height)} Cubic meters more.")
            break
    elif num_boxes == "Done":
        print(f'{(width * length * height) - count_cubic} Cubic meters left.')
        break

