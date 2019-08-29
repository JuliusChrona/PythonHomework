string = input("Enter a string: ")
counter = 0
final_list = []
for char in list(string):
    if char == '"':
        char = "'"
        counter += 1
    elif char == "'":
        char = '"'
        counter += 1
    final_list.append(char)
else:
    if counter == 0:
        print('Your string ', string, 'doesn\'t contain a character \' or "')
    else:
        print("Your new string is ", ''.join(final_list))
