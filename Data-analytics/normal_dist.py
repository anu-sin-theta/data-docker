#measure of central tendency plot
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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
arr2= np.array([40,10,20,50,80,60,200,70])
#variance is the average of the squared differences from the mean
#standard deviation is the square root of the variance
print(np.var(arr2))
print(np.std(arr2))
print(max(arr2)-min(arr2))
print(np.std(arr2)/np.mean(arr2))
#plot histogram
plt.hist(arr2,bins=5)
plt.show()
plt.boxplot(arr2)
plt.show()
data = pd.DataFrame(arr2,arr)
sns.pairplot(data)
