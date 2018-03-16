
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
i=0
camera.init()
movement.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")
correct = 'w'
while correct != 'q':
    camera.take_picture()
    image = Image.open('test.jpg')
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    print(p)
    p = np.argmax(p, axis = 1)
    p=p[0]
    print(p)

    correct = input("Enter correct prediction")  # previously raw_input()

    if correct == 'w':
        os.rename(str("/test.jpg"), str("/images/test/test"+str(i)+".jpg"))
        movement.forward(tf)

    elif correct == 'd':
        os.rename(str("~/Documents/Self-driving-car/"+imageName), str("~/Documents/Self-driving-car/images/test/"+imageName))
        movement.right(tf)

    elif correct == 'a':
        os.rename(str("/home/pi/Documents/Self-driving-car/"+imageName), str("home/pi/Documents/Self-driving-car/images/test/"+imageName))
        movement.left(tf)

    elif correct == 'q':
        camera.end()
        movement.end()
    
    i = i + 1
    

