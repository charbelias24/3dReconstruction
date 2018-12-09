import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("22.22.22.22", 5000))
server_socket.listen(5)


client_socket, address = server_socket.accept()
print ("Conencted to - ",address,"\n")

while True:
    try:
        data = client_socket.recv(1024)
        img_name = 'test1.jpg'
        img = open(img_name,'rb')
        while True:
            strng = img.readline(512)
            if not strng:
                break
            client_socket.send(strng)
        img.close()
        print ("Data sent successfully")
    except KeyboardInterrupt:
        client_socket.close()
        server_socket.close()


