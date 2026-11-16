# RoboMission practice: Robot Rockstars 2026

A practice field for learning Python on a simulated robot before the next RoboMission season. It recreates the 2026 Rookie Primary field ("Robot Rockstars") in [GearsBot](https://gears.aposteriori.com.sg), a free robot simulator that runs in the browser.

![Field map](images/field-map.jpg)

## What's in here

| File | What it is |
|------|------------|
| `worlds/robot-rockstars-malaysia.json` | The field with every object placed as in the Malaysian Rookie Primary rules (notes always blue, white, red, green, black, yellow). Start here. |
| `worlds/robot-rockstars-random-notes.json` | Harder: blue, white, black and yellow notes are shuffled each time, as in the international WRO version. The robot has to check colours. |
| `missions/` | **Start here:** eight mission cards for the kids, from "drive straight" to a full 2-minute run, plus a scoring sheet. Missions 1 to 4 use Blocks, 5 to 8 use Python. |
| `images/field-map.jpg` | The mat with a centimetre grid and every object labelled. Print it or keep it open. |

Both worlds have a 2-minute countdown that stops the robot, like competition day.

## Setting up GearsBot (once)

1. Open **https://gears.aposteriori.com.sg** in Chrome or Edge on a laptop.
2. **Load the world.** Download `worlds/robot-rockstars-malaysia.json` from this page (open the file, then the download button). In GearsBot, open **Worlds > Load from file** and choose it.
3. **Choose the robot.** Open **Robot > Select Robot** and pick **Cage Bot**.
4. **Switch to Python.** Open the **Python** tab, then its menu, and choose **Pybricks Mode**.
5. Open the [missions](missions/README.md) page and start with Mission 1.

Reloading GearsBot resets it, so do steps 2 to 4 again each time. To keep a program, use **File > Save Python to your computer**.

## The robot (Cage Bot)

| Port | Part |
|------|------|
| A | Left wheel |
| B | Right wheel |
| C | Cage motor (traps objects) |
| S1 | Colour sensor, looking down (left) |
| S2 | Colour sensor, looking down (right) |
| S3 | Colour sensor, looking forwards |
| S4 | Distance sensor |
| S5 | Gyro |

Wheels are 56 mm across and 152 mm apart.

## How this differs from the real robot

- **Python dialect.** GearsBot uses the Pybricks EV3 style (`DriveBase`, `GyroSensor`, `Port.S1`). On a SPIKE Prime hub with Pybricks firmware the ideas are the same, but the set-up lines differ (`PrimeHub`, `Port.A` to `Port.F`, `hub.imu` for the gyro). Everything about loops, sensors and gyro steering carries straight across.
- **No "twitch".** The simulator has no gear slack and nobody presses a button, so start-up problems only show up on a real robot.
- **Grabbing is simpler.** Pushing and caging objects behaves roughly like the real thing; picking things up does not.
- **Rules change each season.** The 2027 field will be new. This one is for learning the skills.

## Credits

The world files are adapted from the WRO 2026 Elementary world in [GearsBot](https://github.com/QuirkyCort/gears) by Cort Wee (GPL-3.0), with fixed note positions and a 2-minute timer added. The game mat is © World Robot Olympiad Association, published for teams to print and practise with.
