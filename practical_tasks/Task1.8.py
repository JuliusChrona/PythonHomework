def get_pairs(some_list):
    if len(some_list) <= 1:
        print(None)
        return None
    pairs = []
    for num in some_list[:-1]:
        if some_list != []:
            pairs.append((some_list.pop(0), some_list[0]))
        else:
            break
    print(pairs)
    return pairs

def Tests():
    get_pairs([1, 2, 3, 8, 9])
    get_pairs(['need', 'to', 'sleep', 'more'])
    get_pairs([1])

Tests()
