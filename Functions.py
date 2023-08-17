# Introducing Python. Bill Lubanovic

# Task 9.1-9.4

print("#9.1")


def good():
    list_gp = ["Harry", "Ron", "Hermione"]
    return list_gp


print(good())
print()
print("#9.2")


def get_odds(start=1, end=10, step=2):
    number = start
    while number < end:
        yield number
        number += step


odd = get_odds()
first = 0
for i in odd:
    if first == 2:
        print(i)
    first += 1


print()
print("#9.3")


def test(func):
    def new_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_func


@test
def start_end():
    print("hello")


start_end()


print()
print("#9.4")


class OopsException(Exception):
    pass


minimal = 100


try:
    if minimal > 10:
        raise OopsException
    else:
        print(minimal)
except OopsException:
    print("Caught an oops")

