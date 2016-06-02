#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import Adafruit_LSM303


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)
lsm303 = Adafruit_LSM303.LSM303()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

L_Motor = mh.getMotor(2)
R_Motor = mh.getMotor(1)

def go_forward(timeValue = 1, speed = 100):
	print"go_forward"
	L_Motor.run(Adafruit_MotorHAT.FORWARD)
	R_Motor.run(Adafruit_MotorHAT.FORWARD)
	L_Motor.setSpeed(speed)
	R_Motor.setSpeed(speed)
	print "\tSpeed up..."
	for i in range(speed):
		L_Motor.setSpeed(i)
		R_Motor.setSpeed(i)
		time.sleep(0.02)
	time.sleep(timeValue)
	print "\tSlow down..."
	for i in reversed(range(speed)):
		L_Motor.setSpeed(i)
		R_Motor.setSpeed(i)
		time.sleep(0.02)

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

def slow_to_a_stop(timeValue = 1, speed = 100):
	L_Motor.run(Adafruit_MotorHAT.FORWARD)
	R_Motor.run(Adafruit_MotorHAT.FORWARD)
	for i in reversed(range(255)):
		 	L_Motor.setSpeed(i)
			R_Motor.setSpeed(i)
			time.sleep(0.01)

def stop(timeValue = 1, speed = 100):
	L_Motor.run(Adafruit_MotorHAT.FORWARD)
	R_Motor.run(Adafruit_MotorHAT.FORWARD)
	L_Motor.setSpeed(0)
	R_Motor.setSpeed(0)

# def command(argument):
# 	decision = {
# 		"tl": turn_left(1),
# 		"tr": turn_right(1),
# 		"rl": rotate_left(1),
# 		"rr": rotate_right(1),
# 		"f":  go_forward(1),
#
# 	}
# 	function = decision.get(argument, lambda: "nothing")
# 	return function()

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

# cmd = ""
# print "type q to quit"
# while (cmd!="q"):
# 	cmd = raw_input("Enter command: ")
# 	if cmd == "f":
# 		go_forward(1,240)
# 	elif cmd == "rl":
# 		rotate_left(1,240)
# 	elif cmd == "rr":
# 		rotate_right(1,240)
# 	elif cmd == "tr":
# 		turn_right(1,150)
# 	elif cmd == "tl":
# 		turn_left(1,150)
# 	elif cmd == "s":
# 		slow_to_a_stop()
# 	elif cmd == "ss":
# 		stop()
	# command(cmd)


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
#		 time.sleep(0.01)
#
# 	time.sleep(5)
# 	print "Backward! "
# 	L_Motor.run(Adafruit_MotorHAT.BACKWARD)
# 	R_Motor.run(Adafruit_MotorHAT.BACKWARD)
#
# 	print "\tSpeed up..."
# 	for i in range(255):
#	 	L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "\tSlow down..."
# 	for i in reversed(range(255)):
#	 	L_Motor.setSpeed(i)
# 		R_Motor.setSpeed(i)
# 		time.sleep(0.01)
#
# 	print "Release"
# 	L_Motor.run(Adafruit_MotorHAT.RELEASE)
#	 R_Motor.run(Adafruit_MotorHAT.RELEASE)
# 	time.sleep(1.0)

print('Printing accelerometer & magnetometer X, Y, Z axis values.')
# Read the X, Y, Z axis acceleration values and print them.
accel, mag = lsm303.read()
# Grab the X, Y, Z components from the reading and print them out.
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag
print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
# Wait half a second and repeat.
time.sleep(0.5)

heading = (math.atan2(mag_y,mag_x) * 180) / math.pi;
