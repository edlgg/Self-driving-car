
import movement
import camera
import os

import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image


print("Wait please")
p = 0
tf = 1
camera.init()
movement.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")
correct = 'w'

while p != 3:
    os.chdir('/home/pi/Documents/Self-driving-car')
    print(1)
    camera.take_picture_test()
    print(2)
    image = Image.open('test.jpg')
    print(3)
    image = np.array(image)
    print(4)
    p = model.predict(np.expand_dims(image, axis=0))
    print('****p')
    print(p)
    p = np.argmax(p, axis = 1)
    p=p[0]

    if p == 0:
        print("left")

    elif p == 1:
        print("forward")

    elif p == 2:
        print("right")

    elif p == 3:
        print("quit")

    correct = input('What was the correct prediction?  ')

    if correct == 'a':
        os.chdir('/home/pi/Documents/Self-driving-car/images/a')
        camera.take_picture()
        movement.left(tf)
        print("left")

    elif correct == 'w':
        os.chdir('/home/pi/Documents/Self-driving-car/images/w')
        camera.take_picture()
        movement.forward(tf)
        print("forward")

    elif correct == 'd':
        os.chdir('/home/pi/Documents/Self-driving-car/images/d')
        camera.take_picture()
        movement.right(tf)
        print("right")

    elif correct == 'q':
        os.chdir('/home/pi/Documents/Self-driving-car/images/q')
        camera.take_picture()
        movement.end()
        camera.end()

    elif correct == 'y':
        if p == 0:
            movement.left(tf)
            print("left")

        elif p == 1:
            movement.forward(tf)
            print("forward")

        elif p == 2:
            movement.right(tf)
            print("right")

        elif p == 3:
            movement.end()
            camera.end()