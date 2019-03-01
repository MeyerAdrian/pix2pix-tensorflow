
import argparse
import numpy as np
import cv2
import os
import time

import serve
import json

import face_landmark_detect

def face_landmark_detect_cam(res, *args):

    cam_cap = cv2.VideoCapture(1)

    use_preproc = 1
    use_blend = 0

    #create bg image first outside loop
    bg_img = face_landmark_detect.create_bg(res)


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
            
            #run detection function
            frame_out = face_landmark_detect.face_landmark_detect(frame, bg_img, res)

            if (use_blend):
                frame_out = cv2.addWeighted(frame, 0.5, frame_out, 0.5, 0)

        else:
            frame_out = frame

        

        #display
        cv2.imshow('"q" Close, "d" Face Detection, "b" Blending', frame_out)
        key = cv2.waitKey(1) & 0xFF


        #toggle image preprocesing
        if key == ord('d'):
            if(use_preproc):
                use_preproc = 0
            else:
                use_preproc = 1

        #toggle blending
        if key == ord('b'):
            if(use_blend):
                use_blend = 0
            else:
                use_blend = 1


        #quit process
        if key == ord('q'):

            #break cv
            break


    #close video capture
    cam_cap.release()




#arg parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face Landmark Detect Webcam')

    parser.add_argument('-r', '--res',
                        dest='res',
                        type=int,
                        default=512,
                        help='Resolution',
                        required=False)
    

    results = parser.parse_args()

    #call function
    face_landmark_detect_cam(results.res)