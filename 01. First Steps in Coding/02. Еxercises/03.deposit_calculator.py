deposit_sum = float(input())
months_for_deposit = int(input())
annual_interest_rate = float(input()) / 100

accrued_interest = deposit_sum * annual_interest_rate
interest_per_month = accrued_interest / 12
total = deposit_sum + (months_for_deposit * interest_per_month)

print(total)