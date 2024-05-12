name_participant = input()
points_academy = float(input())
num_jury = int(input())

for i in range(0, num_jury):
    name_jury = ""
    points_jury = ""

    for x in range(1, 3):

        if x % 2 != 0:
            name = input()
            name_jury = name
        if x % 2 == 0:
            points = float(input())
            points_jury = points

    current_points = len(name_jury) * points_jury / 2

    points_academy += current_points

    if points_academy > 1250.5:
        print(f"Congratulations, {name_participant} got a nominee for leading role with {points_academy:.1f}!")
        exit()


if points_academy <= 1250.5:
    print(f"Sorry, {name_participant} you need {1250.5 - points_academy:.1f} more!")