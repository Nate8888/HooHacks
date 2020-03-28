from NeuroPyThree import NeuroPy
import time
import os
import json

data = {}

object1=NeuroPy("COM5")
currentIndex = 0
currentAttentionValue = 1
currentMeditationValue = 1
currentIndex2 = 0


def blink_callback(value):
    print(value)


def attention_callback(value):
    global currentAttentionValue
    global currentIndex
    if value != 0:
        data[str(currentIndex)] = value
        currentIndex += 1
        currentAttentionValue = value
        with open('data.txt', 'w') as outfile:
            outfile.write(str(value))

def meditation_callback(value):
    global currentMeditationValue
    global currentIndex2
    if value != 0:
        data[str(currentIndex2)] = value
        currentIndex2 += 1
        currentMeditationValue = value
        with open('relax.txt', 'w') as outfile:
            outfile.write(str(value))

#set call backs:
object1.setCallBack("attention",attention_callback)
object1.setCallBack("meditation",meditation_callback)

#object1.setCallBack("meditation",meditation_callback)

object1.start()
time.sleep(2)

while True:
    time.sleep(0.2)
