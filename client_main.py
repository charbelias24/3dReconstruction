## THIS IS THE REFACTORED CODE OF THE PREVIOUS RUNNING FILE ON CLIENT RPI

import socket
import time
import RPi.GPIO as GPIO
from picamera import PiCamera

class SendImageToServer():
    """ Take and send images to the server on the press of a button"""
    def __init__(self):
        try:
            self.port = 5002
            self.host_ip = "22.22.22.22"

            self.camera = PiCamera()
            self.camera.resolution = (640, 480)
            self.image_prefix = 'right'
            self.image_path = 'test_images/'
	    self.image_extension = '.jpg'
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception as e:
            print(e)

    def __del__(self):
        self.camera.close()
	self.client_socket.close()

    def connect_to_host(self):
	connected = False
	while not connected:
		try:
			print ("TRYING TO CONNECT TO HOST: {}:{}".format(self.host_ip, self.port))
			self.client_socket.connect((self.host_ip, self.port))
			connected = True
			print ("CONNECTED TO HOST: {}:{}".format(self.host_ip, self.port))
		except Exception as e:
			connected = False
			print (e)
			time.sleep(0.5)
    def receive_name(self):
        image_count = self.client_socket.recv(1024)
	self.client_socket.send("RECEIVED")
        return self.image_prefix + image_count

    def take_picture(self, image_name):
        self.camera.capture(self.image_path + image_name + self.image_extension)
        print ("THE IMAGE IS SAVED IN: {}".format(self.image_path + image_name + self.image_extension))

    def send_image(self, image_name):
        image_name_full = self.image_path + image_name + self.image_extension

        with open(image_name_full, 'rb') as image:
            image_bytes = image.read()
            self.client_socket.send("SIZE " + str(len(image_bytes)))
            reply = self.client_socket.recv(1024)
            if reply != "GOT SIZE":
                return 0
            #print ("SENT SIZE")

            self.client_socket.send(image_bytes)
            self.client_socket.send("DONE")

        #print ("DONE")
        reply = self.client_socket.recv(1024)
        if reply == "IMAGE RECEIVED":
                print ("IMAGE SENT SUCCESSFULLY")
                return 1

    def run(self):
        """ After being connected to the server, get the image name and then take
        a picture and send it to the server"""
        image_name = self.receive_name()
        self.take_picture(image_name)
        self.send_image(image_name)
	print 

def main():
    """ Waits for the press of a button and executes accordingly"""
    ## setting the pin number of the Button
    btn_pin = 7
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btn_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    image_to_server = SendImageToServer()

    try:
        image_to_server.connect_to_host()
	while True:
            ## Checking if the button is pressed
            if GPIO.input(btn_pin):
                print ("BUTTON PRESSED")
		image_to_server.run()
                time.sleep(0.5)
            time.sleep(0.01)
    except Exception as e:
        print(e)
    finally:
        del image_to_server

if __name__ == "__main__":
    main()
