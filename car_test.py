
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
tf = 2
camera.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")

while p != 3:
    camera.take_picture_test()
    image = Image.open('test.jpg')
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    p = np.argmax(p, axis = 1)
    p=p[0]
    print(p)

    if p == 0:
        movement.left(tf)

    elif p == 1:
        movement.forward(tf)

    elif p == 2:
        movement.left(tf)

    elif p == 3:
        camera.end()

