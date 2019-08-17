pi = 2
e = 1


def sin():
    return 42


def cos():
    return 33


def masking(string):
    """ replace characters on # besides last 4-th """
    return "#"*(len(cc)-4) + cc[-4:]


def is_palindrome(string):
    return True if string == string[::-1] else False


def get_digits(num):
    digits = tuple([int(digit) for digit in str(num)])
    return digits
