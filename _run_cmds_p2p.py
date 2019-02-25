# convert edge detect
py -3 edge_detect_batch.py -i <input_dir> -o <output_dir>

# merge abc images side by side
py -3 merge_sbs.py -a <img_a_dir> -b <img_b_dir> c <img_c_dir> -o <output_dir>



###############################


 # pix2pix train mode
 py -3 pix2pix.py --mode train --input_dir <training_input_dir> --output_dir <checkpoint_output_path> --max_epochs 200 --which_direction BtoA --res <res>

# pix2pix export mode
 py -3 pix2pix.py --mode export --output_dir <export_model_dir> --checkpoint <checkpoint_dir> --which_direction BtoA --res <res>


# pix2pix inference output
py -3 inference.py -m <trained_model_dir> -i <input_path> -o <output_path> -r <res>