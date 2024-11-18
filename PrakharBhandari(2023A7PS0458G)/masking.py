import json
import numpy as np
import skimage
import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image


# Function to convert TIFF to JPEG
def convert_tiff_to_jpg(tiff_path, jpg_path):
    try:
        # Open the TIFF image using PIL
        with Image.open(tiff_path) as img:
            # Convert the image to RGB (JPEG doesn't support transparency, so we need RGB mode)
            img = img.convert("RGB")
            # Save the image as JPEG
            img.save(jpg_path, "JPEG")
            print(f"Converted {tiff_path} to {jpg_path}")
    except Exception as e:
        print(f"Error converting {tiff_path} to {jpg_path}: {e}")


# python inference.py --src ../vid.mp4  --model models/pretrained_models/road_segmentation_160_160.h5
# Function to create a mask for each image
def create_mask(image_info, annotations, output_folder):
    # Create an empty mask as a numpy array (Ensure it has the right shape)
    mask_np = np.zeros(
        (image_info["height"], image_info["width"]), dtype=np.uint8
    )  # Changed dtype to uint8 for JPG

    # Counter for the object number
    object_number = 1

    for ann in annotations:
        if ann["image_id"] == image_info["id"]:
            if (
                "segmentation" in ann and ann["segmentation"]
            ):  # Check if segmentation data exists
                # Extract segmentation polygon
                for seg in ann["segmentation"]:
                    if (
                        len(seg) < 6
                    ):  # Skip invalid segments (e.g., too few points to form a polygon)
                        continue

                    # Convert polygons to a binary mask
                    try:
                        # Polygon expects [y1, x1, y2, x2, ..., yn, xn]
                        rr, cc = skimage.draw.polygon(
                            seg[1::2], seg[0::2], mask_np.shape
                        )
                        mask_np[rr, cc] = object_number
                        object_number += 1  # We are assigning each object a unique integer value (labeled mask)
                    except Exception as e:
                        print(
                            f"Error in drawing polygon for annotation {ann['id']}: {e}"
                        )
            else:
                print(f"No segmentation data for image {image_info['file_name']}")

    # Ensure the mask is saved with a .jpg extension, regardless of the original image extension
    mask_filename = (
        image_info["file_name"].split(".")[0] + "_mask.jpg"
    )  # Changed to .jpg extension
    mask_path = os.path.join(output_folder, mask_filename)

    # Check if the mask is non-empty
    if np.count_nonzero(mask_np) > 0:
        # Save the mask as JPEG using PIL (scaled to 255 for visibility)
        mask_image = Image.fromarray(
            mask_np * 255
        )  # Multiply by 255 to make it visible in the saved image
        mask_image.convert("RGB").save(mask_path, "JPEG")  # Save as JPEG

        # Optionally display the mask in the notebook
        plt.imshow(mask_np, cmap="jet")
        plt.title(f"Mask for {image_info['file_name']}")
        plt.axis("off")
        # plt.show()

        print(f"Saved mask for {image_info['file_name']} to {mask_path}")
    else:
        print(f"Mask for {image_info['file_name']} is empty. Not saved.")


# Main function to process images and masks
def main(json_file, mask_output_folder, image_output_folder, original_image_dir):
    # Load COCO JSON annotations
    with open(json_file, "r") as f:
        data = json.load(f)

    images = data["images"]
    annotations = data["annotations"]

    # Ensure the output directories exist
    if not os.path.exists(mask_output_folder):
        os.makedirs(mask_output_folder)
    if not os.path.exists(image_output_folder):
        os.makedirs(image_output_folder)

    # Process each image
    for img in images:
        # Create the masks
        create_mask(img, annotations, mask_output_folder)

        # Original image path
        original_image_path = os.path.join(original_image_dir, img["file_name"])

        # Ensure the image is in JPG format
        if original_image_path.lower().endswith(".tif"):
            # Generate the new JPG file path
            jpg_filename = img["file_name"].replace(".tif", ".jpg")
            jpg_path = os.path.join(image_output_folder, jpg_filename)

            # Convert the TIFF to JPEG and save it
            convert_tiff_to_jpg(original_image_path, jpg_path)
            new_image_path = jpg_path  # Update the new image path to the converted JPG
        else:
            # If it's already a JPG, simply copy it
            new_image_path = os.path.join(
                image_output_folder, os.path.basename(original_image_path)
            )
            shutil.copy2(original_image_path, new_image_path)

        print(f"Copied original image to {new_image_path}")


if __name__ == "__main__":
    # Mount Google Drive
    # Google Drive file path
    # original_image_dir = "/content/drive/My Drive/Assignment_3/bits-vertical-road.v1i.coco/train"  # Update this path as needed
    original_image_dir = "./dataset/Roads.v4i.coco/train"  # Update this path as needed
    json_file = "./dataset/Roads.v4i.coco/train/_annotations.coco.json"  # Update this path as needed
    mask_output_folder = "./dataset/Roads.v4i.coco/train/train_masks"  # Modify this as needed  # Modify this as needed
    image_output_folder = "./dataset/Roads.v4i.coco/train/images"  # Modify this as needed  # Modify this as needed

    main(json_file, mask_output_folder, image_output_folder, original_image_dir)
