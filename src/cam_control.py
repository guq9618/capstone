import cv2
import numpy as np
from PIL import Image, ImageDraw
from multiprocessing import Process
import datetime

now = datetime.datetime.now()
nowstr=now.strftime('%Y_%m_%d_%H_%M_%S')
img_data_path='./img_data'
video_data_path='./video_data'
feature_data_path='./feature_data'


#webcam init
webcam=cv2.VideoCapture('test/test.avi')
#webcam=cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
output = cv2.VideoWriter( 'video_data/video_'+nowstr+'.avi', fourcc, 20.0, (640,480) )
flag=[False,False,False] # is_read,is_write,is_show



#ui init
init_img = cv2.imread('cover_image.jpg')
init_img= cv2.resize(init_img,(640,480))
cv2.imshow('main',init_img)


hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def draw_detections(img,rects,thickness = 1):
	for x,y,w,h in rects:
		pad_w,pad_h = int(0.15*w),int(0.05*h)
		cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)

def write_detections(img,rects,thickness = 1):
	'''
	cnt=0
	for x,y,w,h in rects:
		pad_w,pad_h = int(0.15*w),int(0.05*h)
		crop_img=img[y+pad_h:y+h-pad_h,x+pad_w:x+w-pad_w]
		cv2.imwrite(nowstr+str(cnt),crop_img)
		cnt+=1
	'''
	pass

	
while True:
	now = datetime.datetime.now()
	nowstr=now.strftime('%Y_%m_%d_%H_%M_%S')
	if flag[0]:
		wret,wframe=webcam.read()

		found , w = hog.detectMultiScale(wframe,winStride=(8,8),padding=(32,32),scale=1.05)
		draw_detections(wframe,found)
	if flag[1]:

		for i , rect in enumerate(found):
			crop_img=wframe[rect[1]:rect[1]+rect[3] ,rect[0]:rect[0]+rect[2]]
			cv2.imwrite('./img_data/img'+nowstr+'_%02d'%(i)+'.jpg',crop_img)
		output.write(wframe)
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
