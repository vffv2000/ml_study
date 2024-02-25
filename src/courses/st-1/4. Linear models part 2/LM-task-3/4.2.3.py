import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import statsmodels.api as sm
import matplotlib

matplotlib.use('TkAgg')

sns.set()

data = pd.read_csv('source_data/college-admissions.csv')
y = data['admitted']
x1 = data['sat.score']

plt.scatter(x1, y, color='blue')
plt.xlabel("SAT Score")
plt.ylabel("Admitted")

x = sm.add_constant(x1)
reg_log = sm.Logit(y, x)
results_log = reg_log.fit()

# Corrected logistic function definition
def f(x, b0, b1):
    z = b0 + b1*x
    return np.exp(z) / (1 + np.exp(z))

# Use the correct attribute .params to access the model parameters
f_sorted = np.sort(f(x1, results_log.params[0], results_log.params[1]))
x_sorted = np.sort(np.array(x1))

plt.figure(figsize=(10, 6))  # Optional: Adjust the figure size
plt.scatter(x1, y, color='red', label='Data')
plt.plot(x_sorted, f_sorted, color='green', label='Logistic Regression Fit')
plt.xlabel("SAT Score")
plt.ylabel("Admitted")
plt.legend()
plt.show()

print(results_log.summary())
