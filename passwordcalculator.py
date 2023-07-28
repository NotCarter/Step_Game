import random
number = random.randint (1, 100)
username= "Mickey"
password= "Mousekatoodles"
counter=3
while True:
	Confirm=input("Enter username :")
	confirm=input("Enter password :")
	if confirm==password and  Confirm==username:
		app=input("Which app would you like to use;Calc, Sigma calc, Game1, or Greater than calc?")
		if app== "calculator":
			num1=int(input("enter first number"))
			num2=int(input("enter second number"))
			operation=input("what operation, +,-,*,/")
			if operation== "+":
				print(num1+num2)
			elif operation== "-":
				print(num1-num2)
			elif operation== "*":
				print(num1*num2)
			elif operation== "/":
				if(num2==0):
					print("Can't devide by zero")
				else:
					print(num1/num2)
		elif app== "Calculator":
			num1=int(input("enter first number"))
			num2=int(input("enter second number"))
			operation=input("what operation, +,-,*,/")
			if operation== "+":
				print(num1+num2)
			elif operation== "-":
				print(num1-num2)
			elif operation== "*":
				print(num1*num2)
			elif operation== "/":
				if(num2==0):
					print("Can't devide by zero")
				else:
					print(num1/num2)
		if app== "sigma calculator":
			n=int(input("Input value for N: "))
			print((n*(n+1))/2)
		elif app== "Sigma calculator":
			n=int(input("Input value for N: "))
			print((n*(n+1))/2)
		elif app== "Sigma Calculator":
			n=int(input("Input value for N: "))
			print((n*(n+1))/2)
		elif app== "sigma Calculator":
			n=int(input("Input value for N: "))
			print((n*(n+1))/2)
		if app== "greater than calculator":
			a=int(input("Input a value for A: "))
			b=int(input("Input a value for B: "))
			c=int(input("Input a value for C: "))
			if a > b:
				if a > c:
					print("a is the greatest")
					if b > c:
						print("b is the middle")
						print("c is the least")
					else:
						print("c is the middle")
						print("b is the least")
			if b > a:
				if b > c:
					print("b is the greatest")
					if a > c:
						print("a is the middle")
						print("c is the least")
					else:
						print("c is the middle")
						print("a is the least")
			if c > b:
				if c > a:
					print("c is the greatest")
					if b > a:
						print("b is the middle")
						print("c is the least")
					else:
						print("a is the middle")
						print("b is the least")
		elif app== "Greater Than Calculator":
			a=int(input("Input a value for A: "))
			b=int(input("Input a value for B: "))
			c=int(input("Input a value for C: "))
			if a > b:
				if a > c:
					print("a is the greatest")
					if b > c:
						print("b is the middle")
						print("c is the least")
					else:
						print("c is the middle")
						print("b is the least")
			if b > a:
				if b > c:
					print("b is the greatest")
					if a > c:
						print("a is the middle")
						print("c is the least")
					else:
						print("c is the middle")
						print("a is the least")
			if c > b:
				if c > a:
					print("c is the greatest")
					if b > a:
						print("b is the middle")
						print("c is the least")
					else:
						print("a is the middle")
						print("b is the least")
		if app== "game1":
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
		if app== "Game 1":
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
		if app== "Guess":
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
		if app== "guess":
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
		if app== "Rps" or "RPs" or "RPS" or "rps":
			print("welcome to Rock Paper Scissors!")
			choices=["rock", "paper", "scissors"]
			while True:
				player_choice=int(input(" Enter your choice:\n1. Rock\n2. Paper\n3. Scissors\nYour choice (1/2/3): "))
				if player_choice not in [1,2,3]:
					print("Invalid choice. Choose number 1/2/3 for Rock/Paper/Scissors")
					continue
				player_choice -=1
				computer_choice=random.randint(0,2)
				print(f"Your choice: {choices[player_choice]}")
				print(f"Computer's choice: {choices[computer_choice]}")
				if player_choice==computer_choice:
					print("Tie!")
				elif (player_choice == 0 and computer_choice == 2) or \
					(player_choice == 1 and computer_choice == 0) or \
					(player_choice == 2 and computer_choice == 1):
					print("You win!")
				else:
					print("Computer wins!")
				play_again=input("Do you want to play again? (y/n): ")
				if play_again != 'y':
					print("Thanks for playing! Goodbye!")
					break
	else:
		counter-=1
		if counter==0:
			print ("Incorrect too many times, try again later")
			break
		else:
			print("Incorrect Username Or Password,", +counter, " Tries Left")