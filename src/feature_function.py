# -*- coding: utf-8 -*- 
import tensorflow as tf
import numpy as np
import sys,os
import cv2
from sklearn.cluster import KMeans
tf.app.flags.DEFINE_string("output_graph",
                           "./workspace/output_graph.pb",
                           "상의 데이터 학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("output_labels",
                           "./workspace/output_labels.txt",
                           "상의 데이터 학습할 레이블 데이터 파일")
FLAGS = tf.app.flags.FLAGS

labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.output_labels)]
with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')
sess=tf.Session()

#logits = sess.graph.get_tensor_by_name('final_result:0')
def predict_img(img):
    
	tf.reset_default_graph()
        logits = sess.graph.get_tensor_by_name('final_result:0')
    	image = tf.gfile.FastGFile(img, 'rb').read()

    	prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})
	res_index= np.argmax(prediction[0])
	return labels[res_index]





def hsv_classification(test_color):
    hue,lgt,sat=test_color
    hue,lgt,sat=hue*2,lgt/255,sat/255
    #print hue,sat,lgt
    if (lgt < 0.25):
        return "Black"
    elif (lgt > 0.75):
        return "White"

    if (sat < 0.1):
        return "Gray"

    elif (hue <= 30) or (hue>330) :
        return "Red"
    elif (hue <= 75)   :
        return "Yellow"
    elif (hue <= 160)  :
        return "Green"
    elif (hue <= 210)  :
        return "Cyan"
    elif (hue <= 270)  :
        return "Blue"
    elif (hue <= 300)  :
        return "Violet"
    elif (hue <= 330)  :
        return "Pink"

def hsv2str_colors(test_colors):
        arr=[]
        for color in test_colors:
                arr.append(hsv_classification(color))
        return arr

def image_color_cluster(image_path, k = 3):
    image = image_path
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)


    w,h,rgb=image.shape
    w,h=w/3,h/3
    img = image.reshape((image.shape[0] * image.shape[1], 3))


    clt = KMeans(n_clusters = k).fit(img)

    most_3color=clt.cluster_centers_
    hsv2str=hsv2str_colors(most_3color)
    return list(set(hsv2str))
