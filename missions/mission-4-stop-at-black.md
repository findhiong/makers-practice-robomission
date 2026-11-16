# Mission 4: Stop at the Black Line ⬛

**Your goal:** Drive towards the black and white stripes and stop **by itself** when it sees black.

**Why it matters:** Counting rotations is never perfect. Sensors let the robot check where it really is, even on a bumpy mat.

---

## Step 1: Look at the map 🗺️

On the [field map](../images/field-map.jpg), find the long white stripes with a black line, just above the start (around y = 30 cm). That's where the robot is heading.

## Step 2: Build it in Blocks 🧱

1. `sleep for 1 seconds`
2. `reset gyro on port 5`
3. From **Motion**: `move steering with direction 0 and speed 20 %`
   Use the one **without** "for". It starts the motors and keeps them going.
4. From **Control**: `Wait until`. Inside it, build this check:
   - From **Logic**: the compare block `[ ] = [ ]`
   - On the left, from **Sensors**: `color sensor` set to **color**, on port **1**
   - On the right, from **Sensors**: the colour block set to **BLACK**
5. From **Motion**: `stop moving`

Press ▶️. Does it stop on the black line?

> 💡 **Stuck?** If your robot is facing the wrong way, add your quarter turn from Mission 2 first.

## Step 3: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

In the **Python** tab, find these lines:

- `move_steering(0, (20 / 100) * 1050)` starts driving. The `20` is the **speed**.
- The `while not` line is your **Wait until**. It keeps checking the sensor until it sees `Color.BLACK`.

| In the Python tab, change... | From | To | Your guess | What happened |
|---|---|---|---|---|
| the **speed** | `20` | `80` | | |
| the **colour** | `BLACK` | `WHITE` | | |
| the **colour** | `BLACK` | `GREEN` | | |

> 🤔 Look at the `while not` line. Can you explain how it keeps checking the colour?

---

## ✅ You've finished when...

The robot stops with its sensor on the black line, every time.

## 📓 Notebook

- What happened at high speed? Why do you think that is?
- Where else on the field could a black line help your robot find its way?
