import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

TRIG = 17
ECHO = 27
led = 22

m11 = 16
m12 = 12
m21 = 21
m22 = 20

G.setup(TRIG,G.OUT)
G.setup(ECHO,G.OUT)
G.setup(led,G.OUT)

G.setup(m11,G.OUT)
G.setup(m12,G.OUT)
G.setup(m21,G.OUT)
G.setup(m22,G.OUT)

G.output(led, 1)

time.sleep(5)

def stop():
    print"stop"
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)

def forward():
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)

def back():
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 1)

def left():
    G.output(m11, 0)
    G.output(m12, 0)
    G.output(m21, 1)
    G.output(m22, 0)

def right():
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 0)
stop()
