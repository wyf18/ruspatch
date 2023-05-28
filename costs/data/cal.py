import pandas as pd

# read the CSV file
df = pd.read_csv('e1.csv')

# calculate average and SIQR for the `before` column
before_avg = df['before'].mean()
before_q1 = df['before'].quantile(0.25)
before_q3 = df['before'].quantile(0.75)
before_siqr = (before_q3 - before_q1) / 2

after_avg = df['after'].mean()

increase = (after_avg - before_avg)/before_avg * 100

# print the calculated values
print('Before - Average:', before_avg)
print('Before - SIQR:', before_siqr)
print('Average - Percentage Increase:', increase)