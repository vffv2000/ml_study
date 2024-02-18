# https://stepik.org/lesson/878851/step/9?unit=883402
import numpy as np
import pandas as pd

data = '33 65 nan 86 26 86 63 4 19 70 27 4 16 72 93 20 41 49 53 67 45 nan nan 69 89 nan 52 53 8 90 nan 2 3 nan 6 74 61 21 42 47'
data = data.split(" ")
data = np.array(data).reshape(20, 2)
df = pd.DataFrame(data=data, columns=["value1", "value2"], index=["obj_1", "obj_2"]*10)
df = df.applymap(lambda x: np.nan if x == "nan" else float(x))

# Your code here

mean_values = df.groupby(df.index).mean()

v1o1 = mean_values['value1']['obj_1'].mean().round(2)
v1o2 = mean_values['value1']['obj_2'].mean().round(2)
v2o1 = mean_values['value2']['obj_1'].mean().round(2)
v2o2 = mean_values['value2']['obj_2'].mean().round(2)


for column in df.columns:
    df[column] = df.groupby(df.index)[column].transform(lambda x: x.fillna(x.mean().round(2)))
df.index.name = 'index'
print(df)