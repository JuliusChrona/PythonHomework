def is_palindrome(string):
    if not string == string[::-1]:
        print(string, " - isn't a palindrome", sep="")
    else:
        print(string, " - is a palindrome", sep="")


def Tests():
    is_palindrome('racecar')
    is_palindrome('level')
    is_palindrome('Hello')


Tests()
