
import movement
import camera
import os

print("Wait please")
p = 0
tf = 1.6
camera.init()
print("Camera initialized, go ahead!")
while p == 0:
    key_press = input('')  # previously raw_input()

    if key_press == 'w':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/w')
        camera.take_picture()

        movement.forward(tf)
    elif key_press == 'd':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/d')
        camera.take_picture()

        movement.right(tf)
    elif key_press == 'a':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/a')
        camera.take_picture()

        movement.left(tf)
    elif key_press == 'q':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/q')
        camera.take_picture()

    elif key_press == 'p':
        p = 1
        camera.end()
