#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
L_Motor = mh.getMotor(2)
R_Motor = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
L_Motor.setSpeed(255)
L_Motor.run(Adafruit_MotorHAT.FORWARD);

R_Motor.setSpeed(255)
R_Motor.run(Adafruit_MotorHAT.FORWARD);

# turn on motors
L_Motor.run(Adafruit_MotorHAT.RELEASE);
R_Motor.run(Adafruit_MotorHAT.RELEASE);

def go_forward(timeValue = 1, speed = 100):
	print"go_forward"
    L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)
    L_Motor.setSpeed(speed)
    R_Motor.setSpeed(speed)
    time.sleep(timeValue)

def rotate_left(timeValue = 1, speed = 100):
	print"rotate_left"
    L_Motor.run(Adafruit_MotorHAT.BACKWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)
    L_Motor.setSpeed(speed)
    R_Motor.setSpeed(speed)
    time.sleep(timeValue)

def rotate_right(timeValue = 1, speed = 100):
	print"rotate_right"
    L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.BACKWARD)
    L_Motor.setSpeed(speed)
    R_Motor.setSpeed(speed)
    time.sleep(timeValue)

def turn_left(timeValue = 1, speed = 100):
	print"turn_left"
    L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)
    L_Motor.setSpeed(speed/4)
    R_Motor.setSpeed(speed)
    time.sleep(timeValue)

def turn_right(timeValue = 1, speed = 100):
	print"turn_right"
    L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)
    L_Motor.setSpeed(speed)
    R_Motor.setSpeed(speed/4)
    time.sleep(timeValue)

def slow_forward_stop(timeValue = 1, speed = 100):
    L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)
    L_Motor.setSpeed(speed)
    R_Motor.setSpeed(speed)
    time.sleep(timeValue)

def command(argument):
    decision = {
        "tl": turn_left(1),
        "tr": turn_right(1),
        "rl": rotate_left(1),
        "rr": rotate_right(1),
        "f":  go_forward(1),
    }
    function = decision.get(argument, lambda: "nothing")
    return function()

# rotate_left(3)
# rotate_right(3)
# # slow_forward_stop(1)
# turn_right(2)
# turn_left(2)
# go_forward(.1, 75)
# go_forward(.1, 125)
# go_forward(.1, 150)
# go_forward(.1, 175)
# go_forward(.1, 200)
# go_forward(.1, 225)
# go_forward(.1, 250)
# go_forward(.1, 225)
# go_forward(.1, 200)
# go_forward(.1, 175)
# go_forward(.1, 150)
# go_forward(.1, 125)
# go_forward(.1, 75)

cmd = ""
print "type q to quit"
while (cmd!="q"):
	cmd = raw_input("Enter command: ")
	command(cmd)


# while (False):
# 	print "Forward! "
# 	L_Motor.run(Adafruit_MotorHAT.FORWARD)
# 	R_Motor.run(Adafruit_MotorHAT.FORWARD)
#
# 	print "\tSpeed up..."
# 	for i in range(255):
# 		L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "\tSlow down..."
# 	for i in reversed(range(255)):
# 		L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
#         time.sleep(0.01)
#
# 	time.sleep(5)
# 	print "Backward! "
# 	L_Motor.run(Adafruit_MotorHAT.BACKWARD)
# 	R_Motor.run(Adafruit_MotorHAT.BACKWARD)
#
# 	print "\tSpeed up..."
# 	for i in range(255):
#     	L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "\tSlow down..."
# 	for i in reversed(range(255)):
#     	L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "Release"
# 	L_Motor.run(Adafruit_MotorHAT.RELEASE)
#     R_Motor.run(Adafruit_MotorHAT.RELEASE)
# 	time.sleep(1.0)
