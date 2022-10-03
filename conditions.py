temp = int(input("Please input a temperature"))
print ("The new temp is : ", temp)
if temp > 90:
    print ("Wear Shorts")
elif temp > 70 and temp < 90:
    print ("Short sleeves are fine")
elif temp > 50 and temp < 70:
    print ("Wear a Jacket")
elif temp > 32 and temp < 50:
    print ("Wear a heavy coat")
else:
    print ("Stay Inside")

