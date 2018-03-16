
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
    imageName = camera.take_picture_return()
    image = Image.open(imageName)
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    print(p)
    p = np.argmax(p, axis = 1)
    p=p[0]
    print(p)

    correct = input('Enter correct prediction')  # previously raw_input()

    if correct == 'w':
        camera.take_picture()
        os.rename(str("/home/pi/Documents/Self-driving-car/"+imageName), str("home/pi/Documents/Self-driving-car/images/test/"+imageName))
        movement.forward(tf)

    elif correct == 'd':
        camera.take_picture()
        os.rename(str("~/Documents/Self-driving-car/"+imageName), str("~/Documents/Self-driving-car/images/test/"+imageName))
        movement.right(tf)

    elif correct == 'a':
        camera.take_picture()
        os.rename(str("/home/pi/Documents/Self-driving-car/"+imageName), str("home/pi/Documents/Self-driving-car/images/test/"+imageName))
        movement.left(tf)

    elif correct == 'q':
        camera.end()
        movement.end()
    

