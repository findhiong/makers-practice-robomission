# Mission 7: Deliver a Note 🎵

**Your goal:** Collect the **red note** and bring it to the red square on the music staves. It must be upright and completely inside the grey border.

**Points:** 20 ⭐

**Why it matters:** This is your first real competition mission. Now you're writing the plan yourselves!

---

## Step 1: Plan on paper first ✏️

Use the [field map](../images/field-map.jpg).

- The **red note** starts at the top, in slot 3: about **x = 31, y = 48**.
- The **red target** (R) is at about **x = 20, y = -4.5**.

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

**File > Load Python from your computer**, then choose `code/mission-7.py`. Check `LEFT` again.

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

The red note scores 20 points: upright and completely inside its grey border.

## 📓 Notebook

- Which step was hardest to get right? How did you fix it?
- Could you deliver the green note too, in the same run?
