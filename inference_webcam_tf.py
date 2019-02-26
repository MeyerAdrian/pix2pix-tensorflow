
import argparse
import numpy as np
import cv2
import os
import time

import edge_detect
import serve
import json

def inference_cam(input_model, output_dir, *args):

    ##### get res from input model dir

    options_s = {"scale_size"}
    with open(os.path.join(input_model, "options.json")) as f:
        for key, val in json.loads(f.read()).items():
            if key in options_s:
                #print("loaded", key, "=", val)
                img_res = int(val)
                print("\nModel Resolution retrieved from Exported Model Data and set to:", img_res, "px\n")



    cam_cap = cv2.VideoCapture(1)
    out__ = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp_out.jpg')
    input_image_queue, output_image_queue, live_process, lifetime_end = serve.process_handler(  input_model,
                                                                                                out__)
    _last = None
    n = 1
    use_preproc = 1

    while (True):
        #print (True)
        ret, frame = cam_cap.read()

      
        #resize

        target_size = img_res
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
        


        #inference

        #write temp file
        temp = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp.jpg')
        cv2.imwrite(temp, frame)


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
        cv2.imshow('Press "q" to close, "s" to Save, "d" to toggle Prepocessing', frame)



        #write image function
        if cv2.waitKey(66) == ord('s'):

            image_file = os.path.join(output_dir, "img_{0}.jpg".format(str(n).zfill(4)))
            cv2.imwrite(image_file, frame)

            print("Snapshot created:", image_file, "\n")

            #increase img counter
            n += 1


        #toggle image preprocesing
        if cv2.waitKey(66) == ord('d'):
            if(use_preproc):
                use_preproc = 0
            else:
                use_preproc = 1 


        #quit process
        if cv2.waitKey(33) == ord('q'):
            #set value to break BG while loop
            lifetime_end.value = True

            for process in live_process:
                #kill process in BG
                process.join()

            #break cv
            break


    #close video capture
    cam_cap.release()




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
                        required=True)

    
    results = parser.parse_args()
    

    #call function
    inference_cam(results.input_model,
                    results.output_dir)