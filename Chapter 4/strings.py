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