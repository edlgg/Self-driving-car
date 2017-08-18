print("Wait please")
import movement
import camera
import os

p = 0
tf = 1.6
camera.init()
print("Camera initialized, go ahead!")
while p == 0:
	key_press = raw_input('')

	if key_press == 'w':
		os.chdir('/home/pi/Documents/self-driving-car/images/w')
		camera.take_picture()
		movement.forward(tf)
        elif key_press == 'd':
		os.chdir('/home/pi/Documents/self-driving-car/images/d')
		camera.take_picture()
                movement.right(tf)
        elif key_press == 'a':
		os.chdir('/home/pi/Documents/self-driving-car/images/a')
		camera.take_picture()
                movement.left(tf)
	elif key_press == 't':
		os.chdir('/home/pi/Documents/self-driving-car/images/test')
		camera.take_picture()
                movement.left(tf)
	elif key_press == 'p':
		p = 1
		camera.end()
