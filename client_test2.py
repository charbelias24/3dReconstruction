import socket


def send_image(img_name):
        with open(img_name, 'rb') as img:
            img_bytes = img.read()
            client_socket.send("SIZE " + str(len(img_bytes)))
            reply = client_socket.recv(1024)
            if reply != "GOT SIZE":
                return 0
            print ("SENT SIZE")
            client_socket.send("NAME " + img_name)
            reply = client_socket.recv(1024)
            if reply != "GOT NAME":
                return 0
            print ("SENT NAME")
            client_socket.send(img_bytes)
            reply = client_socket.recv(1024)
            if reply == "IMAGE RECEIVED":
                print ("IMAGE SENT SUCCESSFULLY")
                return 1
try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("22.22.22.22", 5002))
        send_image('aloeL.jpg')
finally:
        client_socket.close()
