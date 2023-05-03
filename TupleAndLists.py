# Introducing Python. Bill Lubanovic
# Task 7.1-7.3
years_list = [1992, 1993, 1994, 1995, 1996]
print("7.1-7.3")
print(years_list[2], max(years_list))

# Task 7.4-7.7
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
things.remove("salmonella")
print("\n7.4-7.7")
print(things)

# Task 7.8-7.9
surprice = ["Groucho", "Chico", "Harpo"]
last = surprice[2].lower()
print("\n7.8 & 7.9")
print(last[::-1].capitalize())

# Task 7.10
even = [number for number in range(10) if number % 2 == 0]
print("\n7.10")
print(even)

# Task 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're down"),
]
start2 = "Someone better"
print("\n7.11")
for i in range(len(rhymes)):
    print(f'{start1[0].capitalize()}! '
          f'{start1[1].capitalize()}! '
          f'{start1[2].capitalize()}! '
          f'{rhymes[i][0].capitalize()}!')
    print(f'{start2} {rhymes[i][1]}.')
    print()
