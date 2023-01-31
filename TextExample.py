#Introducing Python. Bill Lubanovic
#Task 5.1

song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print("5.1")
print(song[-6:-1].capitalize())

#Task 5.2

questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What makes the sound 'Sis! Boom! Bah!'"]
answers = ["An exploding sheep.",
           "No. I'm a frayed knot.",
           "'Pop!' goes the weasel."]

enter = [f"Q: {questions[0]} \nA: {answers[0]}\n",
         f"Q: {questions[1]} \nA: {answers[1]}\n",
         f"Q: {questions[2]} \nA: {answers[2]}\n"]

print("\n5.2")
print(str(enter[0]))
print(str(enter[1]))
print(str(enter[2]))

#Task 5.3
one = "roast beef"
two = "ham"
three = "head"
four = "clam"
poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.""" % (one, two, three, four)

print("5.3")
print(poem)

#Task 5.4 & 5.5
letter = "Dear {salutation} {name},\n\n" \
         "Thank you for your letter. We are sorry " \
         "that our {product} {verbed} in your {room}.\n" \
         "Please note that it should never be used in " \
         "a {room}, especially near any {animals}.\n\n" \
         "Send us your receipt and {amount} for shipping " \
         "and handling. We will send you another {product} " \
         "that,\nin our tests, is {percent} less likely to have {verbed}.\n\n" \
         "Thank you for support.\n" \
         "Sincerely,\n" \
         "{spokesman}\n" \
         "{job_title}.".format(salutation="Uncle", name="Sam", product="paint", verbed="leak",
                               room="balcony", animals="cat", amount=100, percent=50, spokesman="Tom",
                               job_title="Ubisoft")

print("\n5.4 & 5.5")
print(letter)

#Task 5.6 - 5.8
duck = "Duck"
pumpkin = "Pumpkin"
spitz = "Spitz"

resultOldStyle = "%sy Mc%sface \n%sy Mc%sface \n%sy Mc%sface\n " % (duck, duck, pumpkin, pumpkin, spitz, spitz)
resultNewStyle = "{}y Mc{}face \n{}y Mc{}face " \
                 "\n{}y Mc{}face\n".format(duck, duck, pumpkin, pumpkin,spitz, spitz)
resultFStyle = f"{duck}y Mc{duck}face \n{pumpkin}y Mc{pumpkin}face " \
               f"\n{spitz}y Mc{spitz}face"
print("\n5.6 - 5.8")
print(resultOldStyle)
print(resultNewStyle)
print(resultFStyle)
