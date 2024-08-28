# import pandas as pd
import pandas as pd
import seaborn as sns
# data = pd.read_csv("train.csv")
#
# print(data.head())
# print(data.describe())
# print(data.info())
# print(data.columns)
# print(data.shape)
# print(data.isnull().sum())
# print(data["Age"].mean())
# print(data["Age"].median())
# #this data is of titanic dataset
# print(pd.crosstab(data["Survived"],data["Embarked"],normalize="columns")*100)
# print(pd.crosstab(data["Survived"],data["Pclass"],normalize="columns")*100)
# print(pd.crosstab(data["Survived"],data["Sex"],normalize="columns")*100)
# print(pd.crosstab(data["Survived"],data["SibSp"],normalize="columns")*100)
# print(pd.crosstab(data["Survived"],data["Parch"],normalize="columns")*100)
# print(pd.crosstab(data["Sex"],data["Embarked"],normalize="columns")*100)
# print(data["SibSp"].value_counts())
# #feature engineering for calculating individual fare
# data["individual_fare"] = data["Fare"]/data["SibSp"] + data["Parch"] + 1
# print(data["individual_fare"])
# #feature engineering for calculating family size
# data["family_size"] = data["SibSp"] + data["Parch"] + 1
# print(data["family_size"])
# #feature engineering for calculating age group
# data["age_group"] = pd.cut(data["Age"],bins=[0,18,30,50,100],labels=["children","young","middle_aged","old"])
# print(data["age_group"])
# #feature engineering for calculating fare group
# data["fare_group"] = pd.cut(data["Fare"],bins=[0,50,100,200,300,600],labels=["low","medium","high","very_high","extreme"])
# print(data["fare_group"])
# #feature engineering for calculating title
# data["title"] = data["Name"].apply(lambda x: x.split(",")[1].split(".")[0])
# print(data["title"])
#
# #data visualization
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.countplot(data["Survived"])
# plt.show()
# sns.countplot(data["Pclass"])
# plt.show()


import numpy as np
arr = [40,20,20,60,80,60,20,60]
print(np.mean(arr))
print(np.median(arr))
mode = max(set(arr), key = arr.count)
print(mode)
q1 = np.percentile(arr,25)
q3 = np.percentile(arr,75)
iqr = q3 - q1
print(iqr)
lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr
print(lower_whisker)
print(upper_whisker)
outliers = []
for i in arr:
    if i<lower_whisker or i>upper_whisker:
        outliers.append(i)
print(outliers)
arr2= np.array([40,20,20,60,80,60,20,60])
#variance is the average of the squared differences from the mean
#standard deviation is the square root of the variance
print(np.var(arr2))
print(np.std(arr2))
print(max(arr2)-min(arr2))
print(np.std(arr2)/np.mean(arr2))
#plot histogram
import matplotlib.pyplot as plt
plt.hist(arr2,bins=5)
plt.show()
plt.boxplot(arr2)
plt.show()
data = pd.DataFrame(`arr2,arr)
sns.pairplot(data)














