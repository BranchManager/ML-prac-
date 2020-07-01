import pandas as pd
import matplotlib.pyplot as plt

#read in DAta into pandas dataframe
data = pd.read_csv("auto-mpg.data",delimiter='\s+',header=None)


#adding the colunn names
data.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','orign','car name']
#data.Name.str.split(expand=True)

print(data.columns)
print(data)

#irrelevant
Q = data.loc[data['horsepower']=='?']

#removing the rows that have '?' in horsepower column
df = data[~data['horsepower'].isin(['?'])]
print(df['horsepower'].dtypes)

#convert horwpower column to float type
df=df.astype({"horsepower":float})
print(df)


#set up for plotting each in a subplot
fig, axs = plt.subplots(figsize=(10,10),nrows=3, ncols=3)

df.plot(ax=axs[0,0],x='mpg',y='weight',kind='scatter',marker='+')
df.plot(ax=axs[0,1],x='mpg',y='horsepower',kind='scatter')
df.plot(ax=axs[0,2],x='mpg',y='cylinders',kind='scatter')
df.plot(ax=axs[1,0],x='mpg',y='acceleration',kind='scatter')
df.plot(ax=axs[1,1],x='mpg',y='model year',kind='scatter')
df.plot(ax=axs[1,2],x='mpg',y='displacement',kind='scatter')
fig.tight_layout(pad=2.0)
plt.show()

