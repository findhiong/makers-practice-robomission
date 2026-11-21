# Mission 3: Drive to Yellow 🟨

**Your goal:** Drive from the start and stop on the **yellow box with the grey outline**. It sits on the music staves (the wavy purple lines with the big treble clef, across the middle of the mat).

**Why it matters:** This is your first real route: a turn plus a drive. You'll plan it with the map, like a real team.

---

## Before you start 🏁

1. **[Open the field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)** (press and hold, then **Open in New Tab**).
2. In the **menu row**, tap **Python**, then **Pybricks Mode**. ([Not sure where?](../README.md#3-switch-on-pybricks-do-this-every-time))
3. In the **Project Name** box at the very top, type `mission3`.
4. Open the **[🗺️ Field Map](../images/field-map.jpg)** (press and hold, then **Open in New Tab**). It shows where everything is. ([How to read it](README.md#-the-field-map))

## How to run the robot ▶️

1. Tap the **Simulator** tab.
2. Tap ▶️ to start.
3. To try again, tap the **curly arrow** to put the robot back at the start, then ▶️.

## Step 1: Plan it on the map 🗺️

Open the **[🗺️ Field Map](../images/field-map.jpg)**. Find **START** and **Yellow target**.

- The start is at about **x = 98 cm**.
- The yellow box (with the grey outline) is at about **x = -12 cm**.

So the robot needs to travel 98 + 12 = **110 cm** to the **left**.

> 🧮 **Maths time:** One wheel rotation moves the robot about 17.6 cm. How many rotations is 110 cm?
> 110 ÷ 17.6 = ______ rotations

## Step 2: Build it in Blocks 🧱

1. `sleep for 1 seconds`
2. Your **quarter turn to the left** from Mission 2 (use the number of rotations you found).
3. `move steering with direction 0 and speed 30 % for ___ rotations` (your answer from the maths).

Run it.

> 💡 Keep the speed at **30 %**. Faster makes the wheels skid and the robot drifts off course.

## Step 3: Fix it in Blocks 🔧

Did it stop short, go too far, or miss to one side? In the **Blocks** tab, change **one number at a time**: the **rotations** of the turn, or the **rotations** of the drive.

| What I changed | What happened |
|---|---|
| | |
| | |
| | |

## Step 4: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

In the **Python** tab, find your two `move_steering_for_degrees` lines. The first one turns, the second one drives.

> ✏️ **Guess first!** Before you press ▶️, write what you think will happen in the **We think...** column. For example: *"It will go twice as far."* Then press ▶️ and write what really happened.

| In the Python tab, change... | From | To | We think it will... | What happened |
|---|---|---|---|---|
| the **speed** of the drive | `30` | `100` | | |
| the **distance** of the drive | your number | add `0.5` | | |
| the **direction** of the turn | yours | the opposite (`-` in front, or take it away) | | |

---

## ✅ You've finished when...

The robot stops on the yellow box (with the grey outline) 3 times in a row. Then, using **only the Python tab**, change the numbers so it stops on the **black box with the grey outline** instead (find **Black target** on the map).

## 📓 Notebook

- At full speed, was it still accurate? Why might that be?
- Did the robot drift a little to one side on the long drive? We'll fix that in Mission 5.

## 💾 Save your work

1. In the **menu row**, tap **File**.
2. Tap **Save Python to your computer**, then **Download**.
3. Your work is saved as `mission3.zip`. To open it next time: **File > Load Python from your computer**.
