
import argparse
import numpy as np
import cv2
import os
import time

import edge_detect
import serve

def inference_cam(input_model, res, *args):

    cam_cap = cv2.VideoCapture(1)
    out__ = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp_out.jpg')
    input_image_queue, output_image_queue, live_process, lifetime_end = serve.process_handler(  input_model,
                                                                                                out__)
    _last = None
    while (True):
        #print (True)
        ret, frame = cam_cap.read()

        #resize

        target_size = int(res)
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


        #fix that shit
        frame = cv2.resize(frame, (target_size, target_size))


        #image pre processing...

        frame = edge_detect.edge_detect_filter(frame)
        #print (frame.shape)


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
        cv2.imshow('Press "q" to close', frame)

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
    parser.add_argument('-r', '--res',
                        dest='res',
                        help='Image Resolution',
                        required=False,
                        choices=["256", "512", "1024"],
                        default="256")

    
    results = parser.parse_args()
    

    #call function
    inference_cam(results.input_model,
                    results.res)