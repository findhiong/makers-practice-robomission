# Mission 5: Python Takes Over 🐍

**Your goal:** Drive to the yellow square again, but this time with real Python that steers itself using the gyro.

**Why it matters:** In Mission 3 the robot may have drifted on the long drive. Good teams use the gyro to keep the robot straight the whole way. You can't do that easily with blocks, but you can in Python.

---

## Step 1: Load the code 📂

1. In GearsBot: **File > Load Python from your computer**.
2. Open the **code** folder and choose `mission-5.py`.
3. Go to the **Python** tab and have a look.

## Step 2: Read the code like a map 🔍

The code has three parts. Find the big headings:

| Part | What it is |
|---|---|
| **ROBOT PARTS LIST** | Tells Python which motors and sensors are plugged in. Don't change it. |
| **OUR OWN BLOCKS** | New blocks we made ourselves, like `turn_to` and `drive_cm`. |
| **OUR CODE STARTS HERE** | The actual plan. Only 4 lines! |

Read the 4 lines at the bottom out loud. Can you guess what each one does?

## Step 3: One important check ✋

Find this line near the top of **OUR OWN BLOCKS**:

```python
LEFT = -90
```

Look at your Mission 2 notebook. If turning **left** made the gyro go **plus**, change it to `LEFT = 90`.

Now press ▶️.

## Step 4: Change it in Python (guess first!) 🧪

All your changes are in the **Python** tab now. One change at a time, and change it back afterwards.

The line `drive_cm(110, LEFT)` means: **drive 110 cm, facing LEFT**.

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| the **speed** of the drive | `drive_cm(110, LEFT)` | `drive_cm(110, LEFT, speed=500)` | | |
| how hard it **steers** back on course | `STEER_STRENGTH = 3` | `STEER_STRENGTH = 0` | | |
| how hard it **steers** back on course | `STEER_STRENGTH = 3` | `STEER_STRENGTH = 20` | | |
| add a **new line** at the very bottom | | `drive_cm(-110, LEFT)` | | |

> 💡 `STEER_STRENGTH` is how hard the robot steers back when it drifts. Too little and it wanders. Too much and it wobbles. Find the best number!

---

## ✅ You've finished when...

The robot stops on yellow 3 times in a row, **and** you can explain what `drive_cm(110, LEFT)` means.

## 📓 Notebook

- Which was more accurate: your blocks in Mission 3, or this?
- What does the `# ` at the start of a line do? (Try adding one before a line and pressing ▶️.)
