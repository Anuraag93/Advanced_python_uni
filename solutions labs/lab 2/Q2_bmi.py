# Question 2
# Write a program that reads wight in kilograms (an int)
# and height in cms (an int). The program then calculate
# the bmi value
weight = int(input("Enter the weight in kilograms: "))
height = int(input("Enter the height in cms: "))

heightInMeters = height / 100

bmi = weight / heightInMeters ** 2

print("bmi:", bmi)

