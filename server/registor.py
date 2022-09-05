import pandas as pd
from pandas import DataFrame
import hashlib

def registor(id):
    try:
        df = pd.read_csv('/home/joshua/project/data/much.csv')
        id[0] = hashlib.sha256(str(id[0]).encode()).hexdigest()
        text = hashlib.sha256(str(id[1]).encode()).hexdigest()
        a = list(DataFrame(df))
        if id[1] + '_' +id[0] in a:
            return 'error'
        del(a)
        df[id[1] + '_' +id[0]] = 0
        df.to_csv('/home/joshua/project/data/much.csv',index=False)
        del(df)
        df_1 = pd.read_csv('/home/joshua/project/data/check.csv')
        df_1.loc[len(df_1)] = [id[1],id[0],text]
        df_1.to_csv('/home/joshua/project/data/check.csv',index=False)
        return 'success'
    except:
        return 'error'
