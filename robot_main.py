import os.path
import time
import RPi.GPIO as GPIO
import time
import os
t=0


def init():
    TRIG = 16
    ECHO =18
    TRIG2= 29
    ECHO2=31
    TRIG3=37
    ECHO3=22   
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    GPIO.setup(TRIG2, GPIO.OUT)
    GPIO.setup(ECHO2, GPIO.IN)
    GPIO.output(TRIG2, False)
    GPIO.setup(TRIG3, GPIO.OUT)
    GPIO.setup(ECHO3, GPIO.IN)
    GPIO.output(TRIG3, False)

def forward(tf):
    init()
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()

def reverse(tf):
    init()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(tf)
    GPIO.cleanup()

def left (tf):
    init()
    GPIO.output(7, False)
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    time.sleep(tf)
    GPIO.cleanup()

def right(tf):
    init()
    GPIO.output(7, True)
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()

def none(tf):
    init()
    GPIO.output(7, False)
    GPIO.output(11, False)
    GPIO.output(13, False)
    GPIO.output(15, False)
    time.sleep(tf)
    GPIO.cleanup()



print "Calibrating"
time.sleep(1)


def measure():
    global t
    while True:
        print t
        t+=1
        if t==50:
            print 'End'
            GPIO.cleanup()
            os._exit(0)           
        init()
        
        GPIO.output(TRIG,True)
        time.sleep(0.00002)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
                pulse_start=time.time()
        while GPIO.input(ECHO)==1:
                pulse_end=time.time()
                             
        pulse_duration=pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance= round(distance+1.15,2)
        
          if distance<=20 and distance>8.5  :
                 print "Distance ",distance,"cm"
                 with open('text1.txt','a') as f:
                     print >> f, 'turtle.forward(7.5)'
                 forward(0.5)
                 measure2()

          if distance>20  :
                 print "Distance ",distance,"cm"
                 with open('text1.txt', 'a') as f:
                     print >> f, 'turtle.forward(15)'
                 forward(1)
                 measure2()
       
          if distance<=8.5 :
                 measure3()                 

        time.sleep(0.0002)


def measure2():
    while True:
        init()     
        
        GPIO.output(TRIG2, True)
        time.sleep(0.00002)
        GPIO.output(TRIG2, False)
        
        while GPIO.input(ECHO2)==0:                
                pulse_start2=time.time()
        while GPIO.input(ECHO2)==1:
                pulse_end2=time.time()
         
        pulse_duration2=pulse_end2-pulse_start2
        distance2=pulse_duration2*17150
        distance2=round(distance2+1.15,2)
       
        if distance2 >=40:
                print "Distance right",distance2,"cm"
                forward(0.2) 
                right(1)
                forward(0.2)
                with open('text1.txt','a') as f:
                    print >> f,'turtle.right(90)'
                break
            
        if distance2 <40:
                print "Distance right",distance2,"cm"
                none(0.1)
                break
 

def measure3():
    while True:
        init()
        
        GPIO.output(TRIG3,True)
        time.sleep(0.00002)
        GPIO.output(TRIG3,False)
        
        while GPIO.input(ECHO3)==0:
                pulse_start3=time.time()
        while GPIO.input(ECHO3)==1:
                pulse_end3=time.time()

        pulse_duration3=pulse_end3-pulse_start3
        distance3=pulse_duration3*17150
        distance3=round(distanc3+1.15,2)

        if distance3>=40:
                print "Distance Forward Sensor 2, Object Present",distance2,"cm"
                s="fswebcam /home/pi/robotics/images/image0.jpg" 
                os.system(s)
                s2="sudo python3 /home/pi/robotics/ImageClassify.py --modeldir=Image_model --imagedir=images"
                os.system(s2)
                left(1)
                forward(0.2)
                right(1)
                forward(0.2)
                right(1)
                forward(0.2)
                left(1)
                break
                
        if distance3 <40:
               print "Distance Forward Sensor 2,No object, WALL",distance2,"cm"
               reverse(0.15)
               left(1)
               forward(0.2)
               with open('text1.txt','a') as f:
                    print >> f,'turtle.left(90)'
               break     
               
with  open('text1.txt','w') as f:
    print " "
measure()
