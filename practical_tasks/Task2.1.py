def test_1_1(list_of_strings):
    if not list_of_strings:
        return None
    list_of_strings = [word.lower() for word in list_of_strings]
    char_in_all_strings = set(list_of_strings[0])
    for word in list_of_strings[1:]:
        char_in_all_strings = set(word) & char_in_all_strings
    return char_in_all_strings


def test_1_2(list_of_strings):
    if not list_of_strings:
        return None
    list_of_strings = [word.lower() for word in list_of_strings]
    list_of_strings = ''.join(list_of_strings)
    return set(list_of_strings)


def test_1_3(list_of_strings):
    if not list_of_strings:
        return None
    list_of_strings = [word.lower() for word in list_of_strings]
    result = set()
    for index, main_word in enumerate(list_of_strings):
        for word in list_of_strings[index+1:]:
            result = (set(main_word) & set(word)) | result
    return result


def test_1_4(list_of_strings):
    if not list_of_strings:
        return None
    import string
    list_of_strings = [word.lower() for word in list_of_strings]
    list_of_strings = ''.join(list_of_strings)
    result = set(list_of_strings) ^ set(string.ascii_lowercase)
    return result


def Tests():
    test_strings = ["hello", "world", "python"]
    print(test_1_1(test_strings))
    print(test_1_2(test_strings))
    print(test_1_3(test_strings))
    print(test_1_4(test_strings))


Tests()
