import RPi.GPIO as LED # Import GPIO library
from time import sleep 

LED.setwarnings(False) # Ignore warning for now
LED.setmode(LED.BOARD) # Use physical pin numbering
LED.setup(8, LED.OUT, initial=LED.LOW) # pin 8

while True: # loop
 LED.output(8, LED.HIGH) 
 sleep(1) 
 LED.output(8, LED.LOW) 
 sleep(2) 