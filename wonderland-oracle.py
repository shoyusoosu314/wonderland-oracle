import random
import time

print("Welcome to the Wonderland Oracle")
time.sleep(1)
print("One of the following creatures that you choose will tell your fortune today:")
time.sleep(1)
print("1. The White Rabbit")
time.sleep(0.5)
print("2. The Cheshire Cat")
time.sleep(0.5)
print("3. The Cartepillar")
time.sleep(0.5)
print("4. The Queen of Hearts")
time.sleep(0.5)
print("5. The Mad Hatter")
time.sleep(1)

choice = input("\nWhich number do you choose? (1-5): ")

good_fortunes = [
    "Your curiosity will open a powerful door soon.",
    "Something small will become something huge (in a good way).",
    "Something that you have been thinking about will make sense soon."
]

bad_fortunes = [
    "You're falling down a rabbit hole progressively.",
    "You're running out of time, for something you don't even know about.",
    "Remember that not everyone who is kind to you is your friend.",
    "The Queen may not be pleased with your next move..."
]

extra_fortunes = [
    "The stars align in your favor—ask for anything, but be wise.",
    "You are watched by a force that finds you *amusing*. That is good… for now.",
    "You will receive a gift you didn't expect, in a form you do not recognize.",
    "Time is a construct, but your next move is crucial. Choose wisely.",
]

if choice == "1" or choice == "2":
    print("\nYour fortune from Wonderland:")
    print(random.choice(good_fortunes))
elif choice == "4" or choice == "5":
    print("\nA warning from the Carterpillar:")
    print(random.choice(bad_fortunes))
elif choice == "3":
    print("\nYou have choosen the lucky number! Your fortune says:")
    print(random.choice(extra_fortunes))
else:
    print("\nThe decision taken has disappointed the Oracle.")
    time.sleep(1.5)
    print("You have been marked as 'unpredictable'. Something is watching you from beyond now.\n")