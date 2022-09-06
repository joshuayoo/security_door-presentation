import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import pygame
reader = SimpleMFRC522()

def rasist():
        df = pd.read_csv('/home/pi/project/data/much.csv')

try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
finally:
        GPIO.cleanup()