import socket
import time
import re

ip = "192.168.50.54"
port = 5005
bufsize = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip, port))
s.listen(5)

counter = 0
mac_set = set()
while 1:
    conn, addr = s.accept()
    data = conn.recv(bufsize)
    if not data:
        conn.close()
        continue

    data_list = data.split(" ")
    if (data_list[0] != "mac:"):
        conn.close()
        continue

    for mac_addr in data_list[1:]:
        if re.match('(([0-9a-fA-F]{2}:?){6})', mac_addr):
            mac_set.add(mac_addr)

    if counter < 6:
        counter = counter + 1
    else:
        counter = 0
        f = open('test.txt', 'a')
        # f.write('connection addr:' + str(addr) + '\n')
        f.write('received info: ' + ' '.join(mac_set) + '\n')
        f.write('timestamp: ' + str(time.time()) + '\n')
        f.close()
        mac_set.clear()
    conn.close()
