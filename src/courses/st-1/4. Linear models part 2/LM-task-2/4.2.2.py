import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib

matplotlib.use('TkAgg')

sns.set()

df = pd.read_csv('src/courses/st-1/4. Linear models part 2/LM-task-2/data.csv')
df['Attendance'] = df['Attendance'].map({"Yes": 1, "No": 0})

y = df['GPA']
x1 = df.drop('GPA', axis=1)

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()

coefficients = results.params
# const         0.643850
# SAT           0.001400
# Attendance    0.222644
# dtype: float64
y_hat_no = coefficients['const'] + coefficients['SAT'] * df['SAT']

y_hat_yes = (coefficients['const'] + coefficients['Attendance']) + coefficients['SAT'] * df['SAT']

plt.scatter(df['SAT'], y)
plt.scatter(df['SAT'], df['GPA'], c=df['Attendance'], cmap='RdYlGn_r')

plt.plot(df['SAT'], y_hat_yes, lw=2, color='#00FF00')
plt.plot(df['SAT'], y_hat_no, lw=2, color='#FF0000')

plt.show()

new_data = pd.DataFrame({'const': 1, 'SAT': [1700, 1600], 'Attendance': [0, 1]})
new_data = new_data[['const', 'SAT', 'Attendance']]

predictions = results.predict(new_data)
print(predictions)

predictions_df = pd.DataFrame({"predictions": predictions})
joined = new_data.join(predictions_df)
print(joined)
