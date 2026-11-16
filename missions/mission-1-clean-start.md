# Mission 1: The Clean Start 🚀

**Your goal:** Make the robot drive forwards 30 cm in a perfectly straight line.

**Why it matters:** At the competition, your robot twitched at the start. This mission is the first step to fixing that.

---

## Step 1: Build it in Blocks 🧱

Tap the **Blocks** tab. Under the **When Started** block, add these three blocks in order:

1. From **Control**: `sleep for 1 seconds`
   This gives your hands time to get away from the robot.
2. From **Sensors**: `reset gyro on port 5`
   The gyro is the robot's compass. This sets it to zero.
3. From **Motion**: `move steering with direction 0 and speed 50 % for 1.7 rotations`
   Direction 0 means straight ahead.

Go to the **Simulator** tab and press ▶️.

> 🤔 **Why 1.7 rotations?** The wheel is 56 mm across, so one turn of the wheel moves the robot about 17.6 cm. To go 30 cm, the wheel needs to turn about 1.7 times.

## Step 2: Find it in Python 🔍

Tap the **Python** tab. The top part is the robot's set-up. **Don't change it.**

Scroll down until you see:

```
# Here is where your code starts
```

Below that are your three blocks, written in Python. Point to each line and say which block it came from.

## Step 3: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

Your drive line in the **Python** tab looks like this:

```python
move_steering_for_degrees(0, (50 / 100) * 1050, 1.7 * 360)
```

It has three numbers you can change:

| Number | What it means |
|---|---|
| `0` | **Direction.** 0 = straight. Bigger numbers curve more. |
| `50` | **Speed.** 50 = half speed. 100 = full speed. |
| `1.7` | **Distance**, in wheel rotations. |

Do one change at a time. **Guess first**, then press ▶️, then change it back.

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| the **distance** | `1.7` | `3.4` | | |
| the **distance** | `1.7` | `-1.7` | | |
| the **speed** | `50` | `100` | | |
| the **direction** | `0` | `50` | | |
| the **wait** line `wait(1 * 1000)` | `1` | `0` | | |

---

## ✅ You've finished when...

You can explain what each of your three lines does, without looking at the blocks.

## 📓 Notebook

- Which way did the robot drive? Find it on the [field map](../images/field-map.jpg). Which object is it driving towards?
- What surprised you?
