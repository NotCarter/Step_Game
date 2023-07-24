password= "1243"
counter=0
while True:
	confirm=input("Enter password :")
	if confirm==password:
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
		break
	else:
		counter+=1
		if counter==5:
			print ("Incorrect too many times, try again later")
			break