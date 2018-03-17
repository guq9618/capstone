import cv2
import os
import numpy as np
import datetime
from config import *
from img_function import *

if not os.path.isdir(img_data_path):
	os.mkdir(img_data_path)

#webcam init
webcam=cv2.VideoCapture('test/test.avi')
#webcam=cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
output = cv2.VideoWriter(video_data_path+'video_'+start_time_str+'.avi', fourcc, 20.0, (640,480) )



#ui init
init_img = cv2.imread('cover_image.jpg')
init_img= cv2.resize(init_img,(640,480))
cv2.imshow('main',init_img)


hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	

flag=[False,False,False] # is_read,is_detect,is_show
while True:
	now = datetime.datetime.now()
	nowstr=now.strftime('%Y_%m_%d_%H_%M_%S')
	if flag[0]:
		wret,wframe=webcam.read()
		wframe = cv2.resize(wframe, None, fx=0.5, fy=0.5)

		found , w = hog.detectMultiScale(wframe,winStride=(4,4),padding=(50,50),scale=1.15)
	if flag[1]:
		predict_with_write_detections(wframe,found,nowstr)
		#output.write(wframe)
	if flag[2]:
		cv2.imshow('main',wframe)




	key = cv2.waitKey(1)&0xFF

	if key == ord('q'):
		print flag
		break
	elif key == ord('w'):
		flag[1]= not flag[1]		
		flag[0] = flag[1] or flag[2]
		print flag
	elif key == ord('e'):
		flag[2]= not flag[2]		
		flag[0] = flag[1] or flag[2]
		print flag

webcam.release()
output.release()
cv2.destroyAllWindows()
