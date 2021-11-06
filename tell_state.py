import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 8891))                                         #port on which to receive tello  state is 8890

while True:
    try:
        data, server = sock.recvfrom(1024)                 # receives data from the tello drone
        print(data.decode())
    except Exception as err:                                   # when ever error happens print the error , close socket and break
        print(err)
        socket.close()
        break
