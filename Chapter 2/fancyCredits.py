from cgi import print_environ
import quopri


print("\t\t\tFancy Credits")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")
print("\t\t\tby")
print("\t\t\tGagan")
print("\t\t\t \\ \\ \\ \\ \\ \\ \\")

print("\nSpecial thanks goes out to:")
print("My hair stylist. Henry \'The Great.\' who never says \"can\'t")

# sound the system bell
print("\a")

print("\nThis string " + "may not " + "strings with the '+' operator.")
print("\nThis string " + "may not " + "seem terr" + "ibly impressive. " \
      + "But what " + "you don't know" + "is that\n" + "it's one real" \
      + "l" + "y" + "long string. created from the conatenation " \
      + "of " + "twenty-two\n" + "different strings, broken across " \
      + "six lines." + " Now are you" + "impressed? " + "Okay,\n" \
      + "this " + "one " + "long" + " string is now over!")

print("2000 - 100 + 50 =", 2000 - 100 + 50)

name = "bob"
print(name)
print("Hi", name)

num = int(input("Enter a number "))
print(num)

quote = "I think there is a world market for maybe 5 computers"

print(quote)
print(quote.upper())
print(quote.lower())
print(quote.title())
print(quote.replace("five", "millions of"))

input("\n\nPress the enter key to exit")