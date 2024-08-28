import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data=sns.load_dataset("tips")
print(sns.get_dataset_names())
df = sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=data,hue='sex',style='time',size='size')

plt.show()
sns.relplot(x="total_bill",y="tip",data=data,kind='scatter')
plt.show()
# data2 = pd.read_csv("gap.csv")
# tempdf= data2[data2["country"]=="India","Bangladesh","Pakistan","Sri Lanka","Nepal","Bhutan","Maldives"]
#
# sns.relplot(x="year",y="lifeExp",data=tempdf,kind='line',hue='country',style='country',col='country',col_wrap=3)
# plt.show()
sns.relplot(x="total_bill",y="tip",data=data,kind ="scatter",hue="sex",row='sex',col='smoker')
plt.show()

'''The relplot function in Seaborn is a figure-level function for visualizing statistical relationships using two common approaches: scatter plots and line plots.  
Scatter plots: These are used when you want to show the relationship between two variables. Scatter plots represent each relationship of two data points with a dot.  
Line plots: These are used to display data or information in a time series. Line plots can be helpful in comparing multiple variables by drawing multiple lines on the same graph. '''


#distribution plot, 1. kde plot 2. hist plot 3. rug plot
# figure level are relplot, pairplot, jointplot, catplot
#axes level are scatterplot, lineplot, histplot, kdeplot, ecdfplot, rugplot, displot, lmplot, regplot, residplot, heatmat, clustermap, boxplot, violinplot, stripplot, swarmplot, pointplot, barplot, countplot, catplot
#kde plot is used to visualize the probability density of a continuous variable. It is used to estimate the probability density function of a continuous random variable.

sns.kdeplot(data["total_bill"])
plt.show()
sns.histplot(data["total_bill"],kde=True)
plt.show()
sns.rugplot(data["total_bill"])
plt.show()
sns.kdeplot(data['total_bill'])
plt.show()
#pairplot is used to plot pairwise relationships in a dataset. The pairplot function creates a grid of Axes such that each variable in the data will be shared in the y-axis across a single row and in the x-axis across a single column.
#plots under the diagonal are scatter plots and the plots on the diagonal are histograms
#plots under distribution plot are kde plot, hist plot and rug plot
sns.pairplot(data)
plt.show()
gap = pd.read_csv("gap.csv")
temp_df = gap.pivot(index="country",columns="year",values="lifeExp")
plt.figure(figsize=(10,6))
sns.heatmap(temp_df)
#heatmap comes under the category of axes level plot, heatmap is used to plot the rectangular data as a color-encoded matrix
# #clustermap is used to plot a matrix dataset as a hierarchically-clustered heatmap
# df5 = pd.read_csv("Iris.csv")
# sns.clustermap(df5.iloc[:,1:5],cmap="coolwarm",standard_scale=1)
# plt.show()
#boxplot is used to visualize the distribution of a continuous variable. It is used to identify the mean, median, and quartiles of the data.
#violin plot is used to visualize the distribution of a continuous variable. It is used to identify the mean, median, and quartiles of the data.
#stripplot is used to visualize the distribution of a continuous variable. It is used to identify the mean, median, and quartiles of the data.
#swarmplot is used to visualize the distribution of a continuous variable. It is used to identify the mean, median, and quartiles of the data.
sns.boxplot(data=data,x="sex",y="tip")
plt.show()
sns.violinplot(x="day",y="total_bill",data=data)
plt.show()
sns.stripplot(x="day",y="total_bill",data=data)
plt.show()

sns.swarmplot(x="day",y="total_bill",data=data)
plt.show()


