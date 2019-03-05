#cam test

import cv2
import numpy as np


cam = cv2.VideoCapture(0)

cam.set(3, 960);
cam.set(4, 720);

while True:
	ret, frame = cam.read()

	#print ("ret value:", ret)
	print(frame.shape)

	cv2.imshow('"q" Close', frame)
	key = cv2.waitKey(1) & 0xFF


	if key == ord("q"):
		break

cam.release()
