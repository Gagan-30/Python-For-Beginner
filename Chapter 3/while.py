import random

response = ""

while response != "Because":
    response = input("Why\n")

print("Okay")
 
health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage

    print("Your hero swings and defeats a troll, but takes" , damage , "damage points")

count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

print("Guess a number")
num = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1

while guess != num:
    if guess > num:
        print("Lower")
    else:
        print("Higher")

    guess = int(input("Take a guess: "))
    tries += 1

print("Number:", num)
print("Tries:", tries)

