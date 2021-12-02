# Q11

# Read weight of an egg and classifies it as small (< 55),
# med (55 to 65) or large (> 65)

weight = 60
weight = 50
weight = 75

weight = 65

if weight < 55:
    grade = "small"

elif weight <= 65:
    grade = "mdium"

else:
    grade = "large"

print(weight, grade)
