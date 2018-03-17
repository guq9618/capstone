import cv2
from config import *
from predict import *

f = open(feature_data_path+start_time_str+'.txt','a')

def predict_with_write_detections(img,rects,nowstr,thickness=1):
        for i,  [x,y,w,h] in enumerate(rects):
                pad_w,pad_h = int(0.15*w-1),int(0.1*h-1)
                crop_img=img[y+pad_h:y+h-pad_h ,x+pad_w:x+w-pad_w]
		imwrite_str=img_data_path+'/img'+nowstr+'_%02d'%(i)+'.jpg'
                cv2.imwrite(imwrite_str,crop_img)
			
		res=predict_img(imwrite_str)
		res_write_str=imwrite_str+','+str(i)+','+str(x)+','+str(y)+','+str(w)+','+str(h)+','+res+'\n'
		f.write(res_write_str)
		
                cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
