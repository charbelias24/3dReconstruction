import numpy as np
import cv2
from matplotlib import pyplot as plt
from undistort_image import undistort_img

imgL = cv2.imread('test_images/test1.jpg', 0)
imgR = cv2.imread('test_images/test2.jpg', 0)

#imgL = cv2.cvtColor(undistort_img(imgL), cv2.COLOR_BGR2GRAY)
#imgR = cv2.cvtColor(undistort_img(imgR), cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoBM_create()
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.show()
