import numpy as np
import time
import cv2
from config import *
from feature_function import *
#from colors import *

f = open(feature_data_path+start_time_str+'.txt','a')


def predict_with_write_detections(img,rects,nowstr,thickness=1):
	res_data=[]
        for i,  [x,y,w,h] in enumerate(rects):
		print x,y,w,h
		#crop img create	
                pad_w,pad_h = int(0.15*w-1),int(0.1*h-1)
		x_min,x_max,y_min,y_max=x+pad_w,x+w-pad_w,y+pad_h,y+h-pad_h
                crop_img=img[y_min:y_max ,x_min:x_max]

		#save
		imwrite_str=img_data_path+'/img'+nowstr+'_%02d'%(i)+'.jpg'
                cv2.imwrite(imwrite_str,crop_img)
		#feature data	
		colors=image_color_cluster(crop_img)
		res=predict_img(imwrite_str)
		res_data.append([res,colors])
		res_write_str=imwrite_str+' '+res+' '+' '.join(colors)+'\n'
		f.write(res_write_str)
	
	print 'shape',(res_data[0])
	return res_data[0]
	#draw 
        #for i,  [x,y,w,h] in enumerate(rects):
		#res,colors=res_data[i]
                #pad_w,pad_h = int(0.15*w-1),int(0.1*h-1)
		#cv2.putText(img,res,(x+pad_w,y+(pad_w/2)), font, 0.5,(255,255,255),1,cv2.LINE_AA)
		#cv2.putText(img,",".join(colors),(x+pad_w,y+h), font, 0.5,(255,255,255),1,cv2.LINE_AA)
                #cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)


