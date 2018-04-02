import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2
black=[0,0,0]
red=[255,0,0]
green=[0,255,0]
blue=[0,0,255]
yellow=[255,255,0]
pink=[255,0,255]
cyan=[0,255,255]
white=[255,255,255]
color_list=np.array([black,red,green,blue,yellow,pink,cyan,white])
color_name_list=np.array(['black','red','green','blue','yello','pink','cyan','white'])

def hsv_classification(test_color):
    hue,lgt,sat=test_color
    hue,lgt,sat=hue*2,lgt/255,sat/255
    #print hue,sat,lgt
    if (lgt < 0.25):
	return "Blacks"
    elif (lgt > 0.75):
	return "Whites"

    if (sat < 0.1):
	return "Grays"

    if (hue <= 30) or (hue>330) : 
	return "Reds"
    if (hue <= 75)   :
	return "Yellows"
    if (hue <= 160)  :
	return "Greens"
    if (hue <= 210)  :
	return "Cyans"
    if (hue <= 270)  :
	return "Blues"
    if (hue <= 300)  :
	return "violet"
    if (hue <= 330)  :
	return "pink"

def hsv2str_colors(test_colors):
	arr=[]
	for color in test_colors:
		arr.append(hsv_classification(color))
	return arr

def image_color_cluster(image_path, k = 3):
    from matplotlib.colors import hsv_to_rgb
    image = image_path
    #test=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    #plt.imshow(test)
    #plt.show()
    #image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
    w,h,rgb=image.shape
    w,h=w/3,h/3
    #image = image[w:2*w,h:2*h]
    img = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters = k)
    clt.fit(img)
    most_3color=clt.cluster_centers_
    hsv2str=hsv2str_colors(most_3color)
    #print most_3color
    #print hsv2str
    return list(set(hsv2str))



#img=cv2.imread('test1.jpg')
#print image_color_cluster(img)



