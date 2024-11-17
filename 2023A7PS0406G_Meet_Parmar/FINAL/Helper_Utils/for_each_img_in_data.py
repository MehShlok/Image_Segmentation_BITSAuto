import os
import subprocess

# Directory where the images are located
image_dir = r"C:\Users\parma\Downloads\UNet-PyTorch-main\UNet-PyTorch-main\data"

# List all files in the directory
files = os.listdir(image_dir)

# Filter files that match the pattern 'i.jpg'
image_files = [f for f in files if f.endswith('.jpg')]

# Path to the script you want to run
# script_path = "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\tools\test_lanenet.py"
itr = 0 
# Loop through each image file and run the script with its path as an argument
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    temp = os.path.splitext(image_file)[0]
    cmd = fr'python "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\tools\test_lanenet.py" --weights_path "C:\Users\parma\Downloads\lanenet-lane-detection-master (1)\lanenet-lane-detection-master\weights\tusimple_lanenet\tusimple_lanenet.ckpt" --image_path {image_path} --with_lane_fit 0'
    # Run the command using subprocess with shell=True
    subprocess.run(cmd, shell=True)
