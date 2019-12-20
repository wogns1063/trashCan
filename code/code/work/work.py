import RPi.GPIO as GPIO
from time import sleep
import threading
import serial

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)  # GPIO pin Reference method 

GPIO.setup(23, GPIO.IN)  # IR SENSOR setup

openershaft = 19 # opener shaft
GPIO.setup(openershaft , GPIO.OUT)
OpenerShaft = GPIO.PWM(openershaft, 50)
OpenerShaft.start(0)

gripper = 16 # Gripper
GPIO.setup(gripper, GPIO.OUT)
Gripper = GPIO.PWM(gripper, 50)
Gripper.start(0)
Gripper.ChangeDutyCycle(6) # default value

leftshaft = 13 # leftshaft
GPIO.setup(leftshaft, GPIO.OUT)
LeftShaft = GPIO.PWM(leftshaft, 50)
LeftShaft.start(0)
 
rightshaft= 18 # rightshaft
GPIO.setup(rightshaft, GPIO.OUT)
RightShaft = GPIO.PWM(rightshaft, 50)
RightShaft.start(0)
 
ser = serial.Serial('/dev/ttyACM0', 9600)  #serial communication setup

complete = 0

def GripperAction(val): # if irsensor detected, grab and open a cup
    global complete
    Irval = val
    print(Irval)
    
    if Irval == 1:
        th.myExit()
        Gripper.ChangeDutyCycle(6)
        sleep(2)
        Gripper.ChangeDutyCycle(3)  
        sleep(2)  
        arg = "plastic"
        ser.write(arg.encode())
        sleep(1)
        OpenerShaft.ChangeDutyCycle(4)
        sleep(2)
        arg = "opener on"
        ser.write(arg.encode())
        sleep(2)
        OpenerShaft.ChangeDutyCycle(8)
        sleep(2)
        arg = "return"
        ser.write(arg.encode())
        sleep(2)
        arg = "liquid"
        ser.write(arg.encode())
        sleep(5)
        LeftShaft.ChangeDutyCycle(10)
        RightShaft.ChangeDutyCycle(4)
        sleep(5)
        LeftShaft.ChangeDutyCycle(1)
        RightShaft.ChangeDutyCycle(13)
     
        complete = 1
        
class IrSensor(threading.Thread):    #irsensor thread class
    def __init__(self):
        threading.Thread.__init__(self)
        self.__exit = False
    def run(self):
        while True:
            if self.__exit:
                break
            else:
                val = GPIO.input(23) #irsensor value       
                GripperAction(val)
    def myExit(self): # exit thread
        self.__exit = True       

def ThrowCup(val):  # Distinguish the cup after detecting the light sensor.
    global complete
    Cdsval = val;
    th2.myExit()    #light thread exit
    print(Cdsval)   

    if Cdsval > 20:
        print('plastic cup')

        arg = "break"
        ser.write(arg.encode())
        sleep(1)
        Gripper.ChangeDutyCycle(3)
        sleep(1)
        arg = "plastic"
        ser.write(arg.encode())
        sleep(3)
        LeftShaft.ChangeDutyCycle(10)
        RightShaft.ChangeDutyCycle(4)
        sleep(2)
        Gripper.ChangeDutyCycle(6)
        sleep(2)
        LeftShaft.ChangeDutyCycle(1)
        RightShaft.ChangeDutyCycle(13)
        arg = "liquid"
        ser.write(arg.encode())
        
        complete = 0
 
    elif Cdsval < 20:
        print('paper cup')
        
        arg = "break"
        ser.write(arg.encode())
        sleep(1)
        Gripper.ChangeDutyCycle(3)
        sleep(1)
        arg = "paper"
        ser.write(arg.encode())
        sleep(3)
        LeftShaft.ChangeDutyCycle(10)
        RightShaft.ChangeDutyCycle(4)
        sleep(2)
        Gripper.ChangeDutyCycle(6)
        sleep(2)
        LeftShaft.ChangeDutyCycle(1)
        RightShaft.ChangeDutyCycle(13)
        arg = "liquid"
        ser.write(arg.encode())
        
        complete = 0
        
class PhotoResistor(threading.Thread):    #photoresistor thread class
    def __init__(self):
        threading.Thread.__init__(self)
        self.__exit = False
    def run(self):
        while True:
            if self.__exit:
                break           
            else:
                val = ser.readline()
                val2= int(val.decode('utf-8')) #photoresistor sensor value
                ThrowCup(val2) 
    def myExit(self): # exit thread
        self.__exit = True

  
while True:
    th = IrSensor()
    th.start() 
    print('GripperAction start')

    while True:
        if complete == 1 :
            print('ThrowCup start')
            sleep(3)
            arg = "ReadCdsVal"    #read cds val at arduino
            ser.write(arg.encode())
            th2 = PhotoResistor()   
            th2.start()    #PhotoResistor thread start
            sleep(15)
            break

