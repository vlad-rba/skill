def cinema():
    age = int(input('Enter age: '))

    if age < 18:
        print('You can go free')
        return

    discount = get_discount(age)
    print_discount_message(discount)

    price = 14.95
    discd = calculate_discount_price(price, discount)

    print(f'  Your price: {discd} (original price: {price})')


def get_discount(age):
    if age <= 25:
        discount = 0.1
    elif age >= 65:
        discount = 0.15
    else:
        discount = 0.0

    return discount


def print_discount_message(discount):
    if discount == 0.0:
        print('  Not qualified for discount.')
    else:
        print('  Qualified for discount: {}%'.format(int(discount * 100)))


def calculate_discount_price(original_price, discount):
    return round(original_price - original_price * discount, 2)


if __name__ == '__main__':
    while True:
        cinema()
        more = input('Buy more? (Yes/No): ')
        if more != 'Yes':
            break
