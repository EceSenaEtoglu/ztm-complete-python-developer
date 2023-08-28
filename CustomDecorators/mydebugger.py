# if you dont know debugging, debug your  global variable with this template
without throwing bunch of print statements to your functions!

# refactor income as your global variable
# modify the functions to update your global variable

income = 5
def debugger(func):
    def wrapper_func(*args,**kwargs):
        old_income = income
        print(f'function {func.__name__} called with arguments args: {args} kwargs: {kwargs}')

        a = func(*args,**kwargs)
        print(f'function changed global income from {old_income} to {income}')
        return a
    return wrapper_func

@debugger
def decrement_income(dec_amount):
    global income
    income -= dec_amount

@debugger
def increase_income(inc_amount):
    global income
    income += inc_amount


print(income)
decrement_income(6)
increase_income(9)