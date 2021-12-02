s = "abcdef"
s = "strings"
numOfStar = len(s) - 3
print(f'{s[0:2]}{"*" * numOfStar}{s[-1]}')