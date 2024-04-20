number_of_packs_pens = int(input())
number_of_packs_markers = int(input())
liters_cleaning_detergent = int(input())
percent_discount = int(input())

price_for_packs_pens = number_of_packs_pens * 5.80
price_for_packs_markers = number_of_packs_markers * 7.20
price_for_detergent = liters_cleaning_detergent * 1.20
total_price = price_for_packs_pens + price_for_packs_markers + price_for_detergent
price_with_discount = percent_discount * 0.01

print(total_price - (total_price * price_with_discount))

