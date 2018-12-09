# TCP client example
import socket,os
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("169.254.159.161", 5005))
k = ' '
size = 1024

while(1):
    try:
        raw_input()
        command = "SEND"
        client_socket.send(command)
        
        print ("\nThe file will be saved and opened- ")
        fname = 'test1.jpg'
        with open(fname, 'wb') as nf:
            while True:
                strng = client_socket.recv(2097152)
                if not strng:
                    break
                nf.write(strng)
    except KeyboardInterrupt:
        pass
