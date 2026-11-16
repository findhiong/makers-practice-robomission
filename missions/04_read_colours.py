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

# MISSION 4: read the colours under the robot
# Goal: drive slowly along the music staves and print every colour the floor sensor sees.

clean_start()
gyro_turn(-90)
robot.reset()
last = None
while robot.distance() < 1200:
    error = -90 - gyro.angle()
    robot.drive(100, error * 3)
    seen = floor_left.color()
    if seen != last:
        print(round(robot.distance() / 10), "cm:", seen)
        last = seen
    wait(10)
robot.stop()

# Try this:
# - Which colours did it find, and at what distances? Compare with the field map.
# - Print floor_left.reflection() instead. Black gives a low number, white a high one.
# - Make the robot beep and stop as soon as it sees RED (use: if seen == Color.RED: ...)
