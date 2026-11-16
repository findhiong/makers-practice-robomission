# Mission 1: The Clean Start 🚀

**Your goal:** Make the robot drive forwards 30 cm in a perfectly straight line.

**Why it matters:** At the competition, your robot twitched at the start. This mission is the first step to fixing that.

---

## Before you start 🏁

1. **[Open the field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)** (press and hold, then **Open in New Tab**).
2. In the **menu row**, tap **Python**, then **Pybricks Mode**. ([Not sure where?](../README.md#3-switch-on-pybricks-do-this-every-time))
3. In the **Project Name** box at the very top, type `mission1`.

## How to run the robot ▶️

1. Tap the **Simulator** tab.
2. Tap ▶️ to start.
3. To try again, tap the **curly arrow** to put the robot back at the start, then ▶️.

## Step 1: Build it in Blocks 🧱

Tap the **Blocks** tab. Under the **When Started** block, add these two blocks in order:

1. From **Control**: `sleep for 1 seconds`
   This gives your hands time to get away from the robot.
2. From **Motion**: `move steering with direction 0 and speed 30 % for 1.7 rotations`
   Direction 0 means straight ahead.

Run it (see **How to run the robot** above).

> 🤔 **Why 1.7 rotations?** The wheel is 56 mm across, so one turn of the wheel moves the robot about 17.6 cm. To go 30 cm, the wheel needs to turn about 1.7 times.

## Step 2: Find it in Python 🔍

Tap the **Python** tab. The top part is the robot's set-up. **Don't change it.**

Scroll down until you see:

```
# Here is where your code starts
```

Below that are your two blocks, written in Python. Point to each line and say which block it came from.

## Step 3: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

Your drive line in the **Python** tab looks like this:

```python
move_steering_for_degrees(0, (30 / 100) * 1050, 1.7 * 360)
```

It has three numbers you can change:

| Number | What it means |
|---|---|
| `0` | **Direction.** 0 = straight. Bigger numbers curve more. |
| `30` | **Speed.** 30 = slow and steady. 100 = full speed. |
| `1.7` | **Distance**, in wheel rotations. |

Do one change at a time. **Guess first**, then press ▶️, then change it back.

> ✏️ **Guess first!** Before you press ▶️, write what you think will happen in the **We think...** column. For example: *"It will go twice as far."* Then press ▶️ and write what really happened.

| In the Python tab, change... | From | To | We think it will... | What happened |
|---|---|---|---|---|
| the **distance** | `1.7` | `3.4` | | |
| the **distance** | `1.7` | `-1.7` | | |
| the **speed** | `30` | `100` | | |
| the **direction** | `0` | `50` | | |
| the **wait** line `wait(1 * 1000)` | `1` | `0` | | |

---

## ✅ You've finished when...

Using **only the Python tab** (not the blocks), you can make the robot **wait 2 seconds**, then **drive straight 25 cm**.

> 💡 Hint: 25 cm is about 1.4 wheel rotations.

## 📓 Notebook

- Which way did the robot drive? Find it on the [field map](../images/field-map.jpg). Which object is it driving towards?
- What surprised you?

## 💾 Save your work

1. In the **menu row**, tap **File**.
2. Tap **Save Python to your computer**, then **Download**.
3. Your work is saved as `mission1.zip`. To open it next time: **File > Load Python from your computer**.
