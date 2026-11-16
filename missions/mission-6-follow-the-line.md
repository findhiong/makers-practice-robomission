# Mission 6: Follow the Line 〰️

**Your goal:** Drive up to the black line, turn, and follow it for 80 cm without losing it.

**Why it matters:** A line is like a railway track for your robot. Following one keeps the robot in the right place, even if the start was a little bit off.

---

## Step 1: Load the code 📂

1. Open [mission-6.py](code/mission-6.py).
2. Tap the **download** button (the arrow pointing down, near the top right of the code), then **Download**.
3. In GearsBot, tap **File > Load Python from your computer**.
4. Find **mission-6.py** (it's in **Downloads**) and tap it.
5. Tap the **Python** tab to see the code.

Check `LEFT` is the same as you set it in Mission 5.

## Step 2: Measure black and white 📏

The robot needs to know what "black" and "white" look like. Near the bottom of the code is:

```python
print("I see:", floor_sensor.reflection())
```

1. Press ▶️ with the robot at the start. Look in the message box. That number is the **light grey** floor.
2. Now measure **black** and **white**. In the **Python** tab, add `drive_cm(25, UP)` just before the print line, and change 25 until the sensor is on white, then on black. (The robot carries on after that. Just read the number in the message box.)
3. Find these two lines in the code (just under **OUR CODE STARTS HERE**) and put your numbers in:

```python
BLACK = 10
WHITE = 90
```

Then delete the extra `drive_cm` line.

## Step 3: Follow it! 🚂

Press ▶️. The robot should drive up to the black line, turn left, and follow it.

> 🤔 **How does it work?** The sensor sits on the **edge** of the line, half on black, half on white. Too much black? Steer one way. Too much white? Steer the other way. It checks 100 times a second!

**Spinning away from the line?** Change `FOLLOW_STRENGTH = 1.5` to `-1.5`. That flips which way it steers.

## Step 4: Change it in Python (guess first!) 🧪

One change at a time, and change it back afterwards.

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| how hard it **steers** onto the line | `FOLLOW_STRENGTH = 1.5` | `FOLLOW_STRENGTH = 5` | | |
| how hard it **steers** onto the line | `FOLLOW_STRENGTH = 1.5` | `FOLLOW_STRENGTH = 0.3` | | |
| the **speed** | `follow_line(80)` | `follow_line(80, speed=400)` | | |
| how **far** it follows | `follow_line(80)` | `follow_line(40)` | | |

---

## ✅ You've finished when...

The robot follows the line for 80 cm without losing it, 3 times in a row.

## 📓 Notebook

- What happened when `FOLLOW_STRENGTH` was too big? Too small?
- Find another black line on the [field map](../images/field-map.jpg) that could help you get somewhere.
