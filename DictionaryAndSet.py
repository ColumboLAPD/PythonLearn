# Introducing Python. Bill Lubanovic

# Task 8.1-8.5

print("#8.1-8.5")
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(e2f['walrus'])
f2e = dict((values, keys) for keys, values in e2f.items())
f2e2 = {}
for keys, values in e2f.items():
    f2e2[values] = keys
print(f2e['chien'])
print(set(e2f))

# Task 8.6-8.9

life = {
    'animals': {'cats': ('Henri', 'Grumpy', 'Lucy'), 'octopi': (), 'emus': ()},
    'plants': {},
    'other': {}
}
print("\n#8.6-8.9")
print(life.keys(), '\n', life['animals'].keys(), '\n', life['animals']['cats'])

# Task 8.10-8.11

num_tuple = tuple(range(10))
squares = {i: num_tuple[i]*i for i in num_tuple}
odd = {i for i in range(10) if i % 2 == 1}
print("\n#8.10-8.11")
print(squares, odd)

# Task 8.13

psycho = ('optimist', 'pessimist', 'troll')
description = ("The glass is half full", "The glass is half empty", "How did you get a glass?")
psycho_disc = dict(zip(psycho, description))
print("\n#8.13")
print(psycho_disc)
