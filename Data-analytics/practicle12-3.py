import matplotlib.pyplot as plt
import pandas as pd
data = pd.DataFrame({"months":["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],"sales":[100,20,300,400,500,450,700,800,900,1000,1060,1200]})
plt.bar(data["months"],data["sales"])
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.barh(data["months"],data["sales"])
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.bar(data["months"],data["sales"],color="r")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()
plt.plot(data["months"],data["sales"])
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()


