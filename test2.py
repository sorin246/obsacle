import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

m11 = 16
m12 = 12
m21 = 21
m22 = 20

G.setup(m11,G.OUT)
G.setup(m12,G.OUT)
G.setup(m21,G.OUT)
G.setup(m22,G.OUT)

def stop():
    print"stop"
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)

def forward():
    print"forward"
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)

def back():
    print"back"
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 1)

def left():
    print"left"
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)

def right():
    print"right"
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)
    
forward()
time.sleep(5)
back()
time.sleep(5)
left()
time.sleep(5)
right()
time.sleep(5)
stop()
