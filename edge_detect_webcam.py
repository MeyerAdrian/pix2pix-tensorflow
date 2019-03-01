
import argparse
import numpy as np
import cv2
import os
import time

import edge_detect
import serve
import json

def edge_detect_cam(res, *args):

    cam_cap = cv2.VideoCapture(1)

    use_preproc = 1

    while (True):
        #print (True)
        ret, frame = cam_cap.read()

      
        #resize

        target_size = res
        frame_rec = frame.shape
        frame_height = frame_rec[0]
        frame_width = frame_rec[1]
        frame_scale = target_size / frame_height
        frame_width_s = int(frame_width * frame_scale)
        width_offset = int((frame_width_s - target_size) / 2)

        #rescale
        frame = cv2.resize(frame, (frame_width_s, target_size))

        #crop square
        frame = frame[0:target_size, width_offset:(frame_width_s-width_offset)]

        #post fix scale
        frame = cv2.resize(frame, (target_size, target_size))
        #print (frame.shape)


        #image pre processing, filters

        if (use_preproc):
            frame = edge_detect.edge_detect_filter(frame)

        

        #display
        cv2.imshow('"q" Close, "d" Prepocessing', frame)


        #toggle image preprocesing
        if cv2.waitKey(10) == ord('d'):
            if(use_preproc):
                use_preproc = 0
            else:
                use_preproc = 1


        #quit process
        if cv2.waitKey(10) == ord('q'):

            #break cv
            break


    #close video capture
    cam_cap.release()




#arg parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Edge Detect Webcam')

    parser.add_argument('-r', '--res',
                        dest='res',
                        type=int,
                        default=512,
                        help='Resolution',
                        required=False)
    

    results = parser.parse_args()

    #call function
    edge_detect_cam(results.res)