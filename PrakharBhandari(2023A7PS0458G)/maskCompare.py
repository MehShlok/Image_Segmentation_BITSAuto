import cv2
import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
output_dir = "./maskCompare"
os.makedirs(output_dir, exist_ok=True)

images = os.listdir("./images")
masks = os.listdir("./output")

for i in range(len(images)):
    image = cv2.imread(f"./images/{images[i]}")
    mask = cv2.imread(f"./output/{masks[i]}")

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(images[i])
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
    plt.title(masks[i])
    plt.axis("off")

    # Save the image
    plt.savefig(f"{output_dir}/{images[i]}")
    plt.close()
