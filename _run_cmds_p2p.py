# convert edge detect
py -3 edge_detect_batch.py -i <input_dir> -o <output_dir>

# merge abc images side by side
py -3 merge_sbs.py -a <img_a_dir> -b <img_b_dir> c <img_c_dir> -o <output_dir>



###############################


 # pix2pix train mode
 py -3 pix2pix.py -m train -i <training_input_imgs_dir> -o <checkpoint_output_path> 

# pix2pix export mode
 py -3 pix2pix.py -m export -c <checkpoint_dir> -o <export_model_dir>


# pix2pix inference batch output
py -3 inference_batch.py -m <trained_model_dir> -sbs <1> -i <input_images_path> -il <input_label_images_path> -o <output_images_path> -osbs <output_sbs_images_path>

# pix2pix inference webcam output
py -3 inference_webcam_tf.py -m <trained_model_dir>