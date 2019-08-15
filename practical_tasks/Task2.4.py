def combine_dicts(*args):
    dictionary = {}
    for pairs in args:
        for (key, value) in pairs.items():
            try:
                if dictionary[key]:
                    dictionary[key] += value
            except KeyError:
                dictionary[key] = value 
    return dictionary


def Test():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))

Test()