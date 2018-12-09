from picamera import PiCamera
import time

cam = PiCamera()
cam.resolution = (640, 480)
time.sleep(5)
cam.capture('test_images/test1.jpg')

