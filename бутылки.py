price_small = 0.10
price_big = 0.25
quantity_small = float(input('Сколько количество бутылки объёмам 1л и меньшее: '))
quantity_big = float(input('Сколько количество бутылки объемом больше 1л:  '))
amount_small = price_small * quantity_small
amount_big = price_big * quantity_big
totle_amount = amount_small + amount_big
print(f'Сумма за сдачу бутылок объемом 1л и меньшее: ${amount_small: .2f}' )
print(f'Сумма за сдачу бутылок объемом больше 1л: ${amount_big: .2f}')
print(f'Общая сумма: ${totle_amount: .2f}')