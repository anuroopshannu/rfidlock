import RPi.GPIO as GPIO 
from time import sleep
from mfrc522 import SimpleMFRC522
from pushbullet import Pushbullet

pb = Pushbullet("o.vwYuQ41WVSNuAdANnXt3YqMCi9sZFPFM")
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)
reader = SimpleMFRC522()
s="                                            "

while 1:
    try:
        id, text = reader.read()
        if(text=="abcd"):
            GPIO.output(8, GPIO.LOW)
            push = pb.push_note("your door has been unlocked","")
            sleep(5)
            GPIO.output(8, GPIO.HIGH)
        else:
            push = pb.push_note("someone is trying to unlock your door", "")
    except:
        print('unable to read rfid')