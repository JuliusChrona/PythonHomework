def get_digits(num):
    digits = tuple([int(digit) for digit in str(num)])
    return digits


print(get_digits(87178291199))
