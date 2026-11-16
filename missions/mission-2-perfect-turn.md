# Mission 2: The Perfect Turn 🔄

**Your goal:** Make the robot turn exactly a quarter turn (90 degrees), and check it with the gyro.

**Why it matters:** Every route on the field needs turns. A turn that's 5 degrees out sends the robot to the wrong place.

---

## Step 1: Build it in Blocks 🧱

Start with your blocks from Mission 1 (sleep, then reset gyro). Then add:

1. From **Motion**: `move steering with direction 100 and speed 30 % for 1 rotations`
   Direction 100 makes the robot spin on the spot.
2. From **Text**: a `print` block.
3. From **Sensors**: put a `gyro angle on port 5` block inside the print block.

Press ▶️. Then open the **message box** at the bottom of the Simulator (tap the little arrow). The gyro's number is there.

## Step 2: Make it exactly 90 🎯 (in Blocks)

Did the robot turn more or less than a quarter turn? In the **Blocks** tab, tap the number of **rotations** in your move steering block and change it. Try again until the gyro says **90** (or **-90**).

| Rotations | Gyro said |
|---|---|
| 1 | |
| | |
| | |

## Step 3: Which way is positive? 🧭 (in Blocks)

In the **Blocks** tab, change the **direction** in your move steering block from `100` to `-100`. Watch which way it spins, and look at the gyro number.

Fill this in. **You'll need it for every mission after this.**

> Turning **right** makes the gyro go: ➕ or ➖
> Turning **left** makes the gyro go: ➕ or ➖

## Step 4: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

In the **Python** tab, find these two lines:

```python
move_steering_for_degrees(-100, (30 / 100) * 1050, ___ * 360)
print(gyro_sensor_in5.angle())
```

(Your numbers may be a little different.) The first number is the **direction**, the second is the **speed**, the last is the **distance** in rotations.

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| the **speed** | `30` | `100` | | |
| the **direction** | `-100` | `-50` | | |
| the **distance** | your number | double it | | |

---

## ✅ You've finished when...

The robot turns a quarter turn and the gyro says 90 (or -90) at the end, 3 times in a row.

## 📓 Notebook

- How many rotations made a perfect quarter turn?
- Try 4 quarter turns in a row. Does the robot end up facing exactly where it started?
