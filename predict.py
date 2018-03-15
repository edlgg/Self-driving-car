
import movement
import camera
import os

import h5py
import numpy as np
from keras.models import load_model
from keras.models import Model
from PIL import Image


print("Wait please")
i = 1
camera.init()
model = load_model('my_model.h5')
print("Camera initialized, go ahead!")

while i == 1:
    camera.take_picture_test()
    image = Image.open('test.jpg')
    image = np.array(image)
    p = model.predict(np.expand_dims(image, axis=0))
    p = np.argmax(p, axis = 1)
    p=p[0]
    print(p)

    i = input('continue? 1 for yes')  # previously raw_input()

camera.end()

