import time
import picamera
import RPi.GPIO as GPIO  # new

GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)  # new

with picamera.PiCamera() as camera:
    camera.start_preview()
    GPIO.wait_for_edge(17, GPIO.FALLING)  # new
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()