import socket
from picamera import PiCamera

def take_picture(img_name):
    camera.capture('test_images/' + img_name)
    print ("Taking Picture")

def receive_name(prefix=''):
    img_count = client_socket.recv(1024)
    client_socket.send("RECEIVED")
    print ("RECEIVED NAME")
    return prefix + img_count + '.jpg'

def send_image(img_name):
    img_path = 'test_images/' + img_name
    with open(img_path, 'rb') as img:
        img_bytes = img.read()
        client_socket.send("SIZE " + str(len(img_bytes)))
        reply = client_socket.recv(1024)
        if reply != "GOT SIZE":
            return 0
        print ("SENT SIZE")
        
        client_socket.send(img_bytes)
        client_socket.send("DONE")
	print ("DONE")
	reply = client_socket.recv(1024)
        if reply == "IMAGE RECEIVED":
            print ("IMAGE SENT SUCCESSFULLY")
            return 1

try:
        prefix = 'slave'
        camera = PiCamera()
        camera.resolution = (640, 480)

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(("22.22.22.22", 5002))

        img_name = receive_name(prefix)
        take_picture(img_name)
        send_image(img_name)

finally:
        client_socket.close()
