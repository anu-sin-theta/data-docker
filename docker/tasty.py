import pandas as pd
import numpy as np
data = pd.DataFrame({"Name":["Anubhav","Aryan","Anu"],
                     "Marks":[100,99,98],
                        "Age":[20,21,22]})
mean = np.mean(data["Marks"])
print(data)
print("Mean of Marks is: ",mean)