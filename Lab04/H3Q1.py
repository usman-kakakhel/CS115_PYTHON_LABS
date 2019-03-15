import Lab04_module

x = int(input("Enter positive number: "))
y = int(input("Enter Step: "))

if(x <= 0):
	print(x, " cannot be negative or zero")
else:
	Lab04_module.twoInput(x, y)

Lab04_module.generate_password("usman")
