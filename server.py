import socket

ip = "192.168.50.54"
port = 5005
bufsize = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip, port))
s.listen(5)
counter = 0;
while 1:
    conn, addr = s.accept()
    f = open('test.txt', 'a')
    f.write('connection addr:' + str(addr) + '\n')

    data = conn.recv(bufsize)
    if not data:
        continue
    f.write('received info:' + str(data) + '\n')
    f.close()
    conn.close()
