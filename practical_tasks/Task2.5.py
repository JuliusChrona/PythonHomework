def call_once(func, called=False, result=None):
    def wrapper(*args, **kwargs):
        nonlocal called, result    
        if not called:
            result = func(*args, **kwargs)
            called = True
        return result
    return wrapper
    
@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(100, 100))
