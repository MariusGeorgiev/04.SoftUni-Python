name_of_the_movie = input()
num_days = int(input())
num_tickets = int(input())
price_ticket = float(input())
percentage_for_cinema = int(input()) / 100

price_for_all_days = num_tickets * price_ticket * num_days
final_price = price_for_all_days - (price_for_all_days * percentage_for_cinema)

print(f"The profit from the movie {name_of_the_movie} is {final_price:.2f} lv.")