
all_steps = 0
counter = 0
while True:
    steps = input()
    if steps != "Going home":
        all_steps += int(steps)
        if all_steps > 10000:
            break
        if counter > 0:
            break

    if steps == "Going home":
        counter += 1
        continue


if all_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{all_steps - 10000} steps over the goal!")
else:
    print(f"{10000 - all_steps} more steps to reach goal.")

