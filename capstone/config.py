import cv2
import datetime
import os

start_time = datetime.datetime.now()
start_time_str=start_time.strftime('%Y_%m_%d_%H_%M_%S')

video_data_path='./video_data/'
img_data_path='./img_data/'+start_time_str
feature_data_path='./feature_data/'
log_data_path='./log_data/'


if not os.path.isdir(img_data_path):
        os.mkdir(img_data_path)



font = cv2.FONT_HERSHEY_SIMPLEX

hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
