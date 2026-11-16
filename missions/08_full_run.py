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

# MISSION 8: the full 2-minute run
# Load worlds/robot-rockstars-random-notes.json to practise with shuffled notes.
# The timer stops the robot after 120 seconds, just like competition day.
#
# Score yourselves with the sheet in missions/MISSIONS.md.
# Tip: a mission that works 9 times out of 10 beats a faster one that works half the time.

clean_start()

def cables():
    pass   # 2 x 15 points

def microphone():
    pass   # 20 points

def instruments():
    pass   # 3 x 15 points

def notes():
    pass   # 6 x 20 points. With random notes, use front_colour to find out which is which!

cables()
microphone()
instruments()
notes()
