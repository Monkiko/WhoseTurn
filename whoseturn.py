#!/usr/bin/env python
#
#
#
#
import subprocess
from random import shuffle
import time
#
#
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
#
#
kids = int(input('How many kids are here? '))
#
#
Chosen=[]
x=1
while x <= kids:
    Chosen.append(input('Provide the name of one of the children: '))
    x+=1
#
#
print()
shuffle(Chosen)
print(*Chosen, sep = '\n')
print()
print("Let's start a timer for when we change it up.")
t = input("Enter the time in seconds: ")
countdown(int(t))