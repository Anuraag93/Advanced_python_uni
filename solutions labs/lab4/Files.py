# --- File Input-Output ---
# Question 1- Review
# a.	
# –	What are the main steps we follow in writing text to a file? 
# –	What are the functions/methods we use for these steps? 
# –	Illustrate the writing process with a simple but complete example.
# Step 1: open file with mode "w"

file=open("fileName.txt", "w")
# Step 2: write to file
file.write (string)
# Step 3: Close the file
file.close()


# b.	Suppose we open a file for writing. What happens if the file does not exist? What happens if the file already exists? 
# c.	
# –	What are the main steps we follow in reading text from a file? 
# –	What are the functions/methods we use for these steps?
# –	Illustrate the reading process with a simple example in which we read the entire contents of the file into a string.

# Step 1: open file with mode "r"
file=open("fileName.txt", "r")
# Step 2: read data from file
string=file.read ()
# Step 3: Close the file
file.close()


# d.	
# –	How do we open a file to append text to? 
# –	What happens if the file does not exist?
# –	What happens if the file already exists?


# Step 1: open file with mode "a"
file=open("fileName.txt", "a")
# Step 2: write to file
file.write (string)
# Step 3: Close the file
file.close()





# Question 2 - Copy Files
# a.	Write a program to copy a file to another file. Let the input file be twinkle.txt (provided), and the output file is twinkle_copy1.txt.
inputFile = open("twinkle.txt")
outputFile = open("twinkle_copy1.txt", "w")

contents = inputFile.read()
outputFile.write(contents)

inputFile.close()
outputFile.close()

print("done")



# b.	Write a program to copy a file to another file, with each line of text being preceded by the line number, followed by a colon. Start the line numbers at 1. 
#Let the input file be twinkle.txt and the output file be twinkle_copy2.txt

infile = open("twinkle.txt","r")
outfile = open("twinkle_copy2.txt", "w")
lines = infile.readlines()
for n in range(len(lines)):
    outfile.write(str(n+1) +": " + lines[n])
infile.close()
outfile.close()
print("done")



# Question 3 - Merge Files
# Write a program to merge the two files. The files names set1.txt and names set2.txt are provided. 
# Each file has 30 names, each of which is on a line of its own. The names in each file are sorted. The two files have names in common. 
# The program is to merge the two files and save the merged list in the output file names merged.txt. 

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






# Question 4 - Finding Common Words
# Write a program that reads two files and print out all the words they have in common. 
# For this question, take a word as a sequence of characters separated by whitespace characters. 
# For a quick test, you can take names set1.txt and names set2.txt as input files. Print out all the words they have in common.

infile1 = open("names_set1.txt")
infile2 = open("names_set2.txt")

text1 = infile1.read()
wordList1 = text1.split()

text2 = infile2.read()
wordList2 = text2.split()

for i in wordList1:
    for j in wordList2:
        if i==j:
            print("commonWords", i)

infile1.close()
infile2.close()




# Question 5 -Word Frequencies
# Write a program to read a text file and print the frequencies (how many times this word occurs) of each word. To keep things simple, take all the words to be in lower case. 
# We will take a word as a sequence of letters separated by whitespace character and the following punctuation marks: comma, colon, semi-colon, period, question mark, exclamation mark, and quotation marks. 
# For a quick test, use the provided file why.txt for input.




# open and read the contents of the whole file into a string
infile = open("why.txt")
text = infile.read()

# one way to make the punction marks to be the string to
# separate the tokens is to replace the punction marks
# with the blank character
for ch in ".,?!;:\"'":
    text = text.replace(ch, " ")

# get the list of tokens
tokenList = text.split()

# some tokens may contain non-letter characters.
# We want to remove those tokens
# We also convert the words to lower case
wordList =""
for e in tokenList:
    if e.isalpha():
        wordList=wordList+e.lower()


for i in wordList:
    c=wordList.count(i)
    print ("count ", c)
