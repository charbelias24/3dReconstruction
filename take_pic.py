from picamera import PiCamera
import time

cam = PiCamera()
cam.resolution = (640, 480)
cam.start_preview()

time.sleep(5)
for i in range(14):
    print ('Taking picture ' + str(i))
    cam.capture('test_images/calibrate50' + str(i) + '.jpg')
    time.sleep(2)
cam.stop_preview()
