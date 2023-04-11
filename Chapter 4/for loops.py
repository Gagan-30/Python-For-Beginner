word = input("Enter a word: ")

print("\n Here's each letter in your word: ")
for letter in word:
    print(letter)

print("Counting: ")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives: ")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nCounting backwards: ")
for i in range(10, 0, -1):
    print(i, end=" ")