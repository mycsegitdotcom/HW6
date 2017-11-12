# Yosua Oey, Tuesday 1pm
# CSE 3 Fall 2017, Homework 6
# Loops.py: Explores loops in Python
'''
dogs = ["Shiba Inu", "Corgi", "Golden Retriever", "Daschund", "Siberian Husky"]

for dog in dogs:
	print(dog)

countDog = 0
for dog in dogs:
	countDog += 1
print("I have", str(countDog), "favorite pets!")

print("My favorite pets are:")
for dog in dogs:
	print("\t" + dog)

userAnswer = raw_input("What is your favorite pet? ")
if (userAnswer in dogs):
	print("I like " + userAnswer + " too!")
else:
	print(userAnswer + " are not that cute.")

food = ["Ramen", "Boba", "Burger", "Pizza"]

foodCount = 0
for i in food:
	foodCount += 1
print("I have", str(foodCount), "favorite food!") # Printed like ("I have", 4, "favorite food!"), might have to fix!

print("My favorite food includes:")
for i in food:
	print("\t " + i)

userInput = raw_input("What is your favorite food? ")
if (userInput in food):
	print("Hey, that's pretty good!")
else:
	print("Oh ok")
'''
# Yosua Oey, Tuesday 1pm
# CSE 3 Fall 2017, Homework 6
# Functions.py: Explores function in python.

loopCount = 0
for iteration in range(5):
	loopCount += 1
print("I looped", str(loopCount), "times.")

def loop(number):
	loopCounts = 0
	for iteration in range(number):
		loopCounts += 1
	return loopCounts

print("I looped", loop(0), "times.")
print("I looped", loop(4), "times.")
print("I looped", loop(5), "times.")
print("I looped", loop(100), "times.")