class Person:
	def __init__(self, name, age, gender, location):
		self.__name = name
		self.__age = age
		self.__gender = gender
		self.__location = location

	def increaseAge(self):
		self.__age += 1
	
	def getName(self):
		return self.__name
	def getAge(self):
		return self.__age
	def getGender(self):
		return self.__gender
	def getLocation(self):
		return self.__location
	def setLocation(self, location):
		self.__location = location
	def __repr__(self):
		return "Name: " + self.__name + "\nAge: " + (str)(self.__age) +  "\nGender: " + self.__gender + "\nLocation: " + self.__location + "\n"
