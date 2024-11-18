# # import json
# # from PIL import Image
# # import os

# # # Load your coco.json file
# # with open(
# #     "./PrakharBhandari(2023A7PS0458G)/dataset/Roads.v4i.coco/train/_annotations.coco.json",
# #     "r",
# # ) as f:
# #     coco_data = json.load(f)

# # # Define the folder where your images are stored
# # image_folder = "./PrakharBhandari(2023A7PS0458G)/dataset/Roads.v4i.coco/train/_annotations.coco.json"

# # # Loop through each image entry in the COCO data
# # for image_info in coco_data["images"]:
# #     file_name = image_info["file_name"]

# #     # Create the full path to the image
# #     image_path = os.path.join(image_folder, file_name)

# #     # Open the image using PIL
# #     try:
# #         img = Image.open(image_path)

# #         # Save the image in JPG format (even if it's already in JPG, this will re-save it)
# #         output_path = os.path.join(image_folder, f"converted_{file_name}")
# #         img.convert("RGB").save(output_path, "JPEG")
# #         print(f"Saved {file_name} as {output_path}")

# #     except Exception as e:
# #         print(f"Error processing {file_name}: {e}")


# import json
# import numpy as np
# from PIL import Image, ImageDraw
# from pycocotools.coco import COCO

# # File paths
# coco_file_path = "./PrakharBhandari(2023A7PS0458G)/dataset/Roads.v4i.coco/train/_annotations.coco.json"
# output_mask_path = "road_mask.jpg"

# # Load the COCO file
# with open(coco_file_path, "r") as f:
#     coco_data = json.load(f)

# # Initialize COCO object
# coco = COCO(coco_file_path)

# # Find the category ID for the road label
# road_category_id = None
# for category in coco_data["categories"]:
#     if category["name"].lower() == "road":
#         road_category_id = category["id"]
#         break

# if road_category_id is None:
#     print("Road category not found in the COCO file.")
#     exit()

# # Filter annotations for the road category
# road_annotations = [
#     ann for ann in coco_data["annotations"] if ann["category_id"] == road_category_id
# ]

# # Get the image information
# image_info = coco_data["images"][0]  # Assuming a single image in COCO file
# image_width = image_info["width"]
# image_height = image_info["height"]

# # Create an empty mask
# mask = Image.new("L", (image_width, image_height), 0)  # 'L' mode for grayscale

# # Draw the mask
# draw = ImageDraw.Draw(mask)
# for ann in road_annotations:
#     # Use segmentation if available
#     if "segmentation" in ann and ann["segmentation"]:
#         for seg in ann["segmentation"]:
#             polygon = [(seg[i], seg[i + 1]) for i in range(0, len(seg), 2)]
#             draw.polygon(polygon, fill=128)  # Gray color
#     # Or use the bounding box
#     elif "bbox" in ann:
#         x, y, width, height = ann["bbox"]
#         draw.rectangle([x, y, x + width, y + height], fill=128)  # Gray color

# # Save the grayscale mask
# mask.save(output_mask_path)
# print(f"Road mask saved as {output_mask_path}")


import json
import numpy as np
from PIL import Image, ImageDraw
from pycocotools.coco import COCO

# File paths
coco_file_path = "./PrakharBhandari(2023A7PS0458G)/dataset/Roads.v4i.coco/train/_annotations.coco.json"
output_folder = "output/"  # Folder to save the output images

# Load the COCO file
with open(coco_file_path, "r") as f:
    coco_data = json.load(f)

# Initialize COCO object
coco = COCO(coco_file_path)

# Find the category ID for the road label
road_category_id = None
for category in coco_data["categories"]:
    if category["name"].lower() == "road":
        road_category_id = category["id"]
        break

if road_category_id is None:
    print("Road category not found in the COCO file.")
    exit()

# Process each image that has road annotations
for image_info in coco_data["images"]:
    image_id = image_info["id"]
    image_width = image_info["width"]
    image_height = image_info["height"]

    # Filter road annotations for the current image
    road_annotations = [
        ann
        for ann in coco_data["annotations"]
        if ann["category_id"] == road_category_id and ann["image_id"] == image_id
    ]

    # Create an empty grayscale mask
    mask = Image.new(
        "L", (image_width, image_height), 0
    )  # 'L' mode for grayscale (0 = black)
    draw = ImageDraw.Draw(mask)

    # Draw road segments on the mask
    for ann in road_annotations:
        if "segmentation" in ann and ann["segmentation"]:
            for seg in ann["segmentation"]:
                polygon = [(seg[i], seg[i + 1]) for i in range(0, len(seg), 2)]
                draw.polygon(polygon, fill=128)  # Fill road areas with gray (128)
        elif "bbox" in ann:
            x, y, width, height = ann["bbox"]
            draw.rectangle(
                [x, y, x + width, y + height], fill=128
            )  # Fill bounding box with gray (128)

    # Save the mask image as JPEG
    output_mask_path = (
        f"{output_folder}{image_info['file_name'].replace('.jpg', '_road_mask.jpg')}"
    )
    mask.save(output_mask_path)
    print(f"Road mask saved as {output_mask_path}")
