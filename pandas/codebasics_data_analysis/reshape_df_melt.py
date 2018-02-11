import pandas as pd

df = pd.read_csv('melt_file.csv')
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


df = pd.melt(df, id_vars=['day'], var_name='city', value_name='temperature')
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


df = df[df['city']=='chicago']
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")