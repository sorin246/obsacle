import telepot
import RPi.GPIO as G
from telepot.loop import MessageLoop
import time,datetime


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

G.setup(m11,G.OUT)
G.setup(m12,G.OUT)
G.setup(m21,G.OUT)
G.setup(m22,G.OUT)

G.output(led, 1)

time.sleep(1)

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
    G.output(m11, 1)
    G.output(m12, 0)
    G.output(m21, 0)
    G.output(m22, 0)
    
telegram_bot = telepot.Bot('789176298:AAEMCGsHc9d1ibfFh2NHi4yaKwCcHxS_4KI')
print (telegram_bot.getMe())

def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].lower()

    print 'Recieved %s' % command

    if command == "/forward":
        forward()
    elif command == "/back":
        back()
    elif command == "/left":
        left()
    elif command == "/right":
        right()
    elif command == "/stop":
        stop()
    else:
        telegram_bot.sendMessage(chat_id, str( "invalid syntax. valid commands are /forward, /back, /left, /right, /stop."))
MessageLoop(telegram_bot, action).run_as_thread()
print 'Up and Running....'

while 1:
    time.sleep(10)

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
    if(count%3 == 1) & (flag == 0):
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
