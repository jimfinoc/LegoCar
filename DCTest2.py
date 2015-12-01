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
L_Motor = mh.getMotor(1)
R_Motor = mh.getMotor(1)

# set the speed to start, from 0 (off) to 255 (max speed)
L_Motor.setSpeed(255)
L_Motor.run(Adafruit_MotorHAT.FORWARD);

R_Motor.setSpeed(255)
R_Motor.run(Adafruit_MotorHAT.FORWARD);

# turn on motors
L_Motor.run(Adafruit_MotorHAT.RELEASE);
R_Motor.run(Adafruit_MotorHAT.RELEASE);

while (True):
	print "Forward! "
	L_Motor.run(Adafruit_MotorHAT.FORWARD)
    R_Motor.run(Adafruit_MotorHAT.FORWARD)

	print "\tSpeed up..."
	for i in range(255):
		L_Motor.setSpeed(i)
		R_Motor.setSpeed(i)
        time.sleep(0.01)

    time.sleep(0.5)

    print "\tSlow down..."
	for i in reversed(range(255)):
		L_Motor.setSpeed(i)
		R_Motor.setSpeed(i)
        time.sleep(0.01)

	print "Backward! "
	L_Motor.run(Adafruit_MotorHAT.BACKWARD)
	R_Motor.run(Adafruit_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(255):
        L_Motor.setSpeed(i)
        R_Motor.setSpeed(i)
		time.sleep(0.01)

    time.sleep(0.5)
    
	print "\tSlow down..."
	for i in reversed(range(255)):
        L_Motor.setSpeed(i)
		R_Motor.setSpeed(i)
		time.sleep(0.01)

	print "Release"
	L_Motor.run(Adafruit_MotorHAT.RELEASE)
    R_Motor.run(Adafruit_MotorHAT.RELEASE)
	time.sleep(1.0)
