# Q15
# Translate text message

# Read the words

filename = "abbreviations.txt"
infile = open(filename)
lines = infile.readlines()

# inspect
# for i in range(10):
#    print(lines[i].__repr__())


# Build dictionary
mapping = dict()
for line in lines:

    "Extract the required key and value from each line"
    temp = line.split(":")
    key = temp[0].strip()
    value = temp[1].strip()
    print(key, "->", value)

    "Now add the key-value pair to the dictionary"""

# Translate texting message
"""
Extract the words (tokens) from the texting message
Look up the dictionary to construct the plain English message

y r u l8
"""



