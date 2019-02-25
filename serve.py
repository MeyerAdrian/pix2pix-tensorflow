
import numpy as np
import multiprocessing as mp
import tensorflow as tf
import json
import base64
import ctypes
import time
import socket

def process_handler(model, output_file, *args):
    live_process = []
    manager = mp.Manager()
    lifetime_end = manager.Value(ctypes.c_char_p, False)
    input_image_queue, output_image_queue = [mp.Queue() for _ in range(2)]
    img_cap_process = mp.Process(target=local_inference,
                                 args=(input_image_queue,
                                       output_image_queue,
                                       lifetime_end,
                                       model,
                                       output_file,
                                       ))
    
    live_process.append(img_cap_process)

    img_cap_process.start()
    
    return input_image_queue, output_image_queue, live_process, lifetime_end

def local_inference(input_image_queue,
                    output_image_queue,
                    lifetime_end,
                    model,
                    output_file,
                    *args):
    

    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(config=config) as sess:

        saver = tf.train.import_meta_graph(model + "/export.meta")
        saver.restore(sess, model + "/export")
        
        input_vars = json.loads(tf.get_collection("inputs")[0].decode('utf-8'))
        output_vars = json.loads(tf.get_collection("outputs")[0].decode('utf-8'))
        
        _input = tf.get_default_graph().get_tensor_by_name(input_vars["input"])
        output = tf.get_default_graph().get_tensor_by_name(output_vars["output"])
        while True:
            if not input_image_queue.empty():
                input_file = input_image_queue.get()
                try:
                    start = time.time()
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
                                
                    with open(output_file, "wb") as f:
                        f.write(output_data)
                    
                    output_image_queue.put(output_file)
                    print ('takes: ', time.time() - start)
                except Exception as e:
                    pass
            if lifetime_end.value:
                break