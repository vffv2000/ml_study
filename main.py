import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

df = pd.read_csv('source_data/simple_data_for_linear_regression.csv',
                 index_col='Unnamed: 0')

print(df.head(10))
target_x = df.drop('Target', axis=1)
target_y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(target_x, target_y, test_size=0.25, random_state=1)
