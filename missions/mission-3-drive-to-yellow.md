# Mission 3: Drive to Yellow 🟨

**Your goal:** Drive from the start and stop on the yellow square on the music staves.

**Why it matters:** This is your first real route: a turn plus a drive. You'll plan it with the map, like a real team.

---

## Step 1: Plan it on the map 🗺️

Open the [field map](../images/field-map.jpg). Find **START** and **Y** (the yellow target).

- The start is at about **x = 98 cm**.
- The yellow square is at about **x = -12 cm**.

So the robot needs to travel 98 + 12 = **110 cm** to the **left**.

> 🧮 **Maths time:** One wheel rotation moves the robot about 17.6 cm. How many rotations is 110 cm?
> 110 ÷ 17.6 = ______ rotations

## Step 2: Build it in Blocks 🧱

1. `sleep for 1 seconds`
2. `reset gyro on port 5`
3. Your **quarter turn to the left** from Mission 2 (use the number of rotations you found).
4. `move steering with direction 0 and speed 50 % for ___ rotations` (your answer from the maths).

Press ▶️.

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

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| the **speed** of the drive | `50` | `100` | | |
| the **distance** of the drive | your number | add `0.5` | | |
| the **direction** of the turn | yours | the opposite (`-` in front, or take it away) | | |

---

## ✅ You've finished when...

The robot stops on (or touching) the yellow square, **3 times in a row**.

## 📓 Notebook

- At full speed, was it still accurate? Why might that be?
- Did the robot drift a little to one side on the long drive? We'll fix that in Mission 5.
