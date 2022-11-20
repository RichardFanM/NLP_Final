# Data Prepare

import pandas as pd
from sklearn.model_selection import ShuffleSplit

data = pd.read_csv('../datas/crowdflower-airline-twitter-sentiment/data/airline_sentiment_2_w_aa.csv')

columns = data.columns
index_X = columns.get_loc('text')
index_Y = columns.get_loc('airline_sentiment')

X = []
Y = []
for row in data.values:
    X.append(row[index_X])
    Y.append(row[index_Y])

data = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
for train, test in data.split(X):
    x_train, x_test = X[train], X[test]
    # y_train, y_test = Y[train], Y[test]

print(len(x_test))