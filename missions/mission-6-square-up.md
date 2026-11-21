# Mission 6: Square Up on a Line 📐

**Your goal:** The robot starts crooked on purpose. Use the black line to make it perfectly straight again.

**Why it matters:** Remember when your robot twitched at the start and went off course? Top teams fix this by driving up to a line and letting the line straighten the robot. This trick is called **squaring up**.

---

## Before you start 🏁

1. **[Open the field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)** (press and hold, then **Open in New Tab**).
2. In the **menu row**, tap **Python**, then **Pybricks Mode**. ([Not sure where?](../README.md#3-switch-on-pybricks-do-this-every-time))
3. In the **Project Name** box at the very top, type `mission6`.

## Step 1: Load the code 📂

1. Open [mission-6.py](code/mission-6.py).
2. Tap the **download** button (the arrow pointing down, near the top right of the code), then **Download**.
3. In GearsBot, tap **File > Load Python from your computer**.
4. Find **mission-6.py** (it's in **Downloads**) and tap it.
5. Tap the **Python** tab to see the code.

## Step 2: How does it work? 🤔

The robot has **two** sensors looking down at the mat, one on the left and one on the right.

1. Both wheels drive forwards.
2. When the **left** sensor touches black, the **left** wheel stops.
3. When the **right** sensor touches black, the **right** wheel stops.
4. Now both sensors are on the line, so the robot is straight!

Find the `square_up` block in the code. Point to the line that stops the left wheel.

## Step 3: Run it ▶️

Tap the **Simulator** tab and press ▶️. Then look at the **bottom of the Simulator screen**, where messages appear.

- **Crooked:** how far off the robot was.
- **Square:** how far off it is after squaring up. Close to **0** is perfect!

## Step 4: Change it in Python (guess first!) 🧪

> ✏️ **Guess first!** Before you press ▶️, write what you think will happen in the **We think...** column. For example: *"It will still end up straight."* Then press ▶️ and write what really happened.

| In the Python tab, change... | From | To | We think it will... | What happened |
|---|---|---|---|---|
| how **crooked** it starts | `turn_to(8)` and `drive_cm(10, 8)` | `turn_to(-8)` and `drive_cm(10, -8)` | | |
| how **crooked** it starts | `8` (both places) | `20` | | |
| the **speed** of the square-up | `square_up(80)` | `square_up(400)` | | |
| the **speed** of the square-up | `square_up(80)` | `square_up(30)` | | |

---

## ✅ You've finished when...

Using **only the Python tab**, you can add a square-up to your **Mission 5** code: square up on the line first, **then** drive to the yellow square.

## 📓 Notebook

- Was it more accurate fast or slow? Why do you think that is?
- Where on the real competition field could you square up?

## 💾 Save your work

1. In the **menu row**, tap **File**.
2. Tap **Save Python to your computer**, then **Download**.
3. Your work is saved as `mission6.zip`. To open it next time: **File > Load Python from your computer**.
