import socket
from picamera import PiCamera 

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
    reply = client_socket.recv(1024)
    if reply == "RECEIVED":
        return 1
    else return 0

def receive_image(img_name):
    received = False
    print ("Waiting for client to send data")
    data = client_socket.recv(1024)
    if data.split(' ')[0] == 'SIZE':
        img_size = int(data.split(' ')[1])
        print("GOT SIZE: {}".format(img_size))
        client_socket.send("GOT SIZE")
        data = client_socket.recv(1024)
       
        img_path = 'test_images/' + img_name
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
    return img_path if received else 0

try:
    prefix = 'master'
    camera = PiCamera()
    camera.resolution = (640, 480)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("22.22.22.22", 5002))
    server_socket.listen(5)

    chunk_size = 1024
    client_socket, address = server_socket.accept()
    print ("Conencted to - ", address, "\n")
    img_count = get_image_count()
    tmg_name = prefix + img_count + '.jpg'
    if send_count(img_count):
        take_picture(img_name)
    else:
        print("Did not take picture!")
    receive_image(img_name)
    
finally:
    client_socket.close()
    server_socket.close()
    print ("Closed connection securely")
