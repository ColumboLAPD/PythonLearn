# Introducing Python. Bill Lubanovic
# Task 6.1
print('6.1')
numbers = [3, 2, 1, 0]
for i in numbers:
    print(i)

print()

for i in range(3, -1, -1):
    print(i)

# Task 6.2
print('\n6.2')
guess_me = 7
number = 1
while number <= guess_me:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("Found it!")
        break
    else:
        print("Oops!")
    number += 1

# Task 6.3
print('\n6.3')
guess_me = 5
for number in range(10):
    if number < guess_me:
        print("Too low")
    elif number == guess_me:
        print("Fount it!")
        # break
    else:
        print("Oops!")
        break
