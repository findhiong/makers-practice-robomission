# Mission 7: Deliver a Note 🎵

**Your goal:** Collect the **red note** and bring it to the **red box with the grey outline** on the music staves (the wavy purple lines with the big treble clef, across the middle of the mat). It must be upright and completely inside the grey outline.

**Points:** 20 ⭐

**Why it matters:** This is your first real competition mission. Now you're writing the plan yourselves!

---

## Before you start 🏁

1. **[Open the field](https://gears.aposteriori.com.sg/index.html?worldJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Fworlds%2Frobot-rockstars-malaysia.json&robotJSON=https%3A%2F%2Fraw.githubusercontent.com%2Ffindhiong%2Fmakers-practice-robomission%2Fmain%2Frobots%2Fcage-bot.json)** (press and hold, then **Open in New Tab**).
2. In the **menu row**, tap **Python**, then **Pybricks Mode**. ([Not sure where?](../README.md#3-switch-on-pybricks-do-this-every-time))
3. In the **Project Name** box at the very top, type `mission7`.

## Step 1: Plan on paper first ✏️

Use the [field map](../images/field-map.jpg).

- The **red note** starts at the top, in slot 3: about **x = 31, y = 48**.
- The **Red target** (the red box with the grey outline) is at about **x = 20, y = -4.5**.

Draw the robot's route on paper. For each step, write:

| Step | Drive or turn? | Which way? | How far? |
|---|---|---|---|
| 1 | Drive | UP | ___ cm |
| 2 | Turn | | |
| 3 | | | |
| 4 | Close the cage | | |
| 5 | | | |

> 💡 **Watch out:** The notes sit between black "teeth". Your robot has to fit through the gap.

## Step 2: Turn your plan into code 💻

1. Open [mission-7.py](code/mission-7.py).
2. Tap the **download** button (the arrow pointing down, near the top right of the code), then **Download**.
3. In GearsBot, tap **File > Load Python from your computer**.
4. Find **mission-7.py** (it's in **Downloads**) and tap it.
5. Tap the **Python** tab to see the code.

Check `LEFT` is the same as you set it in Mission 5.

At the bottom, write one line of code for each step on your paper. You already know these blocks:

```python
drive_cm(30, UP)       # drive 30 cm, facing up
turn_to(LEFT)          # turn to face left
cage_close()           # trap the note
cage_open()            # let it go
```

## Step 3: Test one step at a time 🔧

Don't write the whole thing at once! Add **one line**, press ▶️, check it's right, then add the next.

Is it really the red note? Put this line just after you close the cage:

```python
print("Front sensor sees:", front_sensor.color())
```

---

## ✅ You've finished when...

The red note scores 20 points: upright and completely inside its grey outline.

## 📓 Notebook

- Which step was hardest to get right? How did you fix it?
- Could you deliver the green note too, in the same run?

## 💾 Save your work

1. In the **menu row**, tap **File**.
2. Tap **Save Python to your computer**, then **Download**.
3. Your work is saved as `mission7.zip`. To open it next time: **File > Load Python from your computer**.
