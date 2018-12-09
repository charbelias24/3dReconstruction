import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("22.22.22.22", 5002))
server_socket.listen(5)

chunk_size = 1024

client_socket, address = server_socket.accept()
print ("Conencted to - ",address,"\n")

def receive_image():
    try:
        received = False
        print ("Waiting for client to send data")
        data = client_socket.recv(1024)
        if data.split(' ')[0] == 'SIZE':
            img_size = int(data.split(' ')[1])
            print("GOT SIZE: {}".format(img_size))
            client_socket.send("GOT SIZE")
            data = client_socket.recv(1024)

            if data.split(' ')[0] == 'NAME':
                client_socket.send("GOT NAME")
                img_name = data.split(' ')[1]
                img_path = 'test_images/' + img_name
                print ("GOT NAME: {}".format(img_name))
                with open(img_path, 'wb') as img:
                    received_chunks = 0
                    total_chunks = img_size // chunk_size + 1
                    while received_chunks < total_chunks:
                        chunk_data = client_socket.recv(chunk_size)
                        img.write(chunk_data)
                        received_chunks += 1
                client_socket.send("IMAGE RECEIVED")
                print ("IMAGE RECEIVED SUCCESSFULLY")
                received = True
                client_socket.close()
                server_socket.close()
                print ("Closed connection securely")
        return received

    except KeyboardInterrupt:
        client_socket.close()
        server_socket.close()
        print ("Closed connection securely")

        return received

receive_image()
