
import sys
import os
import dlib

import argparse
import numpy as np
import cv2
from imutils import face_utils


predictor_path = "./shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)



def create_bg(res, *args):

	#create bg_img image
	rgb_color = (50, 50, 0)
	bgr_color = tuple(reversed(rgb_color))
	bg_img = np.zeros((res, res, 3), np.uint8)
	bg_img[:] = bgr_color

	return bg_img



def face_landmark_detect(img, bg_img, res, blend, *args):

	
	# Ask the detector to find the bounding boxes of each face. The 1 in the
	# second argument indicates that we should upsample the image 1 time. This
	# will make everything bigger and allow us to detect more faces.

	dets = detector(img, 0)
	det_num = len(dets)
	#print("Number of faces detected: {}".format(det_num))


	if (det_num >= 1):
	    for k, d in enumerate(dets):
	        #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
	        # Get the landmarks/parts for the face in box d.
	        shape = predictor(img, d)
	        #print("Part 0: {}, Part 1: {} ...".format(shape.part(0),shape.part(1)))
	        shape = face_utils.shape_to_np(shape)
	        
	        out_img = face_utils.visualize_facial_landmarks(bg_img, shape)

	        if blend == 1:
	        	#blend in original
	        	out_img = cv2.addWeighted(img, 0.3, out_img, 0.7, 0)

	else:
	    out_img = img


	#return
	return out_img




#argument parser

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Face Landmark Detection')
	parser.add_argument('-i', '--image',
						dest='img',
						help='Input Image',
						required=True)
	parser.add_argument('-r', '--res',
						dest='res',
						help='Image Resolution',
						required=True)
	parser.add_argument('-b', '--blend',
						dest='blend',
						help='Blend Original',
						default=0,
						type=int,
						required=False)
   
	results = parser.parse_args()	

	
	#run function
	face_landmark_detect(results.img, results.bg_img, results.res, results.blend)