# merges 3 256x256px images side by side
# have to be named the same and be stored in two different folders
# arguments: -a A Image Dir // -b B Image Dir  // -c C Image Dir  //  -o Output Image Dir

import numpy as np
import argparse
import cv2
import os
import time



def merge_sbs_batch(image_dir_a, image_dir_b, image_dir_c, output_dir, *args):


    print("\n")
    print("\nStart SBS Merging of Images")
    print("Image A Directory:", image_dir_a)
    print("Image B Directory:", image_dir_b)

    if (image_dir_c != None):
        print("Image C Directory:", image_dir_c, "\n")
    else:
        print("No C Image Dir\n")

    

    a_images = iter(os.listdir(image_dir_a))
    b_images = iter(os.listdir(image_dir_b))

    if (image_dir_c != None):
        c_images = iter(os.listdir(image_dir_c))

    end_reached = 0
    n = 0

    while not end_reached:
        try:
            file_a = os.path.join(image_dir_a,next(a_images))
            file_b = os.path.join(image_dir_b,next(b_images))

            a = cv2.imread(file_a)
            b = cv2.imread(file_b)

            if (image_dir_c != None):
                c = cv2.imread(os.path.join(image_dir_c,next(c_images)))

            res = a.shape[1]

            
            #print(a.shape, b.shape, c.shape)

            if (image_dir_c != None):

                image = np.concatenate((a, b, c), axis=1)

            else:
                image = np.concatenate((a, b), axis=1)

            image_file = os.path.join(output_dir, "img_sbs_{0}.jpg".format(str(n).zfill(4)))
            cv2.imwrite(image_file, image)
            print("SBS Image created:", image_file)

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