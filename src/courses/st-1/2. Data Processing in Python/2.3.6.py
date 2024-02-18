# https://stepik.org/lesson/878851/step/8?unit=883402
import pandas as pd
import numpy as np

data = np.array(input().split(" "))
data = data.reshape(10, 10)
df = pd.DataFrame(data)
df = df.astype(float)


def minmax_normalize_and_round(column):
    min_value = column.min()
    max_value = column.max()
    normalized = (column - min_value) / (max_value - min_value)
    return normalized.round(2)


df_normalized = df.apply(minmax_normalize_and_round)

df_normalized['mean'] = df_normalized.mean(axis=1).round(2)
df_normalized.loc['sum'] = df_normalized.sum().round(2)

print(df_normalized)
