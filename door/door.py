from distutils.log import error
import socket
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pyttsx3
import hashlib
from time import sleep
from sys import exit
import threading
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import time
import pygame

lazer = 7
servoPIN = 15
GPIO.setmode(GPIO.BCM)

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)

GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(lazer, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(3)
sleep(0.5)
count = 0

def warn_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("warn.wav")
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy() == True:
        continue

def open():
    global count, chan, p
    GPIO.output(lazer, True)
    sleep(0.3)
    p.ChangeDutyCycle(6.5)
    found = 0
    timer = time()
    while(1):
        if chan.voltage > 1 or time()>timer+10:
            found =1
            break
    if found == 1:
        sleep(1)
        GPIO.output(lazer, False)
        p.ChangeDutyCycle(3)
        ...

def speak(say):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(say)
    engine.runAndWait()
    
    
    
def warn(say): #5회 이상 틀렸을떄.
    global chan
    GPIO.output(lazer, True)
    speak(say)
    while(1):
        if chan.voltage > 1:
            warn = threading.Thread(target=warn_sound)
            warn.start()
            break
    while 1:
        ...
            


# rfid
def check():
    reader = SimpleMFRC522()
    for i in range(3):
        try:
            text = '0';
            id, text = reader.read()
            if text == None:
                return 0, error
            id_s = hashlib.sha256(str(id).encode()).hexdigest()
            try:
                text_s = text
                if text_s == '17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1':
                    return 0, error
            except:
                return 0, error
            del id
            del text
            break
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit()
        except:
            pass
        if i ==2:
            return 0, error
    return id_s, text_s




def connect(id_s, text_s):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('61.74.154.145', 10000))
    send = id_s+"_"+text_s
    try:
        message = send.encode()
        sock.send(message)
        data = sock.recv(1024)
        a = data.decode()
        sock.close()
        return a
    except:
        return error

def alert(n, num):
    if n==0 and num ==5:
        warn("security mode")
    elif n==0:
        print('nope')
        speak(str(num)+' fail.')
    elif n==1:
        speak(str(num)+' wellcome')
        print("come in")
        open()

def start_r():
    GPIO.output(lazer, False)
    n=0
    while 1:
        sleep(2)
        print("cheking")
        id_s, text_s = check()
        if text_s == error:
            print('error')
        else :
            abc = connect(id_s, text_s)
            if abc ==error:
                print("error1")
            elif abc == 'deny':
                n = n+1
                alert(0, n)
            elif 'success' in abc:
                abc = abc.strip("success")
                n=0
                alert(1, abc)

start_r()