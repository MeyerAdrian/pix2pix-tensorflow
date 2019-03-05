
import argparse
import numpy as np
import cv2
import os
import time

import serve
import json

import sys
import subprocess


def inference_cam(input_model, output_dir, *args):



    #start touchdesigner and photoshop
    p = subprocess.Popen(["powershell.exe", "-ExecutionPolicy", "Unrestricted", "./prelaunch_inference_webcam_touchdesigner.ps1"], stdout=sys.stdout)


    #set CUDA_VISIBLE_DEVICES
    os.environ["CUDA_VISIBLE_DEVICES"] = "1"
    print("\nSet CUDA_VISIBLE_DEVICES = 1\n")



    ##### get res from input model dir
    options_s = {"scale_size"}
    with open(os.path.join(input_model, "options.json")) as f:
        for key, val in json.loads(f.read()).items():
            if key in options_s:
                #print("loaded", key, "=", val)
                img_res = int(val)
                print("\nModel Resolution retrieved from Exported Model Data and set to:", img_res, "px\n")



    #set temp img path
    out__ = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp_out.jpg')
    input_image_queue, output_image_queue, live_process, lifetime_end = serve.process_handler(input_model, out__)



    #temp file (labeled image, in this case form touchdesigner)
    temp = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp.jpg')

    #initial frame read
    frame = cv2.imread(temp, 1)


    #vars
    _last = None
    n = 1



    #while loop

    while (True):

        #inference


        #check if prediction process can receive img, if empty
        if input_image_queue.empty():
            #if yes add temp img 
            input_image_queue.put(temp)

        #sleep for a while 
        #time.sleep(0.1)

        #read predict output from process tunnel
        if not output_image_queue.empty():
            #get signal
            pred_img = output_image_queue.get()
            #save img
            _last = cv2.imread(pred_img, 1)
        
        #check if numpy 
        if isinstance(_last, np.ndarray):
            #overwrite frame
            frame = _last



        #display
        cv2.imshow('q Close, s Save', frame)
        key = cv2.waitKey(1) & 0xFF





        #write image function
        if key == ord('s'):

            image_file = os.path.join(output_dir, "img_{0}.png".format(str(n).zfill(4)))
            cv2.imwrite(image_file, frame)

            print("Snapshot created:", image_file, "\n")

            #increase img counter
            n += 1



        #quit process
        if key == ord('q'):
            #set value to break BG while loop
            lifetime_end.value = True

            for process in live_process:
                #kill process in BG
                process.join()

            #break cv
            break





#arg parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pix2Pix Inference Module')

    parser.add_argument('-m', '--input_model',
                        dest='input_model',
                        help='Input Model Dir',
                        required=True)
    parser.add_argument('-o', '--output_dir',
                        dest='output_dir',
                        help='Image Output Dir',
                        required=False)

    
    results = parser.parse_args()
    

    #call function
    inference_cam(results.input_model, results.output_dir)