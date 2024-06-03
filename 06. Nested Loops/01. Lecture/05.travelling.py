destination = input()
needed_budget = float(input())

all_savings = 0
while True:
    saving = float(input())
    all_savings += saving

    if all_savings >= needed_budget:
        print(f"Going to {destination}!")
        all_savings = 0
        destination = input()
        if destination != "End":
            needed_budget = float(input())
        else:
            exit()





