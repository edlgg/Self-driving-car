
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
        try:
            camera.take_picture()
        except Exception:
            camera.close()
            camera.init()
        movement.forward(tf)
    elif key_press == 'd':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/d')
        try:
            camera.take_picture()
        except Exception:
            camera.close()
            camera.init()
        movement.right(tf)
    elif key_press == 'a':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/a')
        try:
            camera.take_picture()
        except Exception:
            camera.close()
            camera.init()
        movement.left(tf)
    elif key_press == 't':
        os.chdir('/home/pi/Documents/Self-driving-car-all/images/test')
        try:
            camera.take_picture()
        except Exception:
            camera.close()
            camera.init()
    elif key_press == 'p':
        p = 1
        camera.end()
