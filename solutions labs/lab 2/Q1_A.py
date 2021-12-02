# Question 1
# Part A
# Write a program to calculate the volume of a can of soft drink
# with diameter cm and height = 10 cm


diameter = int(input("Enter diameter: "))
height = int(input("Enter height: "))



pi=3.14

area = (1/4) * pi * diameter ** 2

volume = area * height

print("volume:", volume)
