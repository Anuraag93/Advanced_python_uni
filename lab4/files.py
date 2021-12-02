

# 1. Open
# 2. Read/write
# 3. Close

# s="Some Text2"
# file = open('string.txt','a')
# file.write(s)
# file.close()
# file = open('string.txt','r')

# text = file.read()
# file.close()
# # print(text)


# # q2
# p = "Twinkle File"
# file = open("twinkle.txt", 'r')
# t = file.read()
# file.close()


# file = open("twinkle_copy1.txt",'w')
# file.write(t)
# file.close()

# inputFile = open('twinkle.txt','r')
# outputFile = open('twinkle_copy2.txt','w')
# t = inputFile.readlines()

# for i in range(len(t)):
#     outputFile.write(f'{i+1}: {t[i]}')
# inputFile.close()
# outputFile.close()

# fname = "names_set1.txt"
# i = open(fname,'w')
# i.write('abc\nbcd\ncde\ndef\nefg')
# i.close()
# fname = "names_set2.txt"
# i = open(fname,'w')
# i.write('abadsfafadfc\nbcafasdfadfadfd\ncasdfadfade\ndeadfasdfasff\nefadfadfg')
# i.close()
#q3
fname = "names_set1.txt"
infile1 = open(fname)

fname = "names_set2.txt"
infile2 = open(fname)

fname = "names_merged.txt"
outfile = open(fname, "w")

list1 = infile1.readlines() 
list2 = infile2.readlines()

mergeList = (list1 + list2)
for word in mergeList:
    outfile.write(word)

infile1.close()
infile2.close()
outfile.close()

print("done")