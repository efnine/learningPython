import pandas as pf
import quandl
import math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOG')

### lets define the initial columns we want
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

### lets add some columns
df['Open2Close_Return'] = ((df['Adj. Close'] / df['Adj. Open']) - 1) * 100
df['Low2High_Spread'] = ((df['Adj. High'] / df['Adj. Low']) - 1) * 100

### lets define the final df
df = df[['Adj. Close','Adj. Volume','Open2Close_Return','Low2High_Spread']]

### lets try to forcast the close
forecast_col = 'Adj. Close'
df.fillna('-9999999999', inplace=True) # in ML you can't work with NaNs

# TODO: test the below with round()
forecast_out = int(math.ceil(0.01*len(df))) # rounding to nearest whole
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

#### lets define our features and our label
X = np.array(df.drop(['label'],1)) # features tend to be capitalize
y = np.array(df['label']) # labels tend to be lower case 
X = preprocessing.scale(X) # we are scaling X to be normalize
y = np.array(df['label'])

print(len(X),len(y))

X_train, X_test, y_test, y_train = cross_validation.train_test_split(X, y, 
                                                                     test_size=0.50)
### lets define our classifier
clf = LinearRegression() # this is the algo used to conduct the regression
clf.fit(X_train, y_train) # fit is used to train
accuracy = clf.score(X_test, y_test) # score is used to test

print(accuracy)

https://www.youtube.com/watch?v=QLVMqwpOLPk&list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v&index=5