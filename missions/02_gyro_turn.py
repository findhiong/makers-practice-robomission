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

def gyro_turn(heading):
    """Spin on the spot until the gyro reads heading (degrees)."""
    while abs(heading - gyro.angle()) > 1:
        error = heading - gyro.angle()
        rate = min(120, max(25, abs(error) * 3))   # fast when far away, slow when close
        robot.drive(0, rate if error > 0 else -rate)
        wait(10)
    robot.stop()

# MISSION 2: turn exactly 90 degrees
# Goal: find out which way the gyro counts, then make an accurate quarter turn.

clean_start()
robot.turn(90)                # the simple way: uses the wheels, not the gyro
wait(500)
print("After robot.turn(90) the gyro says:", gyro.angle())

# Question: was the number +90 or -90? Write down which direction is positive.
# Now the gyro way. Remove the # from the next two lines and run again:
# gyro_turn(180)
# print("After gyro_turn(180) the gyro says:", gyro.angle())

# Try this: turn to 90, then 180, then 270, then back to 0. Do you end up where you started?
