import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Iris.csv")
coulmns= df.columns
print(coulmns)
#printing specific columns
print(df[["Id","Species"]])
#to print the first 5 rows of the dataframe
print(df.head())
#ploting the data
plt.scatter(df["SepalLengthCm"],df["SepalWidthCm"])
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
plt.show()
#to print the unique values of a column
print(df["Species"].unique())
#to print the count of unique values of a column
print(df["Species"].value_counts())
#to print the mean of a column
print(df["SepalLengthCm"].mean())
#coloring the data points
plt.scatter(df["SepalLengthCm"],df["SepalWidthCm"],c="r")
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
plt.show()
#to print the correlation matrix
# Select only the numerical columns
numerical_df = df.select_dtypes(include=[np.number])

# Calculate the correlation
print(numerical_df.corr())#to print the covariance matrix
print(numerical_df.cov())
#to print the standard deviation of the dataframe
print(numerical_df.std())
#to print the variance of the dataframe
print(numerical_df.var())
#to print the descriptive statistics of the dataframe
print(df.describe())
#plotting values in different colors
plt.scatter(df["SepalLengthCm"],df["SepalWidthCm"],c=df["PetalLengthCm"]) #c is used to color the data points according to the values of the column
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
plt.show()
#plotting histogram, histo gram aur bar plot me difference ye hai ki histogram me frequency of the unique values of a column ko plot kiya jata hai aur bar plot me unique values of a column ko plot kiya jata hai
#matplotlib me histogram ko plot karne ke liye hist() function ka use kiya jata hai
df["SepalLengthCm"].hist()
plt.show()
#plotting histogram with bins
df["SepalLengthCm"].hist(bins=50)
plt.show()
#plotting histogram with different colors
df["SepalLengthCm"].hist(bins=50,color="r")
plt.show()
#plotting histogram with different colors and labels
df["SepalLengthCm"].hist(bins=50,color="r")
plt.xlabel("SepalLengthCm")
plt.ylabel("Frequency")
plt.show()
# plotting each coulmn with different color
# Scatter plot for SepalLengthCm and SepalWidthCm
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"], c="r")
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")
plt.show()

# Scatter plot for PetalLengthCm and PetalWidthCm
plt.scatter(df["PetalLengthCm"], df["PetalWidthCm"], c="g")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.show()
#bar plot is used to plot the frequency of the unique values of a column unique values of a column in the form of bars
df["Species"].value_counts().plot(kind="bar",color=["orange","blue","black"],label="Species")
plt.xlabel("Species")
plt.ylabel("Frequency")
plt.show()
# Scatter plot for SepalLengthCm and SepalWidthCm
plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"], c="r", label="Sepal")
plt.xlabel("SepalLengthCm")
plt.ylabel("SepalWidthCm")

# Scatter plot for SepalLengthCm and PetalLengthCm
plt.scatter(df["SepalLengthCm"], df["PetalLengthCm"], c="g", label="Petal")
plt.xlabel("SepalLengthCm")
plt.ylabel("PetalLengthCm")

# Scatter plot for SepalWidthCm and PetalLengthCm
plt.scatter(df["SepalWidthCm"], df["PetalLengthCm"], c="b", label="Sepal vs Petal")

plt.legend()
plt.show()
#plotting the box plot boxplot is used to plot the distribution of the values of the columns for example the minimum value, first quartile, median, third quartile and maximum value
df.boxplot(column=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"])
plt.show()
batdf = pd.read_csv("batter.csv")
#selecting 50 top players randomly

