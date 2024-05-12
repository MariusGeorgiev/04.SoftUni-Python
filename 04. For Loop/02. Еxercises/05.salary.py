num_tabs = int(input())
salary = int(input())

for i in range(0, num_tabs):
    new_tab = input()

    if new_tab == "Facebook":
        salary -= 150
    elif new_tab == "Instagram":
        salary -= 100
    elif new_tab == "Reddit":
        salary -= 50

    if salary <= 0:
        print("You have lost your salary.")
        exit()

print(salary)