width = int(input())
length = int(input())

volume = width * length
eaten_cakes = 0

while True:

    number_cakes = input()

    if number_cakes != "STOP":
        eaten_cakes += int(number_cakes)
        if eaten_cakes > volume:
            print(f"No more cake left! You need {eaten_cakes - volume} pieces more.")
            break
    elif number_cakes == "STOP":
        break


if eaten_cakes <= volume:
    print(f"{volume - eaten_cakes} pieces are left.")



