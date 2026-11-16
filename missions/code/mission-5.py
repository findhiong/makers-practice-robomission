#!/usr/bin/env pybricks-micropython
# ============================================================
#  ROBOT PARTS LIST  (do not change this part)
# ============================================================
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_wheel = Motor(Port.A)
right_wheel = Motor(Port.B)
cage = Motor(Port.C)
floor_sensor = ColorSensor(Port.S1)     # looks down at the mat
floor_sensor_2 = ColorSensor(Port.S2)   # looks down at the mat
front_sensor = ColorSensor(Port.S3)     # looks forwards at objects
gyro = GyroSensor(Port.S5)
robot = DriveBase(left_wheel, right_wheel, wheel_diameter=56, axle_track=152)

# ============================================================
#  OUR OWN BLOCKS  (these are like new blocks we made ourselves)
# ============================================================

# From Mission 2: which way is LEFT for your gyro?
# If turning left made the gyro go MINUS, keep -90. If it went PLUS, change it to 90.
LEFT = -90
RIGHT = -LEFT
UP = 0          # the way the robot faces at the start
DOWN = 180

def stop():
    # Brake hard so the robot doesn't roll on
    left_wheel.brake()
    right_wheel.brake()

def clean_start():
    # Hands off, wait, then set the compass to zero
    wait(1000)
    gyro.reset_angle(0)

def turn_to(heading):
    # Spin until the gyro says the heading we want
    while abs(heading - gyro.angle()) > 1:
        error = heading - gyro.angle()
        spin = min(120, max(25, abs(error) * 3))   # fast when far away, slow when close
        if error > 0:
            robot.drive(0, spin)
        else:
            robot.drive(0, -spin)
        wait(10)
    stop()

STEER_STRENGTH = 3   # how hard the robot steers back on course

def drive_cm(cm, heading, speed=200):
    # Drive in a straight line, using the gyro to steer back on course
    robot.reset()
    direction = 1 if cm > 0 else -1
    while abs(robot.distance()) < abs(cm) * 10:     # robot.distance() is in mm
        error = heading - gyro.angle()
        robot.drive(speed * direction, error * STEER_STRENGTH)
        wait(10)
    stop()


# ============================================================
#  OUR CODE STARTS HERE
# ============================================================

clean_start()
turn_to(LEFT)
drive_cm(110, LEFT)
ev3.speaker.beep()
