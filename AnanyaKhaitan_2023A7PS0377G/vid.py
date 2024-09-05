import cv2
from ultralytics import SAM
from ultralytics import FastSAM
import numpy as np
import matplotlib.pyplot as plt

#extraction of images from a video

for j in range(5):
    cam=cv2.VideoCapture("vid"+str(j)+".mp4")
    fps=24
    n=0
    i=0
    while True:
        ret,frame=cam.read()
        if (0.25*n)%fps==0:
            cv2.imwrite("./images/"+str(j)+"-{}.jpg".format(i),frame)
            i+=1
        n+=1
        if ret == False:
            break
    cam.release()
    cv2.destroyAllWindows()

#Using SAM for segmenting the images

# model = FastSAM("FastSAM-s.pt")
# for m in range(15):
#   results = model.predict(source="./images/"+str(m)+".jpg")   
#   masks = results[0].masks.data
#   masks = masks.cpu().numpy()
#   image = cv2.imread("./images/"+str(m)+".jpg")
#   my_mask = np.zeros((masks.shape[1], masks.shape[2]))
#   for i in range(masks.shape[0]):
#       for j in range(masks.shape[1]):
#           for k in range(masks.shape[2]):
#               if masks[i][j][k]:
#                   my_mask[j][k] = i
#   plt.imshow(my_mask)
#   plt.savefig("./images/mask"+str(m)+".png")
