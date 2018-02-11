import pandas as pd

df = pd.read_excel('stocks2.xlsx',header=[0,1])
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


df = df.stack()
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


df = pd.read_excel('stocks2.xlsx',header=[0,1])
df = df.stack(level=0)
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


df = pd.read_excel('stocks_level_3.xlsx',header=[0,1,2])
df = df.stack(level=1)
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


