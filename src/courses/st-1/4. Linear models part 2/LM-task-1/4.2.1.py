import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib

matplotlib.use('TkAgg')

sns.set()

df = pd.read_csv('src/courses/st-1/4. Linear models part 2/LM-task-1/satgpa.csv')
df.drop('sex', axis=1, inplace=True)
df.drop('sat_v', axis=1, inplace=True)
df.drop('sat_m', axis=1, inplace=True)

sat = df['sat_sum']  # x
hs_gpa = df['hs_gpa']  # y
fy_gpa = df['fy_gpa']  # y


def build_simple_model(x, y, label_x, label_y):
    plt.scatter(x, y)
    plt.xlabel(xlabel=label_x, )
    plt.ylabel(ylabel=label_y)
    linear_regression = sm.add_constant(x)
    results = sm.OLS(y, linear_regression).fit()
    coefficients = results.params
    y_hat = coefficients['const'] + (coefficients['sat_sum'] * x)
    plt.plot(x, y_hat, color='red', linestyle='--', linewidth=2, marker='o', markersize=5, label='Regression Line')
    plt.show()


build_simple_model(sat, hs_gpa, 'SAT', "hs_gpa")
build_simple_model(sat, fy_gpa, 'SAT', "fy_gpa")
