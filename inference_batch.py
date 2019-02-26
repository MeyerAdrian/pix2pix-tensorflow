
import tensorflow as tf
import numpy as np
import argparse
import os
import json
import glob
import random
import collections
import math
import time
import base64

import merge_sbs_batch


def local_inference(input_model, use_sbs, input_dir, input_dir_label, output_dir, output_dir_sbs, *args):
    
    print ("local inference started")
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True


    with tf.Session(config=config) as sess:

        print ("local inference session started with {0}".format('inference'))
        model = input_model
        saver = tf.train.import_meta_graph(model + "/export.meta")
        saver.restore(sess, model + "/export")
        input_vars = json.loads(tf.get_collection("inputs")[0].decode('utf-8'))
        output_vars = json.loads(tf.get_collection("outputs")[0].decode('utf-8'))
        
        _input = tf.get_default_graph().get_tensor_by_name(input_vars["input"])
        output = tf.get_default_graph().get_tensor_by_name(output_vars["output"])


        ##### get res from input model dir

        options_s = {"scale_size"}
        with open(os.path.join(input_model, "options.json")) as f:
            for key, val in json.loads(f.read()).items():
                if key in options_s:
                    #print("loaded", key, "=", val)
                    img_res = int(val)
                    print("\nModel Resolution retrieved from Exported Model Data and set to:", img_res, "px\n")


        #iterate through a directory if images
        for i in os.listdir(input_dir):
            input_file = os.path.join(input_dir, i)

            start = time.time()
            print ("local inference get {0}".format(input_file))
            # if input_file:
            with open(input_file, "rb") as f:
                input_data = f.read()

            input_instance = dict(_input=base64.urlsafe_b64encode(input_data).decode("ascii"), key="0")
            input_instance = json.loads(json.dumps(input_instance))

            input_value = np.array(input_instance["_input"])
            output_value = sess.run(output, feed_dict={_input: np.expand_dims(input_value, axis=0)})[0]

            output_instance = dict(output=output_value.decode("ascii"), key="0")
        
            b64data = output_instance["output"]
            b64data += "=" * (-len(b64data) % 4)
            output_data = base64.urlsafe_b64decode(b64data.encode("ascii"))
            
            # set to png and write 

            output_file = os.path.join(output_dir, i.replace(".jpg", ".png"))
            with open(output_file, "wb") as f:
                print ("local inference open file {0}".format(output_file))
                f.write(output_data)

            print ("local inference sent {0}".format(output_file))
            print (time.time() - start)


    #merge sbs images

    if (use_sbs == 1):
        merge_sbs_batch.merge_sbs_batch(input_dir, input_dir_label, output_dir, output_dir_sbs)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pix2Pix Inference Module')
    parser.add_argument('-m', '--input_model',
                        dest='input_model',
                        help='Input Model',
                        required=True)
    parser.add_argument('-sbs', '--use_sbs',
                        dest='use_sbs',
                        help='Make SBS Images as well',
                        type=int,
                        required=False,
                        default=0)
    parser.add_argument('-i', '--input',
                        dest='input_dir',
                        help='Input IMG Directory',
                        required=True)
    parser.add_argument('-il', '--input_dir_label',
                        dest='input_dir_label',
                        help='Input Label IMG Directory',
                        required=False)
    parser.add_argument('-o', '--output',
                        dest='output_dir',
                        help='Output IMG Directory',
                        required=True)
    parser.add_argument('-osbs', '--output_dir_sbs',
                        dest='output_dir_sbs',
                        help='Output SBS IMG Directory',
                        required=False)

    
    results = parser.parse_args()
    
    
    local_inference(results.input_model,
                    results.use_sbs,
                    results.input_dir, 
                    results.input_dir_label,
                    results.output_dir,
                    results.output_dir_sbs)