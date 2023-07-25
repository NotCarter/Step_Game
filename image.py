import random
number = random.randint (1, 100)
Counter=0
name=input ("Enter your name: ")
while True:
    guess=int(input("Guess a number between 1 and 100: "))
    if number > guess:
        Counter+=1
        print("Too low!")
    elif number < guess:
        Counter+=1
        print("Too high!")
    else:
        Counter+=1
        print("Congradulations", name,"! You guessed the number in", +Counter, "Tries!")
        break