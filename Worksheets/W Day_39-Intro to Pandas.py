import pandas as pd

t1_dict = {'One':[1,2,3,4],
             'Two': [9,8,7,6]}

df = pd.DataFrame(t1_dict)
print(df)
print('-'*20)

#a
#print(df['One']) column
#b
#print(df['One'][2])
#c
#print(df.iloc[1]) #row
#d
#print(df.iloc[1,1])
#e
#df2 = [df.iloc[1]].mean()
#print(df2)
#f
#df['Three'] = df.sum(axis =1)
#print(df)

'''

# Below are quick example
# Using DataFrame.mean() method to get column average
df2 = df["Fee"].mean()

# Using DataFrame.mean() to get entire column mean
df2 = df.mean()

# Using multiple columns mean using DataFrame.mean()
df2 = df[["Fee","Discount"]].mean()

# Average of each column using DataFrame.mean()
df2 = df.mean(axis=0)

# Find the mean including NaN values using DataFrame.mean()
df2 = df.mean(axis = 0, skipna = False)

# Using DataFrame.describe() method
df2 = df.describe()

Average of each row:
df.mean(axis=1)

'''
