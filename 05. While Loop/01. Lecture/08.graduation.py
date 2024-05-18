name = input()

sum_all_grade = 0
count = 0
count_broken = 0
last_grade = 0
while True:
    count += 1
    grade = float(input())
    sum_all_grade += grade

    if grade < 4.00:
        count_broken += 1
        count -= 1

    if count_broken == 1 and grade >= 4.00:
        count_broken -= 1
        sum_all_grade -= last_grade

    if count_broken > 1:
        print(f"{name} has been excluded at {count + 1} grade")
        break

    if count > 11:
        print(f"{name} graduated. Average grade: {(sum_all_grade / count):.2f}")
        break

    last_grade = grade

