def generate_squares(number: int):
    result = {num: pow(num, 2) for num in range(1, number+1)}
    return result
    
print(generate_squares(5))