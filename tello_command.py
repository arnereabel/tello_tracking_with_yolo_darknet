import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)             #udp uses dgram , send a datagram and get reply then connction terminats
tello_adress = ('192.168.10.1', 8889)                               # see docs ,  sets tello ip adress and port
sock.bind(('', 9000))                                               # sets the port to recaive teh response from tello

while True:                                                         # sends command to tello example: takeoff , up x , left y, cw x etc
    try:                                                            # detects 'end' in command ('msg') to tello on wich ity closes the connection
        msg = input('')                                             # encodes the command and sends to tello ip
        if not msg:
            break
        if 'end' in msg:
            sock.close()
            break
        msg = msg.encode()
        print(msg)
        sent = sock.sendto(msg,tello_adress)
    except Exception as err:
        print(err)
        sock.close()
        break