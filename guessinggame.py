import random

print("Welcome to the number guessing game! You have 7 chances to guess the correct number. Good Luck!")

a = int(input("Enter lower bound of range: "))
b = int(input("Enter upper bound of range: "))

num = random.randrange(a, b)


chances = 7
guess_no = 0
counter = 7

while guess_no < chances:
    user = int(input("Guess selected number: "))
    guess_no += 1
    counter -= 1
    if user == num:
        print("Congratulations! You guessed the correct number in", guess_no, "attempts! The number was: ", num)
    elif guess_no == chances and user != num:
        print("Oops! You ran out of attempts. The correct number was: ", num)
        break
    elif user < num:
        print("Sorry. You guessed too low. Remaining attempts: ", counter)
    elif user > num:
        print("Sorry. You guessed too high. Remaining attempts: ", counter)