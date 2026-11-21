# Mission 4: Stop at the Black Line ⬛

**Your goal:** Drive towards the black and white stripes and stop **by itself** when it sees black.

**Why it matters:** Counting rotations is never perfect. Sensors let the robot check where it really is, even on a bumpy mat.

---

## Before you start 🏁

1. **[Open the field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)** (press and hold, then **Open in New Tab**).
2. In the **menu row**, tap **Python**, then **Pybricks Mode**. ([Not sure where?](../README.md#3-switch-on-pybricks-do-this-every-time))
3. In the **Project Name** box at the very top, type `mission4`.
4. Open the **[🗺️ Field Map](../images/field-map.jpg)** (press and hold, then **Open in New Tab**). It shows where everything is. ([How to read it](README.md#-the-field-map))

## Step 1: Look at the map 🗺️

On the **[🗺️ Field Map](../images/field-map.jpg)**, find the long white stripes with a black line, just above the start (around y = 30 cm). That's where the robot is heading.

## Step 2: Build it in Blocks 🧱

1. `sleep for 1 seconds`
2. From **Motion**: `move steering with direction 0 and speed 20 %`
   Use the one **without** "for". It starts the motors and keeps them going.
3. From **Control**: `Wait until`. Inside it, build this check:
   - From **Logic**: the compare block `[ ] = [ ]`
   - On the left, from **Sensors**: `color sensor` set to **color**, on port **1**
   - On the right, from **Sensors**: the colour block set to **BLACK**
4. From **Motion**: `stop moving`

Run it. Does it stop on the black line?

> 💡 **Stuck?** If your robot is facing the wrong way, add your quarter turn from Mission 2 first.

## Step 3: Change it in Python (guess first!) 🧪

> ⚠️ **Python changes happen in the Python tab only.** Once you change the Python, the Blocks tab locks. If you unlock it, your Python changes are lost. So do all your Blocks work first, then switch to Python.

In the **Python** tab, find these lines:

- `move_steering(0, (20 / 100) * 1050)` starts driving. The `20` is the **speed**.
- The `while not` line is your **Wait until**. It keeps checking the sensor until it sees `Color.BLACK`.

> ✏️ **Guess first!** Before you press ▶️, write what you think will happen in the **We think...** column. For example: *"It will go twice as far."* Then press ▶️ and write what really happened.

| In the Python tab, change... | From | To | We think it will... | What happened |
|---|---|---|---|---|
| the **speed** | `20` | `80` | | |
| the **colour** | `BLACK` | `WHITE` | | |
| the **colour** | `BLACK` | `GREEN` | | |

> 🤔 Look at the `while not` line. Can you explain how it keeps checking the colour?

---

## ✅ You've finished when...

Using **only the Python tab**, you can make the robot stop on **white** instead, then **beep**.

> 💡 Hint: the Python for a beep is `ev3.speaker.beep()`

## 📓 Notebook

- What happened at high speed? Why do you think that is?
- Where else on the field could a black line help your robot find its way?

## 💾 Save your work

1. In the **menu row**, tap **File**.
2. Tap **Save Python to your computer**, then **Download**.
3. Your work is saved as `mission4.zip`. To open it next time: **File > Load Python from your computer**.
