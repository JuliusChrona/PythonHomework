def split_by_index(string, indexes: list):
    final_list = []
    word = ""
    for char in string:
        if string.index(char) in indexes:
            final_list.append(word)
            word = ""
            word += char
            continue
        word += char
    final_list.append(word)
    return final_list
    
print(split_by_index("pythoniscool,isn'tit", [6,8,12,13,18]))