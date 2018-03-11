"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import timeit
import sys

import numpy as np
import PIL.Image as Image

import tensorflow as tf

import RPi.GPIO as gpio
import movement
import camera


graph_file="optimized_graph.pb"

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for lin in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
graph = tf.Graph()
with graph.as_default():
    graph_def = tf.GraphDef()

    with tf.gfile.FastGFile(graph_file, 'rb') as f:
        graph_def.ParseFromString(f.read())

    tf.import_graph_def(graph_def, name='')

with tf.Session(graph=graph) as sess:

    p = 0
    tf = 1
    movement.init()
    camera.init()

    while p == 0:
        camera.take_picture_test()

        # Read in the image_data
        image_path="test.jpg"

        image = Image.open(image_path)
        image = np.array(image, dtype=np.float32)

        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = graph.get_tensor_by_name('final_result:0')

        start_time = timeit.default_timer()
        predictions = sess.run(softmax_tensor,
                {'Cast:0': image})
        elapsed = timeit.default_timer() - start_time
        print('Elapsed time: %f\n' % elapsed)

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        prediction = label_lines[0]
        movement.end()
    gpio.cleanup()
    movement.init()
        if prediction == 'w':
            print('w')
            movement2.forward()
        elif prediction == 'd':
            print('d')
            movement2.right()
        elif prediction == 'a':
            print('a')
            movement2.left()
        elif prediction == 'k':
            p = 1
            print("The end")
            camera.end()
            gpio.cleanup()

        if cv2.waitKey(1) == 13: #13 is the Enter Key
            print("The end")
            camera.end()
            gpio.cleanup()
            break

"""
