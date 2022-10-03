average = 0
total = 0
howMany = int(input("How many test scores would you like to average?"))
howManyEntered = howMany
while (howMany > 0):
    testScore = int(input("Enter testScore"))
    howMany -= 1
    total += testScore

average = total / howManyEntered
print ("The average for the test scores you entered is: ", average)

