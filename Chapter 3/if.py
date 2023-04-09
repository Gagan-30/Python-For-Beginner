import random

die1 = random.randint(1,6)
die2 = random.randrange(6) + die1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

password = input("Enter your password: ")

if password == "secret":
    print("Access Granted")
else:
    print("Access Denied")

mood = random.randint(1, 3)

if mood == 1:
    print("Happy")
elif mood == 2:
    print("Neutral")
elif mood == 3:
    print("Sad")
else:
    print("Illegal mood")