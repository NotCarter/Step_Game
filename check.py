counter=3
username=input("Ener your username :")
print (username)
password=input("Enter a password here :")
while True:
	confirm=input("Confirm new password :")
	if confirm==password:
		print ("If your username is "+username+" and password is "+password+", your username and password are saved! Please move on to the next step; if that is not correct, restart the code.")
		break
	else:
		counter-=1
		print("incorrect password,", +counter," tries remaining.")
	if counter==0:
		print("Incorrect too many times, try again later.")
		break