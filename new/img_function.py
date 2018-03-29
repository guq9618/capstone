import numpy as np
import matplotlib.image as mpimg
import time
import cv2
from config import *
import matplotlib.pyplot as plt
from predict import *
from sklearn.cluster import KMeans

f = open(feature_data_path+start_time_str+'.txt','a')
'''
def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def image_color_cluster(image_path, k = 3):
    plt.figure()
    image = image_path
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.subplot(2,1,1) 
    plt.imshow(image)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
  
    clt = KMeans(n_clusters = k)
    clt.fit(image)

    hist = centroid_histogram(clt)
    #return hist
    print hist,clt.cluster_centers_
    bar = plot_colors(hist, clt.cluster_centers_)
    
    plt.subplot(2,1,2)
    plt.axis("off")
    plt.imshow(bar)
    plt.show()

img=cv2.imread('cover_image.jpg')
image_color_cluster(img)
'''
def predict_with_write_detections(img,rects,nowstr,thickness=1):
	res_data=[]
        for i,  [x,y,w,h] in enumerate(rects):
		#crop img create	
                pad_w,pad_h = int(0.15*w-1),int(0.1*h-1)
		x_min,x_max,y_min,y_max=x+pad_w,x+w-pad_w,y+pad_h,y+h-pad_h
                crop_img=img[y_min:y_max ,x_min:x_max]
		#most_3color=image_color_cluster(crop_img)
                #crop_img=img[y+pad_h:y+h-pad_h ,x+pad_w:x+w-pad_w]
		imwrite_str=img_data_path+'/img'+nowstr+'_%02d'%(i)+'.jpg'
                cv2.imwrite(imwrite_str,crop_img)
		#inception predict		
		res,res_lower=predict_img(imwrite_str)
		res_data.append([res,res_lower])
		res_write_str=imwrite_str+','+str(i)+','+str(x)+','+str(y)+','+str(w)+','+str(h)+','+res+res_lower +'\n'
		f.write(res_write_str)
	#draw 
        for i,  [x,y,w,h] in enumerate(rects):
		res,res_lower=res_data[i]
                pad_w,pad_h = int(0.15*w-1),int(0.1*h-1)
		cv2.putText(img,res+','+res_lower,(x+pad_w,y+(pad_w/2)), font, 0.5,(255,255,255),1,cv2.LINE_AA)

                cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
