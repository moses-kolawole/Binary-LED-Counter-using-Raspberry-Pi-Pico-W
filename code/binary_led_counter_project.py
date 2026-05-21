from machine import Pin
from time import sleep

firstled = Pin(6, Pin.OUT)
secondled = Pin(7, Pin.OUT)
thirdled = Pin(8, Pin.OUT)
fourthled = Pin(9, Pin.OUT)

while True:
    #0
    firstled.value(0)
    secondled.value(0)
    thirdled.value(0)
    fourthled.value(0)
    sleep(1)
    
    # 1
    firstled.value(0)
    secondled.value(0)
    thirdled.value(0)
    fourthled.value(1)
    sleep(1)
    
    # 2
    firstled.value(0)
    secondled.value(0)
    thirdled.value(1)
    fourthled.value(0)
    sleep(1)
    
    # 3
    firstled.value(0)
    secondled.value(0)
    thirdled.value(1)
    fourthled.value(1)
    sleep(1)
    
    # 4
    firstled.value(0)
    secondled.value(1)
    thirdled.value(0)
    fourthled.value(0)
    sleep(1)
    
    # 5
    firstled.value(0)
    secondled.value(1)
    thirdled.value(0)
    fourthled.value(1)
    sleep(1)
    
    # 6
    firstled.value(0)
    secondled.value(1)
    thirdled.value(1)
    fourthled.value(0)
    sleep(1)
    
    # 7
    firstled.value(0)
    secondled.value(1)
    thirdled.value(1)
    fourthled.value(1)
    sleep(1)
    
    # 8
    firstled.value(1)
    secondled.value(0)
    thirdled.value(0)
    fourthled.value(0)
    sleep(1)
    
    # 9
    firstled.value(1)
    secondled.value(0)
    thirdled.value(0)
    fourthled.value(1)
    sleep(1)
    
    # 10
    firstled.value(1)
    secondled.value(0)
    thirdled.value(1)
    fourthled.value(0)
    sleep(1)
    
    # 11
    firstled.value(1)
    secondled.value(0)
    thirdled.value(1)
    fourthled.value(1)
    sleep(1)
    
    # 12
    firstled.value(1)
    secondled.value(1)
    thirdled.value(0)
    fourthled.value(0)
    sleep(1)
    
    # 13
    firstled.value(1)
    secondled.value(1)
    thirdled.value(0)
    fourthled.value(1)
    sleep(1)
    
    # 14
    firstled.value(1)
    secondled.value(1)
    thirdled.value(1)
    fourthled.value(0)
    sleep(1)
    
    # 15
    firstled.value(1)
    secondled.value(1)
    thirdled.value(1)
    fourthled.value(1)
    sleep(1)
    
    
