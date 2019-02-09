import RPi.GPIO as G
import time

G.setwarnings(False)
G.setmode(G.BCM)

TRIG = 17
ECHO = 27
led = 22

G.setup(TRIG,G.OUT)
G.setup(ECHO,G.IN)
G.setup(led, G.OUT)
G.output(led, False)
time.sleep(1)

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
