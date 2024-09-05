
# Authored By :  Meoweet



import cv2
import os
import choosing_vid_path as cvp
# import numpy as np

def process_vid(cap,j) :
    # take every 10 th frame
    if not cap.isOpened():
        raise Exception(f"Error: Could not open video ")
    
    limit =300
    for i in range(0,int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),10) :
        if(i>limit ):
            break
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if(ret) :
            #save the image in a new dir
            if not os.path.exists("./DataSet") :
                os.makedirs("./DataSet") 
            #j is the video number and i is the frame number
            cv2.imwrite(f"./DataSet/{j}_{i}.jpg",frame)
    


def loop_vids(k) :
    # k is the number of videos to process
    for j in range (1,k+1) :
        cap = cvp.load_vids(j)
        process_vid(cap,j)
        cap.release()


loop_vids(8)
