import random

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print("The message length:", len(message))

if "e" in message:
    print("is in your message")
else:
    print("is not in your message")

word = "index"

high = len(word)
low = -len(word)

for i in range (10):
    position = random.randrange(low, high)
    print("word[",position, "]\t", word[position])

for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("A new string has been created:",new_message)

print("Without vowels:",new_message)


word = "pizza"

print(word[0:5])
print(word[1:3])
print(word[-4:-2])
print(word[-4:3])
print(word[0:4])
print(word[:4])
print(word[2:5])
print(word[2:])
print(word[0:5])
print(word[:])

start = None
if start != "":
    start = int(input("\nStart: "))

    if start:

        finish = int(input("Finish: "))

        print("word[", start, ":",finish, "] is", end=" ")
        print(word[start:finish])


# tuple
inventory = ("sword", "armor", "shield", "healing potion")

if not inventory:
    print("You are empty handed")

print("The tuple inventory is:\n", inventory)

print("\nYour items:")
for item in inventory:
    print(item)

print("You have", len(inventory), "items in your possession")    

if "healing potion" in inventory:
    print("You fight another day")

index = int(input("Enter index of item: "))
print(inventory[index])

chest = ("gold", "gems")
print("Chest contains:", chest)
inventory += chest
print(inventory)
