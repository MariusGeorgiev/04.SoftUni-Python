mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

bonito_price = mackerel_price * 1.6
safrid_price = sprinkle_price * 1.8
MUSSELS_PRICE = 7.50


total_bonito = bonito_kg * bonito_price
total_safrid = safrid_kg * safrid_price
total_mussels = mussels_kg * MUSSELS_PRICE

total_sum = total_bonito + total_safrid + total_mussels

print(f"{total_sum:.2f}")
