# Q14

# A
# Build the letter-to-words dictionary

# Read the contents into a list of strings which contain
# newline characters
file = open("words_3000.txt")
lines = file.readlines()

# Construct the list of words by striping off whitespace
# characters
words = []
for line in lines:
    words.append(line.strip())
    
# Buil the dictionary
# First initialise the dictionary
# Initially, the values are empty sets
mapping = dict()
for code in range(ord("a"), ord("z") + 1):
    mapping[chr(code)] = set()

# Then fill the set up with words
for letter in mapping:
    for word in words:
        if letter in word.lower():
            mapping[letter].add(word)

# quick test
# print(mapping['z'])

# B

# take "hat" as an example first
s1 = mapping["h"]
s2 = mapping["a"]
s3 = mapping["t"]
ans = s1.intersection(s2).intersection(s3)
print("Words that contain letter of 'hat':")
print(ans)

# general solution - consider a string s
# take for example
s = "cat"
ans = mapping[s[0]]
for i in range(1, len(s)):
    ans = ans.intersection(mapping[s[i]])

print("\nWords containing letters of 'cat':")
print(ans)
