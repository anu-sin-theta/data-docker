import numpy
import pandas
from matplotlib import pyplot as plt
df = pandas.read_csv("batter.csv")
plt.scatter(df["avg"],df["runs"])
plt.xlabel("Average")
plt.ylabel("Runs")
plt.show()
fig = plt.figure() #to create a figure
#to create a subplot
#subplot me 3 arguments pass kiye jate hai, pehla argument rows, doosra argument columns, teesra argument subplot number
#subplot number 1 se start hota hai
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(df["avg"],df["runs"],c="g")
ax1.set_xlabel("Average")
ax1.set_ylabel("Runs")
#
fix,ax = plt.subplots(nrows=2,ncols=2,figsize=(10,6), sharex=True) #10,6 represents the width and height of the plot
# ax is the object of the plot difference between plt and ax is that ax is used to set the properties of the plot
ax1.scatter(df["avg"],df["runs"],c="r")
ax1.set_xlabel("Average")
ax1.set_ylabel("Runs")
plt.show()
#

# ax[1, 0] represents the second subplot
ax[1, 0].scatter(df["avg"],df["runs"],c="b")
ax[1, 1].set_xlabel("Average")
ax[0, 0].set_ylabel("Runs")
#
plt.show()
#3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["avg"],df["runs"],df["strike_rate"],c=df["avg"])
ax.set_xlabel("Average")
ax.set_ylabel("Runs")
ax.set_zlabel("strike_rate")
plt.show()
# 2d x,y,z
x = numpy.linspace(2, 100, 100)
y = numpy.linspace(2, 100, 100)
x, y = numpy.meshgrid(x, y)
z = numpy.sin(numpy.sqrt(x**2 + y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c=z)
p = ax.plot_surface(x, y, z, rstride=8, cstride=8, alpha=0.3, cmap="Blues")
plt.show()