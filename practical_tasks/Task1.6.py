def get_longest_word(string):
    final_list = []
    for word in string.split():
        final_list.append(len(word))
    longest_word = string.split()[final_list.index(max(final_list))]
    print(longest_word)
    return longest_word


get_longest_word('Python is simple and effective!')
get_longest_word('Any pythonista like namespaces a lot.')
