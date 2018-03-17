# -*- coding: utf-8 -*- 
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
tf.app.flags.DEFINE_boolean("show_image",
                            True,
                            "이미지 추론 후 이미지를 보여줍니다.")
'''
tf.app.flags.DEFINE_string("lower_graph",
                           "./workspace/flowers_graph.pb",
                           "학습된 신경망이 저장된 위치")
tf.app.flags.DEFINE_string("lower_labels",
                           "./workspace/flowers_labels.txt",
                           "학습할 레이블 데이터 파일")
'''
FLAGS = tf.app.flags.FLAGS

labels = [line.rstrip() for line in tf.gfile.GFile(FLAGS.output_labels)]

with tf.gfile.FastGFile(FLAGS.output_graph, 'rb') as fp:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(fp.read())
        tf.import_graph_def(graph_def, name='')
def predict_img(img):

    with tf.Session() as sess:
        logits = sess.graph.get_tensor_by_name('final_result:0')
        image = tf.gfile.FastGFile(img, 'rb').read()
        prediction = sess.run(logits, {'DecodeJpeg/contents:0': image})


    #print('=== 예측 결과 ===')
    res_max=0.0
    res_index=0
    res_name=''
    for i in range(len(labels)):
        name = labels[i]
        score = prediction[0][i]
        if res_max<score*100:
		print 'update'
                res_max=score*100
                res_index=i
	print i,name,score,res_max,res_index
    #res_str= "inception res: "+str(res_name)+'\n'
    #print labels[res_index],res_max
    sess.close()
    return labels[res_index]


