import socket
import time
from picamera import PiCamera 
import RPi.GPIO as GPIO


def take_picture(img_name):
    camera.capture('test_images/' + img_name)

def get_img_count():
    try:
        with open('data/current_count.txt', 'r') as file:
            current_count = file.read()
            if current_count:
                current_count = int(current_count)
            else:
                return 0
        with open('data/current_count.txt', 'w') as file:
            file.write(str(current_count+1))

        return str(current_count)

    except Exception as e:
        print (e.message)

def send_count(img_count):
    client_socket.send(img_count)
    print ("Sending image count")
    reply = client_socket.recv(1024)
    if reply == "RECEIVED":
        print ("The slave got the count")
        return 1
    else:
        print ("The slave did not get the count ")
        return 0

def receive_image(img_count):
    received = False
    print ("Waiting for client to send data")
    data = client_socket.recv(1024)
    if data.split(' ')[0] == 'SIZE':
        img_size = int(data.split(' ')[1])
        print("GOT SIZE: {}".format(img_size))
        client_socket.send("GOT SIZE")
        #img_name = 'right' + img_count + '.jpg'
        img_name = 'right' + '.jpg'

        img_path = 'test_images/' + img_name
        with open(img_path, 'wb') as img:
            while True:
                chunk_data = client_socket.recv(chunk_size)
                if "DONE" in chunk_data:
                    img.write(chunk_data[:-4])
                    break
                img.write(chunk_data)
    
        client_socket.send("IMAGE RECEIVED")
        print ("IMAGE RECEIVED SUCCESSFULLY")
        received = True
    return img_path if received else 0

red_led = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_led, GPIO.OUT)

prefix = 'left'
camera = PiCamera()
camera.resolution = (640, 480)
time.sleep(2)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("22.22.22.22", 5002))
server_socket.listen(5)

chunk_size = 1024
client_socket, address = server_socket.accept()
print ("Conencted to - " + str(address))

try:
    img_count = get_img_count()
    #img_name = prefix + img_count + '.jpg'
    img_name = prefix + '.jpg'

    if send_count(img_count):
        take_picture(img_name)
        GPIO.output(red_led, 1)

    else:
        print("Did not take picture!")
    receive_image(img_count)
    
    client_socket.close()
    server_socket.close()
    print ("Closed connection securely")
    GPIO.output(red_led, 0)

    
except Exception as error:
    print (error)
    client_socket.close()
    server_socket.close()
    print ("Closed connection securely")
