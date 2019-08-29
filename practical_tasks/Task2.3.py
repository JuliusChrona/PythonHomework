def count_letters(string: str):
    dictionary = {letter: string.count(letter) for letter in string}
    return dictionary


print(count_letters("stringsample"))
