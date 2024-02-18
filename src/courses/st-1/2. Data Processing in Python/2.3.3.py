import numpy as np
import pandas as pd

# Обработка входных данных
data = input()        
data = data.split(" ")
data = np.array(data).reshape(20, 2)
df = pd.DataFrame(data=data, columns=["value1", "value2"], index=["obj_1", "obj_2"]*10)
df = df.applymap(lambda x: np.nan if x == "nan" else float(x))

# Your code here
# Your code here
# 33 65 nan 86 26 86 63 4 19 70 27 4 16 72 93 20 41 49 53 67 45 nan nan 69 89 nan 52 53 8 90 nan 2 3 nan 6 74 61 21 42 47
print(df)