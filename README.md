# 🤖 Robot Rockstars: learn Python with a robot

Practise for RoboMission on an iPad or computer. No robot needed, no sign-up, nothing to install.

## 👉 Start here

### 1. Open the practice field

**[▶️ Tap here to open the Robot Rockstars field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)**

This opens GearsBot with the field and the robot already loaded. It takes a few seconds.

> 💡 **Tip:** Save this link so you can find it again. On an iPad, tap the **Share** button in Safari, then **Add to Home Screen**.

### 2. Switch on Python (do this every time)

At the top of GearsBot there's a row of words: **File, Python, Robot, Worlds, Help**.

1. Tap **Python** in that row.
2. Tap **Pybricks Mode**.

### 3. Name your work

At the very top there's a box that says **Project Name**. Type the mission you're doing, for example `mission1`.

### 4. Pick your mission

**[📋 Open the mission cards](missions/README.md)** and start with Mission 1.

### 5. Save before you finish

Tap **File**, then **Save Python to your computer**, then **Download**.

---

## 🧭 Finding your way around GearsBot

| What you want | Where it is |
|---|---|
| Build with blocks | The **Blocks** tab (top left) |
| See and change the Python | The **Python** tab (top left) |
| Watch the robot | The **Simulator** tab (top left) |
| Start the robot | ▶️ in the **Simulator** |
| Put the robot back at the start | The **reset** button (curly arrow) in the **Simulator** |
| See messages from `print` | The message box at the bottom of the **Simulator** (tap the little arrow) |
| Open a saved program | **File > Load Python from your computer** |

## 🗺️ The field map

The map shows where everything is, in centimetres. Keep it open while you plan.

![Field map](images/field-map.jpg)

## ⭐ Ready for a challenge?

**[🔀 Open the field with shuffled notes](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-random-notes.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)**

Four of the notes swap places every time, so your robot has to check colours to find the right one.

---

# For grown-ups

## Sharing with other kids

Just share the link to this page. Everything works from a web browser: the field, robot and missions all load from here, and children don't need a GitHub or GearsBot account.

Work is kept in the browser between sessions on the same device, but only the latest program. Saving with **File > Save Python to your computer** keeps each mission. Clearing Safari's history or using a private tab wipes unsaved work.

## If the "Tap here" link doesn't work

You can load everything by hand in GearsBot (**https://gears.aposteriori.com.sg**):

1. On this page, open `worlds/robot-rockstars-malaysia.json` and tap the **download** button (the arrow pointing down, top right of the file).
2. In GearsBot, tap **Worlds > Load from file** and choose the downloaded file.
3. Tap **Robot > Select Robot**, choose **Cage Bot**, then **Ok**.
4. Tap **Python > Pybricks Mode**.

## What's in here

| Folder | What it is |
|---|---|
| `missions/` | Eight mission cards, from "drive straight" to a full 2-minute run, plus a scoring sheet. Missions 1 to 4 use Blocks, 5 to 8 use Python. |
| `missions/code/` | Starter Python for missions 5 to 8. |
| `worlds/` | The field: Malaysian Rookie Primary layout (fixed notes) and a shuffled-notes version. Both have a 2-minute timer. |
| `robots/` | The Cage Bot robot. |
| `images/` | The mat and the labelled field map. |

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
