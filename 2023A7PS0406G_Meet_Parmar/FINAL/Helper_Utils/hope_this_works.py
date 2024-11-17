import os
import time
import subprocess
import gc
import tensorflow as tf


# Directory where the images are located
image_dir = r"C:\Users\parma\Downloads\DataSet"

# List all files in the directory
files = os.listdir(image_dir)

# Filter files that match the pattern 'i.jpg'
image_files = [f for f in files if f.endswith('.jpg')]

# Path to the script you want to run
# script_path = "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\tools\test_lanenet.py"

# Define the batch size
batch_size = 4
num_images = len(image_files)
tf.keras.backend.clear_session()
gc.collect()
# Loop through each batch
for batch_start in range(0, num_images, batch_size):
    batch = image_files[batch_start:batch_start + batch_size]
    
    # Process each image in the batch
    for image_file in batch:
        image_path = os.path.join(image_dir, image_file)
        cmd = fr'python "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\tools\test_lanenet.py" --weights_path "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\weights\tusimple_lanenet\tusimple_lanenet.ckpt" --image_path {image_path} --with_lane_fit 0'
        
        # Run the command using subprocess with shell=True
        subprocess.run(cmd, shell=True)
    
    # Optional: Add a delay or memory clear operation here if needed, especially for large batches.
    tf.keras.backend.clear_session()
    gc.collect()
    time.sleep(2)  # Uncomment to add a short delay between batches
