import numpy as np
import cv2
from matplotlib import pyplot as plt
from undistort_image import undistort_img

window_size = 3
min_disp = 1
num_disp = 16


imgL = cv2.imread('test_images/master53.jpg')
imgR = cv2.imread('test_images/slave53.jpg')

imgL = cv2.cvtColor(undistort_img(imgL), cv2.COLOR_BGR2GRAY)
imgR = cv2.cvtColor(undistort_img(imgR), cv2.COLOR_BGR2GRAY)

stereo = cv2.StereoSGBM_create(
            minDisparity=min_disp,
            #numDisparities=num_disp,
            uniquenessRatio=10,
            speckleWindowSize=100,
            speckleRange=32,
            disp12MaxDiff=1,
            P1=8*3*window_size**2,
            P2=32*3*window_size**2,
            )

disparity = stereo.compute(imgL,imgR)

plt.imshow(disparity,'gray')
plt.show()
