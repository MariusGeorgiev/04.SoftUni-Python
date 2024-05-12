import math

num_tournaments = int(input())
point_rank_list = int(input())
initial_points = point_rank_list
num_win_tournament = 0

for i in range(0, num_tournaments):

    current_tournament = input()

    if current_tournament == "W":
        point_rank_list += 2000
        num_win_tournament += 1
    elif current_tournament == "F":
        point_rank_list += 1200
    elif current_tournament == "SF":
        point_rank_list += 720

print(f"Final points: {point_rank_list}")
print(f"Average points: {math.floor((point_rank_list - initial_points) / num_tournaments)}")
print(f"{num_win_tournament / num_tournaments * 100:.2f}%")