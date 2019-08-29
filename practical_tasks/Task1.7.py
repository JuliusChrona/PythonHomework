def foo(some_list):
    mult = some_list[0]
    for num in some_list[1:]:
        mult *= num
    final_list = [int(mult/num) for num in some_list]
    print(final_list)
    return final_list


foo([1, 2, 3, 4, 5])
foo([3, 2, 1])
