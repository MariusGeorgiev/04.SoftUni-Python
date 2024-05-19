bad_grades = int(input())

all_bad_grades = bad_grades
count_problems = 0
sum_grades = 0
last_problem = ""

while True:
    name_of_exercise = input()

    if name_of_exercise != "Enough":
        last_problem = name_of_exercise

    count_problems += 1

    if name_of_exercise == "Enough":
        count_problems -= 1
        print(f"Average score: {sum_grades / count_problems:.2f}")
        print(f"Number of problems: {count_problems}")
        print(f"Last problem: {last_problem}")
        break

    grade_of_exercise = int(input())
    sum_grades += int(grade_of_exercise)

    if grade_of_exercise <= 4:
        all_bad_grades -= 1

    if all_bad_grades < 1:
        print(f"You need a break, {bad_grades} poor grades.")
        break
