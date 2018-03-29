import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import cv2
White=[255,255,255]
Grey=[128,128,128]
Black=[0,0,0]
Brown=[165,42,42]
Red=[250,5,5]
Orange=[255,165,0]
Yellow=[255,255,0]
Light_green=[144,238,144]
Green=[0,255,0]
Cyan=[0,255,255]
Sky_blue=[135,206,235]
Blue=[0,0,255]
Navy=[0,0,128]
Purple=[128,0,128]
Pink=[255,105,180]

color_list=np.array([White,Grey,Black,Brown,Red,Orange,Yellow,Light_green,Green,Cyan,Sky_blue,Blue,Navy,Purple,Pink])

color_name_list=np.array(['White','Grey','Black','Brown','Red','Orange','Yellow','Light_green','Green','Cyan','Sky_blue','Blue','Navy','Purple','Pink'])


def color_name_classification(test_colors):
	res=[]
	for test_color in test_colors:
		sub_list=[]
		for i,color in enumerate(color_list):
			#sub=abs(color-test_color)
			#sub_list.append(np.mean(sub))
			dist=np.linalg.norm(color-test_color)
			sub_list.append(dist)
			#print test_color,color_name_list[i],np.mean(sub)
			print test_color,color_name_list[i],dist
		res.append(color_name_list[np.argmin(sub_list)])
	return res

def image_color_cluster(image_path, k = 3):
    image = image_path
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image)
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    clt = KMeans(n_clusters = k)
    clt.fit(image)
    most_3color=clt.cluster_centers_
    #print most_3color
    #hist = centroid_histogram(clt)
    rgb2str=color_name_classification(most_3color)
    
    plt.show()
    print rgb2str
    return rgb2str

#test
#image=cv2.imread('test.jpg')
#image_color_cluster(image)
