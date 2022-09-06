import pandas as pd
from pandas import DataFrame
from datetime import datetime

def check(id, text):
    df = pd.read_csv('/home/pi/project/data/check.csv')
    data =list(df['id'])
    print(data)
    if id in data:
        data =list(df['text'])
        for row in range(len(data)):
            if text in data[row]:
                name = df.iloc[row][0]
                return 'success' + str(name)
            else:
                return 'deny'
    return 'deny'

print(check('id', 'text'))