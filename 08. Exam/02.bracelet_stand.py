pocket_money_daily = float(input())
daily_profit = float(input())
total_expenses = float(input())
price_of_the_present = float(input())

DAYS_LEFT = 5

saved_pocket = DAYS_LEFT * pocket_money_daily
save_from_profits = DAYS_LEFT * daily_profit

total_saved = saved_pocket + save_from_profits - total_expenses

if total_saved >= price_of_the_present:
    print(f"Profit: {total_saved:.2f} BGN, the gift has been purchased.")

if total_saved < price_of_the_present:
    print(f"Insufficient money: {(price_of_the_present - total_saved):.2f} BGN.")