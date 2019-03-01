
import sys
import os
import dlib
import glob

import argparse
import numpy as np
from imutils import face_utils
import cv2


def face_landmark_detect_batch(input_dir, output_dir, *args):

    predictor_path = "./shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    
    print("Start Batch Processing.\n")
        
    #iterate through directory
    for f in os.listdir(input_dir):

        input_file = os.path.join(input_dir, f)
        output_file = os.path.join(output_dir, f)


        print("Processing file: {}".format(input_file))

        img = dlib.load_rgb_image(input_file)
        cv2_img = cv2.imread(input_file, 1)
        img_res = cv2_img.shape[0]


        #create bg_img image
        rgb_color = (50, 50, 0)
        bgr_color = tuple(reversed(rgb_color))
        bg_img = np.zeros((img_res, img_res, 3), np.uint8)
        bg_img[:] = bgr_color


        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.

        dets = detector(img, 1)
        det_num = len(dets)
        print("Number of faces detected: {}".format(det_num))

        
        if (det_num >= 1):
            for k, d in enumerate(dets):
                #print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
                # Get the landmarks/parts for the face in box d.
                shape = predictor(img, d)
                #print("Part 0: {}, Part 1: {} ...".format(shape.part(0),shape.part(1)))
                shape = face_utils.shape_to_np(shape)
                
                out_img = face_utils.visualize_facial_landmarks(bg_img, shape)

        else:
            out_img = cv2_img


        cv2.imwrite(output_file, out_img)
        print("Face Landmark Image written:", output_file, "\n")

    
    print("Batch Processing Finished.\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "DLib Face Landamrk Detecttion")
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