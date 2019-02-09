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
G.setup(ECHO,G.IN)
G.setup(led,G.OUT)
G.setup(led, False)
time.sleep(1)

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
    G.output(m11, 0)
    G.output(m12, 1)
    G.output(m21, 0)
    G.output(m22, 0)
stop()
count = 0
while True:
    i = 0
    avgDistance = 0
    for i in range(5):
        G.output(TRIG, False)
        time.sleep(0.1)
        G.output(TRIG, True)
        time.sleep(0.00001)
        G.output(TRIG, False)
        while G.input(ECHO) == 0:
            #continue
            G.output(led, False)
        pulse_start = time.time()
        while G.input(ECHO) == 1:
            #print "ECHO = 1"
            #continue
            G.output(led, True)
        pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        avgDistance = avgDistance + distance
    avgDistance = avgDistance / 5
    print avgDistance
    flag = 0
    if avgDistance < 15:
        count = count + 1
        stop()
        time.sleep(1)
        back()
        time.sleep(1.5)
        if(count%3 == 1) and (flag == 0):
            right()
            flag = 1
        else:
            left()
            flag = 0
        time.sleep(1.5)
        stop()
        time.sleep(1)
    else:
        forward()
        flag = 0
