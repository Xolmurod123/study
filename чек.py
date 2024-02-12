order = float(input('Введите сумму заказа: '))
tax = 0.12
tips = 0.18
amount_tax = order * tax
amount_tips = order * tips
total = amount_tax + amount_tips + order
print(f'Чек с налогам: ${amount_tax: .2f}')
print(f'Чаевые: ${amount_tips: .2f}')
print(f'Итог: ${total: .2f}')