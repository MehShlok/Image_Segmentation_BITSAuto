# import open cv
import cv2

# load the video using path of video
video_path = "/home/sankabapur/Desktop/Image segmentation /WhatsApp Video 2024-09-03 at 1.38.33 PM.mp4"
video = cv2.VideoCapture(video_path)

success = True
count = 1
image_id = 1

while success:
    success , frame = video.read()
    
    if success == True:
        
        
        # i want every 5th frame from video
        # thats why i used following line of code
        # i dont want all frames from video
        # so we can decide the outpt frames count according to us.
        
        if count%150 == 0: #video is 30 fps so 150 is 5 sec sso 1 image per 5 sec
            
            # specify the output path and file name
            # i used count as a file name
            # you can use any
            name = str(image_id)+".jpg"
            image_id += 1
            
            # save the image
            cv2.imwrite(name,frame)
        
        count += 1
    else:
        break

print("Total Extracted Frames :",image_id)
