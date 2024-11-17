# Image Segmentation Project - BITS Auto

## Overview
This project focused on developing and testing image segmentation models to accurately identify road areas in photographs from a specific locality. Emphasis was placed on handling challenging conditions such as rainy weather and nighttime images.

## Project Steps

### 1. Image Source
- **Objective**: Gather video data that included a variety of conditions, with a focus on rainy and nighttime scenarios.
- **Method**: Video footage was collected to ensure a diverse dataset, emphasizing challenging weather and lighting conditions.

### 2. Frame Extraction
- **Objective**: Extract individual frames from the video data to create an image dataset for annotation and training.
- **Method**: A custom frame extraction script was used to break down video files into still images. This ensured that enough high-quality and representative frames were available, covering a range of challenging conditions.

### 3. Roboflow Annotation
- **Objective**: Annotate the extracted frames with segmentation masks for training purposes.
- **Method**: The Roboflow platform was used to label images accurately. Specific attention was given to marking 'road' areas in images that included rain and nighttime settings, enhancing the dataset's complexity and variety.

### 4. Roboflow Model Training
- **Objective**: Perform initial model training using Roboflow’s built-in tools.
- **Outcome**: The initial model trained on Roboflow provided foundational results but was insufficient for achieving desired performance levels, leading to further model exploration.

![image](https://github.com/user-attachments/assets/cfc07ffe-1838-4b41-b9b6-de622f767b5c)


### 5. U-Net Model Implementation
- **Objective**: Implement a U-Net architecture to improve segmentation performance.
- **Method**: The U-Net model, known for its strong image segmentation capabilities, was trained on the annotated dataset to enhance accuracy. This step aimed to surpass the baseline results obtained from the Roboflow-trained model.

## Conclusion
The project involved sourcing video data, extracting frames, annotating images, and training models under various conditions, with a particular focus on rainy weather and nighttime challenges. The exploration of different model training approaches, including U-Net, aimed to identify the best-performing solution for road segmentation tasks.
