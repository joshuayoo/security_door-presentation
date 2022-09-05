import socket
import pandas as pd
from pandas import DataFrame
import datetime

# TCP/IP 소켓을 생성하고
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 소켓을 포트에 연결
server_address = ('172.30.1.33', 10000)
print('Startinf up on {} port {}'.format(*server_address))
sock.bind(server_address)

# 연결을 기다림
sock.listen(1)       

def check(id, text):
    df = pd.read_csv('/home/joshua/project/data/check.csv')
    data1 =list(df['id'])
    if id in data1:
        data1 =list(df['text'])
        for row in range(len(data1)):
            if text in data1[row]:
                name = df.iloc[row][0]
                print(name, id)
                data_def(name, id)
                a = 'success' + str(name)
                return a
            else:
                return 'deny'
    return 'deny'
    
def data_def(name, id):
    df = pd.read_csv('/home/joshua/project/data/much.csv')
    date = datetime.datetime.now()
    date = date.strftime("%Y년 %m월 %d일")
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
    a = int(df.iloc[-1][name + '_*_' +id ]) +1
    df.at[a1, name + '_*_' +id] = a

    df.to_csv('/home/joshua/project/data/much.csv',index=False)
    

while True:
    #연결을 기다림
    print('waiting for a connection')
    connection, _ = sock.accept()
    try:
        while True:
            data = connection.recv(1024)
            a = format(data.decode())
            id = a[:len(a)//2]
            text = a[len(a)//2:]
            print('sending data back to the client')
            send = check(id, text)
            print(send)
            message= send.encode()
            connection.sendall(message)
            break
    finally:
        # 연결 모두 지움
        print("closing current connection")
        connection.close()