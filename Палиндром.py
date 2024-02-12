all_products = {}
karzina = {}

while True:
    print("1. Добавить товар в склад ")
    print('2. Удалить товар из склада')
    print('3. Добавить в карзину')
    print('4. Замена товаров в карзине')
    print('5. Показать карзину')
    admin = input('Что вы хотите сделать? ')
    # 1. Добавить товар в склад
    if admin == '1':
        print('__________________________')
        print('Вы выбирали "1", можете дабавить товар в склад! ')
        product_name = input('Введите название продукта: ')
        product_count = int(input('Введите количество: '))
        all_products [product_name] = product_count
        print('Продукт успешно добавлен!')
    elif admin == 'Список':
        print(all_products)
        print('__________________________')
    # 2. Удалить товар из склада
    if admin == '2':
        print('__________________________')
        print('Вы выбирали "2", можете удалить товар из склада! ')
        product_name = input('Введите название продукта: ')
        if product_name in all_products:
            del all_products[product_name]
            print('Продукт успешно удален!')
            print(all_products)
        else:
            print('Товар нет на складе!')
            print(all_products)
    # 3. Добавить в карзину
    if admin == '3':
        print('__________________________')
        print('Вы выбирали "3", можете дабавить товар в карзину! ')
        product_name = input('Введите название продукта: ')
        if product_name in all_products:
            product_count = int(input('Введите количество: '))
            if product_count <= all_products[product_name]:
                if product_name in karzina:
                    karzina[product_name] += product_count
                else:
                    karzina[product_name] = product_count
                all_products[product_name] -= product_count
                print(f'{product_count} {product_name} добавлен в карзину')
                print(all_products)
            else:
                print('Недостаточно товара на складе!')
        else:
            print('Такого товара нет в магазине!')
    # 4. Замена товаров в карзине
    if admin == '4':
        print('__________________________')
        print('Вы выбирали "4", можете заменить товар в карзине! ')
        product_name = input('Введите название продукта: ')
        if product_name in karzina:
            change_name = input('Что хотите изменить?')






        else:
            print('Такой продукт нет в карзине!')








    # 5. Показать карзину
    if admin == '5':
        print(karzina )