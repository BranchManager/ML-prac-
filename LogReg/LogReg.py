import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Untitled.txt",delimiter=',',header=None)

data.columns=['Times Prego','Plasma Glucose','BP','Skin Thiskness','2hr serum insulin','BMI','Pedigree Funtion','age','class']

print(data.dtypes)
print(data['class'].value_counts())
print(data['age'].mean())

pos = data.loc[data['class'] == 1]
print(pos['age'].mean())