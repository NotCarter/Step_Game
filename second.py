username=input("Enter your username")
print (username)
password=input
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
else:
	print("Invalid operator, please try again.")