username=input("Ener your username :")
print (username)
password=input("Enter a password here :")
confirm=input("Confirm new password :")
if confirm==password:
	print ("If your username is "+username+" and password is "+password+", your username and password are saved! Please move on to the next step; if they are not correct not please re-run the system.")
else:
	print("incorrect password, please try again")
	confirm=input("Confirm new password")