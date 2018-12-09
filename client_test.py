# TCP client example
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("22.22.22.22", 5000))

while True:
    try:
        raw_input()
        command = "SEND"
        client_socket.send(command)
        
        print ("\nThe file will be saved and opened- ")
        fname = 'test_images/test2.jpg'
        with open(fname, 'wb') as file:
            while True:
                strng = client_socket.recv(2097152)
                if not strng:
                    break
                file.write(strng)
    except KeyboardInterrupt:
        client_socket.close()
