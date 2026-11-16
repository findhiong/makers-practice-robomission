#!/usr/bin/env pybricks-micropython
# Robot: GearsBot "Cage Bot"   World: worlds/robot-rockstars-malaysia.json
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor, UltrasonicSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
cage = Motor(Port.C)                 # the cage that traps game objects
floor_left = ColorSensor(Port.S1)    # looks down at the mat
floor_right = ColorSensor(Port.S2)   # looks down at the mat
front_colour = ColorSensor(Port.S3)  # looks forwards, at objects
gyro = GyroSensor(Port.S5)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
# Distances are in millimetres (mm). The field map is in centimetres (cm): 10 mm = 1 cm.

def clean_start():
    """Hands off, let the robot settle, then set the gyro to zero."""
    wait(1000)
    gyro.reset_angle(0)

def gyro_straight(distance_mm, heading=0, speed=200):
    """Drive in a straight line, steering back towards heading using the gyro."""
    robot.reset()
    direction = 1 if distance_mm > 0 else -1
    while abs(robot.distance()) < abs(distance_mm):
        error = heading - gyro.angle()
        robot.drive(speed * direction, error * 3)
        wait(10)
    robot.stop()

def gyro_turn(heading):
    """Spin on the spot until the gyro reads heading (degrees)."""
    while abs(heading - gyro.angle()) > 1:
        error = heading - gyro.angle()
        rate = min(120, max(25, abs(error) * 3))   # fast when far away, slow when close
        robot.drive(0, rate if error > 0 else -rate)
        wait(10)
    robot.stop()

# MISSION 7: deliver one note
# The RED note always starts in slot 3 at the top (x = 31 cm, y = 48 cm).
# Its target R is at about x = 20 cm, y = -4.5 cm.
# Goal: bring the red note to R, upright and completely inside the grey border (20 points).

def cage_open():
    cage.run_target(200, 0)

def cage_close():
    cage.run_target(200, 90)    # Is 90 right? Try different angles!

clean_start()
cage_open()
# Plan it on paper first:
# 1. Where must the robot drive to be in front of the red note?
# 2. Which way must it face?
# 3. How far to the target, and which heading?
# Then write it here using gyro_turn() and gyro_straight().

# Check with the front sensor that you really have the right note:
# print(front_colour.color())
