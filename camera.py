import time
import picamera


def init():
    global camera
    camera = picamera.PiCamera()
    camera.resolution = (128, 128)
    camera.start_preview()
    time.sleep(3)
    camera.vflip = True
    camera.hflip = True
    camera.brightness = 60


def end():
    camera.stop_preview()
    camera.close()


def take_picture():
    current_date = (time.strftime("%d-%m-%Y"))
    current_time = (time.strftime("%H:%M:%S"))
    image_name = current_date + "_" + current_time + ".jpg"
    camera.capture(image_name)


def take_picture_test():
    image_name = "test.jpg"
    try:
        camera.capture(image_name)
    except Exception:
        print("Ran into camera error")
        camera.close()
        camera.init()
