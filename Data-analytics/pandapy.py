import pandas as pd
import numpy as np
#pandas main teen data structures hai: Series, DataFrame, Panel
#Series is a 1D array
#DataFrame is a 2D array
#Panel is a 3D array

# Creating a pandas Series
s1 = pd.Series([1,2,3,4,5])
print(s1)

# Creating a pandas Series with custom index
s2 = pd.Series([1,2,3,4,5], index=["a","b","c","d","e"])
print(s2)

# Creating a pandas Series from a dictionary
s3 = pd.Series({"a":1,"b":2,"c":3,"d":4,"e":5})
print(s3)

# Creating a DataFrame
data = pd.DataFrame({
    "Name":["Anubhav","Aryan","Anu"],
    "Marks":[100,99,98],
    "Age":[20,21,22]
})

# Calculating the mean of the 'Marks' column
mean = np.mean(data["Marks"])
print("Mean of Marks is: ", mean)

# Creating a numpy array using arange
arng = np.arange(1,100,2)
print(arng)

# Demonstrating slicing in numpy arrays
print(arng[-4:-1])  # Last three elements
print(arng[-1:-4:-1])  # Last three elements in reverse order

# Creating a DataFrame from a list
test = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame(test)

# Displaying the first and last 5 rows of the DataFrame
print(df.head())
print(df.tail())

# Displaying the shape and columns of the DataFrame
print(df.shape)
print(df.columns)

# Displaying the first row and first 3 rows of the DataFrame
print(df.iloc[0])
print(df.iloc[0:3])

# Reshaping the DataFrame into a 1D array and displaying it
print(df.values.reshape(-1))#-1 ka matlab hai ki jitne bhi rows ho utne hi columns ho aur vice versa

# Getting and displaying descriptive statistics of the DataFrame
stats = df.describe()
print(stats)
print(df.info())#this will give the info about the dataframe jaise ki kitne rows hai, kitne columns hai, kitne non null values hai etc.

# Reshaping the DataFrame into a 1D array and converting it back into a DataFrame
melted = df.melt()
print(melted)
print(melted.pivot(columns="variable", values="value"))

# Removing duplicate rows from the DataFrame
print(df.drop_duplicates())

# Creating a DataFrame for the industry.csv file
industry_df = pd.DataFrame({
    "Industry": ["Industry1", "Industry2", "Industry3"],
    "Value": [100, 200, 300]
})

# Displaying the first element of the 'Industry' column
print(industry_df["Industry"][0])

# Displaying the first 3 rows and first 2 columns of the DataFrame
print(industry_df.iloc[0:3,[0,1]])

# Displaying the first 3 rows and first and second column of the DataFrame in array form
print(industry_df.iloc[0:3,[0,1]].values)

# Displaying the shape of the array
print(industry_df.iloc[0:3,[0,1]].values.shape)

# Displaying the array in 1D form
print(industry_df.iloc[0:3,[0,1]].values.reshape(-1))

# Getting descriptive statistics of the DataFrame including all columns
info= industry_df.describe(include="all")
print(info)
numbers =[1,2,3,4,5,6,7,8,9,10]
df2 = pd.DataFrame(numbers)
#odds = df2.apply(numbers,lambda x:x%2==1 )# ye galat hai because apply function is used to apply a function on a dataframe
odds = df2.apply(lambda x:x%2==1 )
print(odds)
# Removing duplicate values from the 'Industry' column and keeping the last occurrence
print(industry_df.drop_duplicates(subset=["Industry"],keep="last"))

# Adding 1 to each value in the 'Value' column
print(industry_df["Value"].apply(lambda x:x+1))

# Adding a comma after each value in the 'Value' column
print(industry_df.apply(lambda x:str(x)+","))

# Adding a new column 'Percentage' to the DataFrame
print(industry_df.assign(Percentage=lambda x:x["Value"]*0.1))

# Removing the 'Value' column from the DataFrame
print(industry_df.drop("Value",axis=1))#axis=1 means column and axis=0 means row
print(industry_df.drop("Value",axis=1,inplace=True))#inplace=True means that the changes will be made in the original dataframe
df3 = pd.DataFrame({"Marks":[100,20,98,97,96,95,31,93,92,91,90]})
print(df3)
df3["result"] = df3["Marks"].apply(lambda x:"Pass" if x>33 else "Fail")
print(df3)
print(df3["result"].value_counts())  #value_counts() function is used to count the number of unique values in a column
print(df3["result"].value_counts(normalize=True)) #normalize=True means that the values will be displayed in percentage
print(df3["result"].value_counts(normalize=True)*100) #ye percentage me dikhayega result ko
mean = 0 #apne aap ko 0 se compare karega
std_dev = 1  #apne aap ko 1 se compare karega
variance = np.square(std_dev)  #variance is the square of standard deviation
for _ in range(2):
    values_mean_std_dev = np.random.normal(mean, std_dev, 5)
    print(values_mean_std_dev)
values = variance*np.random.randn(5)
print(values)
