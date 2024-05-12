num_groups = int(input())

total_people = 0

musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0


for i in range(0, num_groups):
    group = int(input())
    total_people += group

    if group < 6:
        musala += group
    elif 6 <= group <= 12:
        monblan += group
    elif 13 <= group <= 25:
        kilimandjaro += group
    elif 26 <= group <= 40:
        k2 += group
    elif group >= 41:
        everest += group


print(f"{musala / total_people * 100:.2f}%")
print(f"{monblan / total_people * 100:.2f}%")
print(f"{kilimandjaro / total_people * 100:.2f}%")
print(f"{k2 / total_people * 100:.2f}%")
print(f"{everest / total_people * 100:.2f}%")