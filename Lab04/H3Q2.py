import Lab04_module

userNames = open("users.txt", "r")
userPasses = open("passwords.txt", "w")
user = " "
while(user != ""):
	user = userNames.readline()[:-1]
	if (user != ""):
		userPasses.write(Lab04_module.generate_password(user) + "\n")

