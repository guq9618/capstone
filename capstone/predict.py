# -*- coding: utf-8 -*- 
import time
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys,os

tf.app.flags.DEFINE_string("output_graph",
                           "./workspace/flowers_graph.pb",
                           "학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("output_labels",
                           "./workspace/flowers_labels.txt",
                           "학습할 레이블 데이터 파일")
tf.app.flags.DEFINE_string("upper_graph",
                           "./workspace/upper_graph.pb",
                           "상의 데이터 학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("upper_labels",
                           "./workspace/upper_labels.txt",
                           "상의 데이터 학습할 레이블 데이터 파일")
tf.app.flags.DEFINE_string("lower_graph",
                           "./workspace/lower_graph.pb",
                           "하의 데이터 학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("lower_labels",
                           "./workspace/lower_labels.txt",
                           "하의 데이터 학습할 레이블 데이터 파일")
tf.app.flags.DEFINE_string("full_graph",
                           "./workspace/full_graph.pb",
                           "한벌 데이터 학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("full_labels",
                           "./workspace/full_labels.txt",
                           "한벌 데이터 학습할 레이블 데이터 파일")
FLAGS = tf.app.flags.FLAGS

labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.upper_labels)]
with tf.gfile.FastGFile(FLAGS.upper_graph, 'rb') as fp:
        upper_graph_def = tf.GraphDef()
        upper_graph_def.ParseFromString(fp.read())
        tf.import_graph_def(upper_graph_def, name='')
lower_labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.lower_labels)]


'''
        tf.import_graph_def(graph_def, name='')

lower_labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.lower_labels)]
full_labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.full_labels)]
labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.output_labels)]

with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')

with tf.gfile.FastGFile(FLAGS.lower_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')

with tf.gfile.FastGFile(FLAGS.full_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')
'''
sess=tf.Session()
logits = sess.graph.get_tensor_by_name('final_result:0')
def predict_img(img):
    
	tf.reset_default_graph()
    	#with tf.Session() as sess:
        #logits = sess.graph.get_tensor_by_name('final_result:0')
    	image = tf.gfile.FastGFile(img, 'rb').read()

	tmp=time.time()
    	prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})
	res_index= np.argmax(prediction[0])
	return labels[res_index]
