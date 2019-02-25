import numpy as np
import cv2
import os
import argparse

import edge_detect


def trackbar_callback(x):
	pass

def edge_detect_batch(input_dir, output_dir, preblur_size, mode, can_min_val, can_max_val, scale, sob_size, tresh, use_ip, *args):



	print("\nInput Dir: %s" % input_dir)
	print("Output Dir: %s" % output_dir)

	#iterate through image dir
	for i in os.listdir(input_dir):

		#if ip
		if (int(use_ip) == 1):
			#create image window
			cv2.namedWindow('image')
			cv2.createTrackbar('treshhold','image', int(tresh), 255, trackbar_callback)


		#stay in loop while adjusting sliders
		while True:
			#if ip
			if (int(use_ip) == 1):
				tresh = cv2.getTrackbarPos('treshhold','image')

			
			#read image
			input_img = os.path.join(input_dir, i)
			output_img = os.path.join(output_dir, i)

			#read image into cv2
			img = cv2.imread(input_img, 1)


			#run edge detection filter script
			img = edge_detect.edge_detect_filter(img)

			

			#if ip
			if (int(use_ip) == 1):

				#show image in window
				cv2.imshow('image', img)
				k = cv2.waitKey(1) & 0xFF
				if k == 27:
					#write image
					cv2.imwrite(output_img, img)

					#break while loop
					break
			#if no ip
			else:
				
				#write image
				cv2.imwrite(output_img, img)

				#break while loop
				break


			

	print("\nFinished converting images with OpenCV Canny Edge Detection.\n")



#argument parser

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='OpenCV Canny Edge Detection Conversion')
	parser.add_argument('-i', '--input',
						dest='input_dir',
						help='Input Directory',
						required=True)
	parser.add_argument('-o', '--output',
						dest='output_dir',
						help='Outut Directory',
						required=True)
	parser.add_argument('-bs', '--preblur_size',
						dest='preblur_size',
						help='Gaussian Pre Blur Size',
						required=False,
						default=3)
	parser.add_argument('-m', '--mode',
						dest='mode',
						help='Detection Mode: 0=Canny, 1=Laplacian, 2=Sobel Combined, 3=SobelX, 4=SobelY',
						required=False,
						default=2)
	parser.add_argument('-x', '--can_minval',
						dest='can_min_val',
						help='Canny Min Val',
						required=False,
						default=100)
	parser.add_argument('-y', '--can_maxval',
						dest='can_max_val',
						help='Canny Max Val',
						required=False,
						default=200)
	parser.add_argument('-s', '--scale',
						dest='scale',
						help='Filter Scale',
						required=False,
						default=6)
	parser.add_argument('-sz', '--sob_size',
						dest='sob_size',
						help='Sobel Size',
						required=False,
						default=1)
	parser.add_argument('-tr', '--tresh',
						dest='tresh',
						help='Black Treshhold',
						required=False,
						default=0)
	parser.add_argument('-ip', '--use_ip',
						dest='use_ip',
						help='Ise Interactive Preview',
						required=False,
						default=0)
   

	results = parser.parse_args()
	

	

	#run function	

	edge_detect_batch(results.input_dir, 
					results.output_dir,
					results.preblur_size,
					results.mode,
					results.can_min_val,
					results.can_max_val,
					results.scale,
					results.sob_size,
					results.tresh,
					results.use_ip)

