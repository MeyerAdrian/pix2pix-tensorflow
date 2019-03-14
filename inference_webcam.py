
import argparse
import numpy as np
import cv2
import os
import time

import serve
import json

import edge_detect
import face_landmark_detect


def inference_cam(input_model, output_dir, cam_id, cam_width, cam_height, perf_mode, *args):


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


    #cam capture    
    cam_cap = cv2.VideoCapture(cam_id)
    #set res
    cam_cap.set(3, cam_width);
    cam_cap.set(4, cam_height);

    #cam_cap.set(14, 10)



    out__ = os.path.join(os.path.dirname(__file__), '_temp_imgs/temp_out.jpg')
    input_image_queue, output_image_queue, live_process, lifetime_end = serve.process_handler(input_model, out__)


    #vars
    _last = None
    n = 1
    use_preproc = 0
    preproc_mode = 0
    use_zoom = 0
    use_inf = 0



    #resize
    if (img_res == 1024) and (perf_mode == 1):
        target_size = int(img_res / 2)
    else:
        target_size = img_res



    #create bg image first outside loop
    bg_img = face_landmark_detect.create_bg(target_size)


    while (True):
        #print (True)
        ret, frame = cam_cap.read()


        frame_rec = frame.shape
        frame_height = frame_rec[0]
        frame_width = frame_rec[1]
        #print (frame_width, frame_height, target_size)


        if use_zoom == 0:

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

        else:

            width_offset = int((frame_width - target_size) / 2)
            height_offset = int((frame_height - target_size) / 2)

            #crop square
            frame = frame[height_offset:(frame_height-height_offset), width_offset:(frame_width-width_offset)]
            #print (frame.shape)
            #post fix scale
            frame = cv2.resize(frame, (target_size, target_size))
            #print (frame.shape)




        

        #image pre processing, filters
        if use_preproc:
            if preproc_mode == 0:
                frame = face_landmark_detect.face_landmark_detect(frame, bg_img, target_size, 0)

            else:
                frame = edge_detect.edge_detect_filter(frame)
                
        

        #post upscale to match target res
        if (img_res == 1024) and (perf_mode == 1):
            frame = cv2.resize(frame, (img_res, img_res))



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
            
            #check if use inference
            if(use_inf):
                frame = _last
        

        #display
        cv2.imshow('q Close, s Save, d Prepocess, m P. Mode, p Perf. Mode, f Inference, z Zoom', frame)
        key = cv2.waitKey(1) & 0xFF



        #write image function
        if key == ord('s'):

            image_file = os.path.join(output_dir, "img_{0}.png".format(str(n).zfill(4)))
            cv2.imwrite(image_file, frame)

            print("Snapshot created:", image_file, "\n")

            #increase img counter
            n += 1


        #use image preprocesing
        if key == ord('d'):
            if(use_preproc):
                use_preproc = 0
            else:
                use_preproc = 1

        #toggle image preprocesing mode
        if key == ord('m'):
            if(preproc_mode):
                preproc_mode = 0
            else:
                preproc_mode = 1


        #toggle inferenceing
        if key == ord('f'):
            if(use_inf):
                use_inf = 0
            else:
                use_inf = 1 

        #toggle inferenceing
        if key == ord('z'):
            if(use_zoom):
                use_zoom = 0
            else:
                use_zoom = 1 


        #quit process
        if key == ord('q'):
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
                        required=False)
    parser.add_argument('-c', '--cam_id',
                        dest='cam_id',
                        help='Webcam ID',
                        required=False,
                        type=int,
                        default=0)
    parser.add_argument('-x', '--cam_width',
                        dest='cam_width',
                        help='Webcam Px Width',
                        required=False,
                        type=int,
                        default=960)
    parser.add_argument('-y', '--cam_height',
                        dest='cam_height',
                        help='Webcam Px Height',
                        required=False,
                        type=int,
                        default=720)
    parser.add_argument('-p', '--perf_mode', #zoom doesn't work in non_perf_mode yet
                        dest='perf_mode',
                        help='1024Px Performance Mode',
                        required=False,
                        type=int,
                        default=1)

    
    results = parser.parse_args()
    

    #call function
    inference_cam(results.input_model, results.output_dir, results.cam_id, results.cam_width, results.cam_height, results.perf_mode)