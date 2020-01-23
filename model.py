import numpy as np
import pandas as pd
import os

train_data = pd.read_csv('./train.csv')
test_data = pd.read_csv('./test.csv')

train_headers = train_data.head(n=1)
test_headers = test_data.head(n=1)

train_desc = train_data.columns
test_desc = test_data.describe()


print(train_desc)
print('\n')
print(test_desc) 