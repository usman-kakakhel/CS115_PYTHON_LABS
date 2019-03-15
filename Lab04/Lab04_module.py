def generate_password(userName):
	import random
	password = ""
	for c in range(4):
		newChar  = userName[random.randint(0,len(userName)-1)]
		capital = random.randint(0,1)
		if(capital is  0):
			password = password + newChar.upper()
		else:
			password = password + newChar
	
	for t in range(4):
		password = password + str(random.randint(0,9))

	return password

def twoInput(x, y):
	if (x >= y):
		print(x, end= ' ')
		twoInput(x-y, y)
	else:
		print( x , " *")
		return

	return


