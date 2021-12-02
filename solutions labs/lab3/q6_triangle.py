s1, s2, s3 = 10, 20, 15
s1, s2, s3 = 10, 20, 5
s1, s2, s3 = 10, 20, 10
maxSide=0

if s1 >= s2:
    maxSide = s1
else:
    maxSide = s2

if s3 > maxSide:
    maxSide = s3

sumOfOtherTwo = s1 + s2 + s3 - maxSide

if maxSide < sumOfOtherTwo:
    print("triangle")
else:
    print("not triangle")
