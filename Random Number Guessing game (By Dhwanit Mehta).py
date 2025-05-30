import random

gen=random.randint(1,100)

a=int(input("Guess a number between 1-100 which you think the computer has chosen:- "))

while True:

    if a==gen:
        print("Eyyy congratulations! You guessed the number!")
        print("Thank you for playing! Bye!")
        break

    elif 100>a>gen:
        print("You are higher than the number! Try guessing lower.")

    elif 0<a<gen:
        print("You are lower than the number. Try guessing higher.")

    elif a>100 or a<=0:
        print("I get that you are a very smart person my friend but... \n"
              "I SAID GUESS A NUMBER BETWEEN 1-100 WHY ARE YOU GUESSING HIGHER/LOWER THAN THAT!?")

        a=int(input("Guess again: "))