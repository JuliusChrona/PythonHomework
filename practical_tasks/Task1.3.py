def my_split(delimiter: str, string):
    final_list = []
    word = ""
    for char in string:
        if char == delimiter:
            final_list.append(word)
            word = ""
            continue
        word += char
    final_list.append(word)
    print(final_list)
    return final_list


some_string = input("Enter a string: ")
some_delimiter = input("Enter a delimiter: ")
my_split(some_delimiter, some_string)
