import pandas as pd

df = pd.read_excel('survey.xlsx')
print("\n----------------------------------------")
print(df)
print("----------------------------------------\n")


### lets create a contingency table
new_df = pd.crosstab(df['Nationality'],df['Handedness'])
print("\n----------------------------------------")
print(new_df)
print("----------------------------------------\n")

### lets create a contingency table
new_df = pd.crosstab(df['Sex'],[df['Nationality'],df['Handedness']],margins=True)
print("\n----------------------------------------")
print(new_df)
print("----------------------------------------\n")


### lets create a contingency table
pct_df = pd.crosstab(df['Sex'],df['Handedness'],normalize='index')
print("\n----------------------------------------")
print(pct_df)
print("----------------------------------------\n")


### How about understanidng the average age of females that are lefthanded
pct_df = pd.crosstab(df['Sex'],df['Handedness'], values=df['Age'], aggfunc='mean')
print("\n----------------------------------------")
print(pct_df)
print("----------------------------------------\n")