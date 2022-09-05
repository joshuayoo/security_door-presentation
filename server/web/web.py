from flask import Flask, render_template, request
import pandas as pd
from pandas import DataFrame
from datetime import datetime


app = Flask(__name__)
date = datetime.now().strftime("%Y-%m-%d")
status = ''

def graph(date):
    global status
    name = []
    a = date.split('-')
    a = str(a[0] + "년 " + a[1] + "월 " + a[2] + "일")
    df = pd.read_csv('/home/joshua/project/data/much.csv')
    data_frame = DataFrame(df)
    if a in list(df['date']):
        data_1 =list(df['date'])
        a1 = data_1.index(a)
        status = '1'
        for i in list(data_frame)[1:]:
            a = i.split('_*_')
            name.append(a[0])
        return name, list(df.iloc[a1])[1:]
    else:
        status = 'no_data'
        return ["none"], ["none"]

@app.route('/')
def index():
    global date, status
    max_date = datetime.now().strftime("%Y-%m-%d")
    a, data = graph(date)
    return render_template('index.html', a =a, data = data, date = date, max_date = max_date, a1= status)

@app.route('/key', methods=['POST'])
def key():
    global date, status
    max_date = datetime.now().strftime("%Y-%m-%d")
    date = request.get_json()['key']
    print(date)
    a, data = graph(date)
    return render_template('index.html', a =a, data = data, date = date, max_date = max_date, a1= status)


if __name__ == '__main__':
    app.run(host='172.30.1.33', port="25565")