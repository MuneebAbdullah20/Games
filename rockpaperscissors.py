import random

print("Welcome to Rock, Paper and Scissors!")
print("The rules of the game are as follows: ")
print()
print("Rock vs Paper ------> Paper wins")
print("Scissors vs Paper ------> Scissors wins")
print("Rock vs Scissors ------> Rock wins")
print()
print("Enter your choice")
print("1- Rock")
print("2- Paper")
print("3- Scissors")
print()

i = 0
while i < 1:
    try:
        user_choice = int(input("Enter your choice: "))
    except:
        print("Enter ONLY 1 for Rock, 2 for paper and 3 for scissors")
        continue
    if user_choice not in [1, 2, 3]:
        print("Enter ONLY 1 for Rock, 2 for paper and 3 for scissors")
        continue
    comp_choice = random.randrange(1,4)
    # comp_choice = 2
    if user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    elif user_choice == 3:
        user_choice_name = "Scissors"

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    elif comp_choice == 3:
        comp_choice_name = "Scissors"


    if user_choice == comp_choice:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Draw. Try again")
        continue
    elif user_choice == 1 and comp_choice == 2:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Oops! You lost. Try again")
        print("Do you want to play again? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break
        elif ans == 'y':
            continue
    elif user_choice == 1 and comp_choice == 3:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Congratulations! You won!")
        print("Do you want to play again? (Y/N)")
        while True:
            ans = input().lower()
            if ans in ['n', 'y']:
                break
            else:
                print("Enter ONLY 'n' or 'y'")
        if ans == 'n':
                break
    elif user_choice == 2 and comp_choice == 1:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Congratulations! You won!")
        print("Do you want to play again? (Y/N)")
        while True:
            ans = input().lower()
            if ans in ['n', 'y']:
                break
            else:
                print("Enter ONLY 'n' or 'y'")
        if ans == 'n':
                break
    elif user_choice == 2 and comp_choice == 3:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Oops! You lost. Try again")
        print("Do you want to play again? (Y/N)")
        while True:
            ans = input().lower()
            if ans in ['n', 'y']:
                break
            else:
                print("Enter ONLY 'n' or 'y'")
        if ans == 'n':
                break
    elif user_choice == 3 and comp_choice == 1:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Oops! You lost. Try again")
        print("Do you want to play again? (Y/N)")
        while True:
            ans = input().lower()
            if ans in ['n', 'y']:
                break
            else:
                print("Enter ONLY 'n' or 'y'")
        if ans == 'n':
                break
    elif user_choice == 3 and comp_choice == 2:
        print("You chose ", user_choice_name, "and computer chose ", comp_choice_name)
        print("Congratulations! You won!")
        print("Do you want to play again? (Y/N)")
        while True:
            ans = input().lower()
            if ans in ['n', 'y']:
                break
            else:
                print("Enter ONLY 'n' or 'y'")
        if ans == 'n':
                break
