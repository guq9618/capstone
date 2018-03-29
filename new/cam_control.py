import cv2
import os
import numpy as np
import time
import datetime
from config import *
from img_function import *



def webcam_control():
	write_start_time=datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
	fourcc = cv2.VideoWriter_fourcc(*'XVID')  
	output = cv2.VideoWriter(video_data_path+'video_'+write_start_time +'.avi', fourcc, 20.0, (640,480) )
	
	
	

	#ui init
	init_img = cv2.imread('cover_image.jpg')
	init_img= cv2.resize(init_img,(640,480))
	cv2.imshow('main',init_img)
	print 'ui init'
	
	
	
			
	#webcam init
	#webcam=cv2.VideoCapture('test/test.avi')
	webcam=cv2.VideoCapture(0)

	flag=[False,False,False] # is_read,is_detect,is_show
	while True:
		
		start = time.time()
		now = datetime.datetime.now()
		nowstr=now.strftime('%Y_%m_%d_%H_%M_%S')
		if flag[0]:
			tmp=time.time()
			wret,wframe=webcam.read()
			wframe = cv2.resize(wframe, None, fx=0.5, fy=0.5)
			found , w = hog.detectMultiScale(wframe,winStride=(4,4),padding=(50,50),scale=1.1)
			cp_found=[]
			for i,rect in enumerate(found):
				if rect[2] > 50 and rect[3] >50:
					cp_found.append(rect)
			print 'f0',time.time()-tmp
		if flag[1]:
			tmp=time.time()
			predict_with_write_detections(wframe,cp_found,nowstr)
			print 'f1',time.time()-tmp
		if flag[2]:
			tmp=time.time()
			end=time.time()
			seconds=end-start
			fps= 1/seconds
			cv2.putText(wframe,'fps:'+str(int(fps)),(50,50), font, 1,(255,255,255),2,cv2.LINE_AA)
			cv2.imshow('main',wframe)
			print 'f2',time.time()-tmp
		#control
		key = cv2.waitKey(1)&0xFF
	
		if key == ord('q'):
			print 'exit'
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


