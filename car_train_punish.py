
import movement
import camera
import os

import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image


print("Wait please")
p = 3
tf = 1
camera.init()
movement.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")
correct = 'w'
while correct != 'q':
    os.chdir('/home/pi/Documents/Self-driving-car')
    camera.take_picture_test()
    image = Image.open('test.jpg')
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    print(p)
    p = np.argmax(p, axis = 1)
    p=p[0]

    print(p)

    correct = input('Enter correct prediction')  # previously raw_input()

    if correct == 'w':
        print('www')
        os.chdir('/home/pi/Documents/Self-driving-car/images/w')
        camera.take_picture()
        movement.forward(tf)

    elif correct == 'd':
        os.chdir('/home/pi/Documents/Self-driving-car/images/d')
        camera.take_picture()
        movement.right(tf)

    elif correct == 'a':
        os.chdir('/home/pi/Documents/Self-driving-car/images/a')
        camera.take_picture()
        movement.left(tf)

    elif correct == 'q':
        camera.end()

