
import sys
import os

import argparse
import cv2
#import dlib

import face_landmark_detect


def face_landmark_detect_batch(input_dir, output_dir, *args):

    print("Start Batch Processing.\n")

           
    #iterate through directory
    for f in os.listdir(input_dir):

        input_file = os.path.join(input_dir, f)
        output_file = os.path.join(output_dir, f)


        print("Processing file: {}".format(input_file))

        #load image
        #img = dlib.load_rgb_image(input_file)
        img = cv2.imread(input_file, 1)
        img_res = img.shape[0]


        #create bg image first outside loop
        bg_img = face_landmark_detect.create_bg(img_res)

        #run detection function
        out_img = face_landmark_detect.face_landmark_detect(img, bg_img, img_res)


        #write image
        cv2.imwrite(output_file, out_img)
        print("Face Landmark Image written:", output_file, "\n")

    
    print("Batch Processing Finished.\n")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Batch Face Landmark Detection")
    parser.add_argument('-i', '--input_dir',
                        dest='input_dir',
                        help='Face Input Directory',
                        required=True)
    parser.add_argument('-o', '--output_dir',
                        dest='output_dir',
                        help='Output Directory',
                        required=True)

    r = parser.parse_args()


    #call function
    face_landmark_detect_batch(r.input_dir, r.output_dir)