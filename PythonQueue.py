##List of names
names = []
##For loop asking for 10 names
for x in range(10):
    ##Asks for names 10 times
    acceptedName = input("Enter name: ")
    ##Puts all 10 names individually in list
    names.append(acceptedName)

print(names)

##Uses the length of the list(10) to individually print each name
for x in range(len(names)):
    ##Print the list
    print(names.pop(0))
