import socket
import registor

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('172.30.1.33', 15000)
print('Startinf up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)    

while True:
    #연결을 기다림
    print('waiting for a connection')
    connection, _ = sock.accept()
    try:
        while True:
            data = connection.recv(1024)
            a = format(data.decode())
            id = a.split('_')
            print('sending data back to the client')
            send = registor.registor(id)
            message= send.encode()
            connection.sendall(message)
            break
    finally:
        # 연결 모두 지움
        print("closing current connection")
        connection.close()