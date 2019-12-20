import os
import threading
import object_detection_yolo as yolo
import time
import RPi.GPIO as GPIO

class YoLo(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        th_yolo = threading.Thread(target = yolo.ObjectDetection_YOLO, args=('r'))
        th_yolo.start()
            
                
th = YoLo()
th.start()

def Motor():
    pin = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    p = GPIO.PWM(pin, 50)
    p.start(0)
    p.ChangeDutyCycle(3)
    while True:
        search = yolo.getSearchObj()
        if (search == 'take-out-cup'):
           print(search)
           p.ChangeDutyCycle(12)
           time.sleep(10)
           p.ChangeDutyCycle(3)
           yolo.setSearchObj()
        
th_Motor = threading.Thread(target = Motor, args=())
th_Motor.start()