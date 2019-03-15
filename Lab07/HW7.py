from guy import Person

def getByLocation(loc, myList):
	newList = []
	for ps in myList:
		if (ps.getLocation() == loc):
			newList.append(ps)

	return newList

def getByGender(gend, myList):
	newList = []
	for ps in myList:
		if (ps.getGender() == gend):
			newList.append(ps)
	
	return newList

myFile = open("input.txt", "r")
myPersons = []
for x in myFile:
	i = x.find(",")
	name = x[:i]
	i = x.find(",",i + 1)
	age = x[len(name) + 1:i]
	i = x.find(",",i + 1)
	gender = x[len(name) + len(age)+ 2 : i]
	location = x[i + 1 : -1]
	myPersons.append(Person(name,age,gender,location))

newList = getByLocation("ankara", myPersons )
newList = getByGender("female", newList)

print(newList)
