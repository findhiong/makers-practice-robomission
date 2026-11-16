# Mission ladder

Each mission builds on the one before. Open the `.py` file, copy everything into GearsBot's **Python** tab, then press play in the **Simulator** tab.

Keep a notebook. For every mission, write down what you changed, what you expected, and what actually happened. Judges ask you to explain your code, so this is your practice.

| # | Mission | What you learn | Done when... |
|---|---------|----------------|--------------|
| 1 | Clean start | Waiting, resetting the gyro, `straight()` | The robot drives 30 cm and the gyro still reads 0 or 1 |
| 2 | Gyro turn | Which way the gyro counts, `while` loops | Four 90° turns bring the robot back to where it started |
| 3 | Drive to yellow | Turning plus driving straight, using the field map | The robot stops with its sensor on the yellow square, 3 times in a row |
| 4 | Read colours | Colour and reflection sensors, `if` | The robot stops by itself on the red target |
| 5 | Follow a line | Proportional control (the `gain`) | The robot follows a black line for 80 cm without losing it |
| 6 | Count junctions | Counting, remembering the last reading | The robot stops exactly at the 3rd black tooth |
| 7 | Deliver a note | Planning a route, using the cage | The red note scores 20 points |
| 8 | Full run | Putting it all together in functions | Your best score in 2 minutes, with random notes |

## Rules worth practising now

- **One press to start.** On competition day you get one press of the start button. Your code must do its own waiting (that's what `clean_start()` is for).
- **No calibrating at the table.** Measure your black and white values during practice time and put the numbers in your code.
- **Expect a messy table.** Real mats are wavy and the lights change. Gyro driving and lines help more than counting wheel turns.

## Scoring sheet (Rookie Primary 2026, maximum 255)

| Task | Each | Max | Run 1 | Run 2 |
|------|------|-----|-------|-------|
| Cable completely in grey area and upright | 15 | 30 | | |
| Cable only partly in, or not upright | 5 | | | |
| Microphone completely in target area and upright | 20 | 20 | | |
| Microphone only partly in, or not upright | 10 | | | |
| Instrument completely in backstage area | 15 | 45 | | |
| Note completely in its colour's target (grey border counts) and upright | 20 | 120 | | |
| Note only partly in, or not upright | 10 | | | |
| Clef not moved or damaged | 10 | 10 | | |
| Speaker not moved or damaged | 10 | 20 | | |
| Amplifier not moved or damaged | 10 | 10 | | |
| **Total** | | **255** | | |
| **Time (seconds)** | | | | |

"Completely in" means the object touches its area and no other area of the mat.
