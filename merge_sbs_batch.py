# merges 3 256x256px images side by side
# have to be named the same and be stored in two different folders
# arguments: -a A Image Dir // -b B Image Dir  // -c C Image Dir  //  -o Output Image Dir

import numpy as np
import argparse
import cv2
import os
import time



def merge_sbs_batch(image_dir_a, image_dir_b, image_dir_c, output_dir, *args):

    '''
    print("\n")
    print(image_dir_a)
    print(image_dir_b)

    if (image_dir_c != None):
        print(image_dir_c)
    else:
        print("No C Image Dir")

    '''

    a_images = iter(os.listdir(image_dir_a))
    b_images = iter(os.listdir(image_dir_b))
    
    if (image_dir_c != None):
        c_images = iter(os.listdir(image_dir_c))

    end_reached = 0
    n = 0

    while not end_reached:
        try:
            a = cv2.imread(os.path.join(image_dir_a,next(a_images)))
            b = cv2.imread(os.path.join(image_dir_b,next(b_images)))
            if (image_dir_c != None):
                c = cv2.imread(os.path.join(image_dir_c,next(c_images)))

            res = a.shape[1]

            if (image_dir_c != None):
                image = np.concatenate((a, b, c), axis=1)
                resized = cv2.resize(image, (res*3, res))

            else:
                image = np.concatenate((a, b), axis=1)
                resized = cv2.resize(image, (res*2, res))

            cv2.imwrite(os.path.join(output_dir, "{0}.jpg".format(str(n))), resized)
            n += 1
        except StopIteration:
            end_reached = True

            print("\nFinished merging Images\n")



#argument parser

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description='OpenCV Canny Edge Detection Conversion')

    ap.add_argument("-a", "--A",
                    dest='input_dir_a',
                    required=True,
                    help="path to input A images dir")
    ap.add_argument("-b", "--B",
                    dest='input_dir_b',
                    required=True,
                    help="path to input B images dir")
    ap.add_argument("-c", "--C",
                    dest='input_dir_c',
                    required=False,
                    help="path to input C images dir")
    ap.add_argument("-o", "--output",
                    dest='output_dir',
                    required=True,
                    help="path to merged output dir")

    results = ap.parse_args()


    
    #run function   

    merge_sbs_batch(results.input_dir_a,
                    results.input_dir_b,
                    results.input_dir_c,
                    results.output_dir)