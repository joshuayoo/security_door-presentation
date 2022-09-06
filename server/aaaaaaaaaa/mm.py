from numpy import NaN
import pandas as pd
from pandas import DataFrame
from datetime import datetime

check=1
name = 'dbcksr'
df = pd.read_csv('/home/pi/project/data/much.csv')
date = datetime.now()
date = date.strftime("%Y년 %-m월 %-d일")
data_frame = DataFrame(df)
a = list(data_frame)
num = df.shape[0]
data_1 =list(df['date'])
if num == 0 or data_1[-1] != date:
    data_2 = [date]
    for _ in range(1, len(a)):
        data_2.append(0)
    df.loc[len(df)] = data_2
del(data_1)
data_1 =list(df['date'])
a1 = data_1.index(date)
a = int(df.iloc[-1][name]) +1
df.at[a1, name] = a

df.to_csv('/home/pi/project/data/much.csv',index=False)
check = 0
