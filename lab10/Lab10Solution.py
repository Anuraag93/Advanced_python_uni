# Task 1: Read and manipulate CSV data using the Python Panda library
import pandas as pd
# Read the Cars.csv file
df = pd.read_csv('Cars.csv')
# View data
print (df.head())
print (df.info())
#Display the number of columns and rows
print (df.shape)
# Check if there are missing or empty cells
print (df.isnull().sum())
# Replace the missing values of each column with the mean value of this column
# here is an exampl for the mpg column ... use same code for other column 
m1=df['mpg'].mean()
print (m1)
df["mpg"].fillna(m1, inplace = True)
print (df.head())

# Print the Cumulative product of values.
print (df.cumprod)

# Save the min, max, sum, std and median of each column in a dictionary.
# here is an example for one column
mpg={'min':df['mpg'].min(), 'max':df['mpg'].max(),'sum':df['mpg'].sum(),'std':df['mpg'].std(),'median':df['mpg'].median()}
print (mpg)

#Print the summary statistics of the data.
print ("\n \n --- Print the summary statistics of the data --- \n \n .")
print (df.describe)




#Task 2: Visualise the CSV data using the Python Matplotlib library


import pandas as pd
import matplotlib . pyplot as plt
# Read the Cars.csv file
df = pd.read_csv('Cars.csv')
# View data
print (df.head())
print (df.info())
#Display the number of columns and rows
print (df.shape)
# Check if there are missing or empty cells
print (df.isnull().sum())
# Remove the missing values
df.dropna(inplace = True)
print(df.to_string())
print (df.shape)
print (df.shape[0])
x=[i for i in range (df.shape[0])]
print (x)

# Plot the lines of all columns, e.g., one line for each column
plt.plot(x, df["mpg"])
plt.plot(x, df["cyl"])
plt.plot(x, df["disp"])
plt.plot(x, df["hp"])
plt.plot(x, df["wt"])
plt.plot(x, df["drat"])
plt.plot(x, df["qsec"])
plt.plot(x, df["vs"])
plt.plot(x, df["am"])
plt.plot(x, df["gear"])
plt.plot(x, df["carb"])

plt.show()

# Plot mpg vs cyl
plt.plot(df["mpg"], df["cyl"])
plt.show()
#Plot gear vs carb
plt.plot(df["gear"], df["carb"])
plt.show()


# Plot the lines of all columns using different colors and shapes
marker = ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd', 'ok']
i=0
for col in df.columns:
    plt.plot(x, df[col], marker[i])
    i=i+1
plt.show()

# Create the histogram of all columns
for col in df.columns:
    n, bins , patches = plt . hist (df[col], 3, density =1, facecolor ='g', alpha =0.75)

plt.show()

 # or if the above is not clear 
n, bins , patches = plt . hist (df["mpg"], 3, density =1, facecolor ='g', alpha =0.75)

plt.show()