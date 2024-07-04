# Introduction
OpenCV is the most popular library for the task of computer vision, it is a cross-platform open-source library for machine learning, image processing, etc. using which real-time computer vision applications are developed.

CVzone is a computer vision package, where it uses OpenCV and MediaPipe libraries as its core that makes us easy to run like hand tracking, face detection, facial landmark detection, pose estimation, etc., and also image processing and other computer vision-related applications. Check here for more information.

# Outcome
![2024-07-04 17-37-15](https://github.com/tuyenle009/AI-Virtual-Keyboard-Using-OpenCV/assets/128459950/4a551d90-7b8e-43c0-b9e1-0b4baafb1139)

# Implementation of Virtual Keyboard Using OpenCV
Let us create a virtual Keyboard.

First, let us install the required modules.

---> pip install numpy

---> pip install opencv-python

---> pip install cvzone

---> pip install pynput

# Import Libraries for Virtual Keyboard Using OpenCV
Now let’s import the required modules

import cv2
from HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

# Conclusion
This is the implementation of the virtual keyboard, if you want to take it to the next step you can also all the keypress sounds and then we can also make the keyboard layout move within the frames.
Hope you enjoyed it.


