# 3D Reconstruction

A DIY-box containing 2 Raspberry Pi cameras connected to a Raspberry Pi 3 to capture multiple stereo images and reconstruct a 3d pointcloud. 

### Calibration
After fixing the 2 cameras on the DIY-box, we calibrated them by taking stereo-images of a checkerboard and calculating the matrices using the library [StereoVision](https://stereovision.readthedocs.io/en/latest/).

### How it works
The stereo cameras are connected to a Rapsberry Pi 3 which are located in the DIY box.
A button is connected to the Raspberry Pi that takes a stereo-image when pressed, then undistorts the images and creates a disparity map. 
Then, we create a point cloud based on the disparity map and the colored images, and send it to the laptop using a socket connection.
Additionally, there is a connected LED light to visualize the success or failure of the process.

