'''
Exercises from https://www.practicepython.org/ - Exercise 1
This program asks the user for their age and caluclates the year they will turn 100
'''
age = int(input("How old are you? "))
year = 2021
byear = year - age
print ("You were born in", byear ,"and are ", age ,"years old.")
year100 = byear + 100
print ("In", year100, "you will be 100 years old" )

#Additional exercises

i=3
while i > 0:
    repeat = int(input("Please give me a number between 1 and 10 "))
    if repeat <= 10:
        for i in range(repeat):
            print ("In", year100, "you will be 100 years old")
            i=0
    else:
        i -= 1
        print("Your number is not within range")
