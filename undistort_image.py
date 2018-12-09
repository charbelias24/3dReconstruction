import numpy as np
import cv2

objpoints = np.load('data/objpoints.npy')
imgpoints = np.load('data/imgpoints.npy')

def undistort_img(img, objpoints=objpoints, imgpoints=imgpoints):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

    h,  w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # crop the image
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    return dst

if __name__=="__main__":
    img = cv2.imread('test_images/calibrate7.jpg')

    undistorted_image = undistort_img(img, objpoints, imgpoints)
    cv2.imshow("Undistorted Image", undistorted_image)
    cv2.waitKey(5000)

