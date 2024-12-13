import random

name = input("Enter your name: ")
print("Welcome ", name, "! Guess the fruit within the given number of tries to win the game. Good Luck!")

words = ['apple', 'banana', 'mango', 'strawberry', 
'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 
'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

word = random.choice(words)

guesses = '_' * len(word)

chances = len(word) + 2
guesses_list = list(guesses)
print(guesses_list)
print("You have ", chances, "tries. Good luck!")

while chances > 0:
    
    try:
        k = str(input("Enter a character: "))
    except:
        print("Enter only a letter")
        continue
    if not k.isalpha():
        print("Enter only a LETTER")
        continue
    elif not k.islower():
        print("Enter only LOWER CASE LETTER")
        continue
    elif len(k) > 1:
        print("Enter only a SINGLE LETTER")
        continue
    elif k in guesses_list:
        print("You have already guessed this letter")
        continue
    chances -= 1
    if k in word:
        indices = [i for i, wd in enumerate(word) if wd == k]
        for ind in indices:
            guesses_list[ind] = k
        print(str(guesses_list))

    elif k not in word:
        print("Opps!. You guessed incorrectly. Remaining tries are = ", chances)

    if "_" not in guesses_list:
        print("Congratulations! You guessed the word with ", chances, "remaining chances. The word was: ", word)
        break
    elif chances == 0:
        print("Oops! You ran out of attempts. The word was: ", word)
        print("Please try again")


