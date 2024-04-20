square_metres = float(input())

price_for_one_square = 7.61
discount = 0.82

print(f'The final price is: {square_metres * price_for_one_square * discount} lv.')
print(f'The discount is: {(square_metres * price_for_one_square) - (square_metres * price_for_one_square * discount)} lv.')

