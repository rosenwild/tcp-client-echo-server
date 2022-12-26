import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()
connection = True
while connection:
    data = conn.recv(1024)
    if not data:
        break
    elif data == b'exit':
        print('client disconnected')
    else:
        conn.send(data)
        print(data)
conn.close()
