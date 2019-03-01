
import argparse
import numpy as np
import cv2
import os
import time

import edge_detect
import serve
import json

def face_detect_cam(res, *args):

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
            #frame = edge_detect.edge_detect_filter(frame)

            #convert to grayscale
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
            faces = faceCascade.detectMultiScale(frame_gray)
            for face in faces:
                x1, y1, w, h = face
                x2 = x1 + w
                y2 = y1 + h

                #draw face recatngel over image
                frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        

        #display
        cv2.imshow('"q" Close, "d" Face Detect', frame)
        key = cv2.waitKey(1) & 0xFF


        #toggle image preprocesing
        if key == ord('d'):
            if(use_preproc):
                use_preproc = 0
            else:
                use_preproc = 1


        #quit process
        if key == ord('q'):

            #break cv
            break


    #close video capture
    cam_cap.release()




#arg parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Face Detect Webcam')

    parser.add_argument('-r', '--res',
                        dest='res',
                        type=int,
                        default=512,
                        help='Resolution',
                        required=False)
    

    results = parser.parse_args()

    #call function
    face_detect_cam(results.res)