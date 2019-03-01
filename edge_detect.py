
import numpy as np
import cv2
import argparse		



def edge_detect_filter(img, preblur_size=1, mode=2, can_min_val=100, can_max_val=200, scale=6, sob_size=1, tresh=0, *args):


	#convert to grayscale
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	
	#preblur
	img = cv2.GaussianBlur(img, (int(preblur_size), int(preblur_size)), 0)


	#edge detction filters
	mode = int(mode)
	if (mode==0):
		#canny
		img = cv2.Canny(img, int(can_min_val), int(can_max_val))

	if (mode==1):
		#laplacian
		img = cv2.Laplacian(img, cv2.CV_64F, scale=int(scale))
		#img = cv2.convertScaleAbs(img)

	if (mode==2):
		#sobel combined
		grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, scale=int(scale), ksize=int(sob_size))
		grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, scale=int(scale), ksize=int(sob_size))

		abs_grad_x = cv2.convertScaleAbs(grad_x)
		abs_grad_y = cv2.convertScaleAbs(grad_y)
		img = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

	if (mode==3):
		#sobelx
		img = cv2.Sobel(img, cv2.CV_64F, 1, 0, scale=int(scale), ksize=int(sob_size))

	if (mode==4):
		#sobely
		img = cv2.Sobel(img, cv2.CV_64F, 0, 1, scale=int(scale), ksize=int(sob_size))


	
	#set image treshold
	ret, img = cv2.threshold(img, int(tresh), 255, cv2.THRESH_TOZERO)

	#convert
	img = np.uint8(np.absolute(img))


	#return
	return img





#argument parser


######defaults out of date

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='OpenCV Canny Edge Detection Conversion')
	parser.add_argument('-i', '--image',
						dest='img',
						help='Input Image',
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
   

	results = parser.parse_args()
	

	

	#run function	

	edge_detect_filter(results.img,
					results.preblur_size,
					results.mode,
					results.can_min_val,
					results.can_max_val,
					results.scale,
					results.sob_size,
					results.tresh)