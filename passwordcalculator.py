import random
number = random.randint (1, 100)
username= "cnoel4"
password= "Hi53Hello"
counter=3
while True:
	Confirm=input("Enter username :")
	confirm=input("Enter password :")
	if confirm==password and  Confirm==username:
		app=input("Which app would you like to use(Calc Sigma calc or Game1?")
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
	else:
		counter-=1
		if counter==0:
			print ("Incorrect too many times, try again later")
			break
		else:
			print("Incorrcet Username Or Password,", +counter, " Tries Left")