is_valid = False
def check_valid(age,age_limit = 18) -> bool:
    try:
        age = int(age)
    except TypeError:
        print("enter an integer!")
        return False
    if age <= age_limit:
        print(f"enter a value greater than {age_limit}")
        return False

    print("congrats")
    return True

strike = 0
strike_limit = 5
while not is_valid:
    if strike == strike_limit:
        print("you lost")
    else:
        strike += 1
        age = input("please enter an age:")
        is_valid = check_valid(age,13)