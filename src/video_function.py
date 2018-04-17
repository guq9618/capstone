import cv2
import os
import numpy as np
import time
import datetime
from sort import * 
from config import *
from img_function import *
#from tracker import *
def reinit_tracker(frame, hog, _type="hog"):
    tracker = cv2.MultiTracker_create()
    if _type == "hog":
        (rects, weights) = hog.detectMultiScale(frame, winStride=(3,3), padding=(8,8), scale=1.1)
    for rect in rects:
        tracker.add(cv2.TrackerKCF_create(), frame, tuple(rect))

    return tracker
def distance_to_camera(knownWidth, focalLength, perWidth):
    # compute and return the distance from the maker to the camera
    print (knownWidth * focalLength) / perWidth
    return (knownWidth * focalLength) / perWidth


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
	#webcam=cv2.VideoCapture('video_data/video_2018_04_02_11_56_02.avi')
	webcam=cv2.VideoCapture('test/test.avi')
	#webcam=cv2.VideoCapture(0)

	tracker = cv2.MultiTracker_create()
	needHogVerif = 0
	KNOWN_DISTANCE = 24.0

	track_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                    	(0, 255, 255), (255, 0, 255), (255, 127, 255),
			(127, 0, 255), (127, 0, 127)]
	allBoxes=[]
	speedBoxes=[]
	Boxes_feature=[]
	focalLength=0
	HOG_VERIF_TRESH=30
	KNOWN_DISTANCE = 24.0
	KNOWN_WIDTH = 11.0
	MAX_DISTANCE = 10
	isNew=True
	flag=[False,False,False] # is_read,is_detect,is_show
	while True:
		start = time.time()
		now = datetime.datetime.now()
		nowstr=now.strftime('%Y_%m_%d_%H_%M_%S')
		nBox=0

		if flag[0]:
			tmp=time.time()
			wret,wframe=webcam.read()
			
			wframe = cv2.resize(wframe, None, fx=0.5, fy=0.5)

			frame=wframe.copy()
		if flag[1]:
			tmp=time.time()
			ok,boxes=tracker.update(wframe)
			if not ok or boxes is () or needHogVerif>HOG_VERIF_TRESH:
				needHogVerif=0
				cv2.imshow('main',wframe)
				tracker = reinit_tracker(wframe,hog)
				isNew=True
				speedBoxes=[]
				Boxes_feature=[]
				allBoxes=[]
				continue


 			violators = []
    			for i, box in enumerate(boxes):
        			if focalLength == 0:
            				focalLength = ((box[2]+box[0]) * KNOWN_DISTANCE) / KNOWN_WIDTH
				distance = distance_to_camera(KNOWN_WIDTH, focalLength, box[2]+box[0])
        			#distance = (box[0]+box[1]+box[2]+box[3]) / 4
        			l_distance = 0
        			if isNew:
            				allBoxes.append([box])
            				speedBoxes.append([distance])
					Boxes_feature.append(predict_with_write_detections(wframe,[[int(box[0]),int(box[1]),int(box[2]),int(box[3])]],nowstr))
					print Boxes_feature
        			else:
            				l_distance =  abs(speedBoxes[nBox][len(speedBoxes[nBox])-1] - distance)
            				speedBoxes[nBox].append(distance)
            				allBoxes[nBox].append(box)

        			p1 = (int(box[0]), int(box[1]))
        			p2 = (int(box[2])+int(box[0]), int(box[3])+int(box[1]))
	
	        		#cv2.rectangle(wframe, p1, p2, track_colors[i%len(track_colors)], 2)
	        		cv2.rectangle(wframe, p1, p2, (255,255,0), 2)
	
	        		for pbox in allBoxes[nBox]:
	            			pointCor = (int(pbox[0]+pbox[2]/2), int(pbox[1]+pbox[3]))
	            			cv2.circle(wframe, pointCor, 3, (0,0,255), -1)
	
	        		#print(str(box)+" "+str(l_distance))
	        		if l_distance > MAX_DISTANCE:
	            			violators.append((p1,p2))
	        		cv2.putText(wframe,'%.2f'%l_distance,(int(box[0])-20, int(box[1])-30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 3)
	        		cv2.putText(wframe,str(Boxes_feature[i][0]),(int(box[0])+20, int(box[1])+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255),1, cv2.LINE_AA)
	        		#cv2.putText(wframe,str((l_distance)),(int(box[0])-20, int(box[1])-30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,0), 3)
	        		nBox+=1
    			if len(violators)>0:
    	    			for a in violators:
            				cv2.rectangle(wframe, a[0], a[1], (0,0,255), 2)
    			cv2.imshow('main', wframe)
    			if len(violators)>0:
        			#cv2.waitKey(0)
        			#needHogVerif = HOG_VERIF_TRESH
        			violators = []
    			isNew = False
			needHogVerif+=1
			print len(speedBoxes),len(Boxes_feature),nBox




			print 'f0',time.time()-tmp
			'''
			found , w = hog.detectMultiScale(wframe,winStride=(4,4),padding=(50,50),scale=1.1)
			cp_found=[]
			for i,rect in enumerate(found):
				if rect[2] > 50 and rect[3] >50:
					cp_found.append(rect)
			predict_with_write_detections(wframe,cp_found,nowstr)
			'''
			print 'f1',time.time()-tmp


			
		if flag[2]:
			tmp=time.time()
			end=time.time()
			seconds=end-start
			fps= 1/seconds
			cv2.putText(wframe,'fps:'+str(int(fps)),(50,50), font, 1,(255,255,255),2,cv2.LINE_AA)
			cv2.imshow('ori',frame)
			print 'f2',time.time()-tmp
			print 'fps',seconds
			print 'fps',int(fps)
			output.write(wframe)



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


