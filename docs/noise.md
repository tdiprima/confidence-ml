`01_steady_hand_regression.py`

## 1) What is `noise`?

```python
noise = rng.normal(0, 4, size=n)
```

This generates **n random numbers** (so 80 random numbers if `n=80`), from a **normal distribution** (bell curve):

* mean = `0`
* standard deviation = `4`

### In plain English:

"For each student, add a random wiggle to their score."

Because in real life, people don't get the exact same score even if they study the same amount.

## What does `normal(0, 4)` mean?

This part:

* **0** = average is zero → so the noise is centered around 0

  * sometimes it adds points
  * sometimes it subtracts points

* **4** = typical amount of variation is about 4 points
  (standard deviation)

So most of the noise values will be between roughly:

* `-4` and `+4` (very common)
* `-8` and `+8` (still pretty normal)
* `-12` and `+12` (rare but possible)

## 2) What is `score` doing?

```python
score = 50 + 5 * hours + noise
```

This defines the *rule* of your fake world.

### Break it down:

### **`50`**

This is the **baseline score**.

Even if someone studies 0 hours, they'll average around 50.

(Like: the test isn't impossible. Or it's multiple choice. Or they already know some stuff.)

### **`5 * hours`**

This says:

every extra hour studied is worth ~5 points.

So:

* 2 hours → +10 points
* 6 hours → +30 points
* 10 hours → +50 points

### **`+ noise`**

This adds randomness because people are not robots.

Two students could both study 6 hours and still get different scores.

Example:

* Student A: `hours=6`, `noise=+2`

  * score = 50 + 5*6 + 2 = 82

* Student B: `hours=6`, `noise=-6`

  * score = 50 + 5*6 - 6 = 74

Same hours. Different results. That's realistic.

## Why noise matters (this is important)

Without noise:

```python
score = 50 + 5 * hours
```

All points lie perfectly on a straight line.

Regression would be *too perfect* and not feel like real data.

Noise makes the data messy enough that regression has to "learn the best fit line."

## TL;DR

That pair of lines means:

We're generating exam scores where studying helps a lot, but there's natural randomness in outcomes.

Or more simply:

**Score = baseline + studying effect + real life chaos**

```py
# Generate random "noise" (random variation) for each data point/student
# normal(mean=0, std_dev=4) means:
#   - centered around 0 (sometimes adds points, sometimes subtracts points)
#   - usually within about +/- 4 points, but can be more
# size=n means we generate ONE noise value per student (n students total)
noise = rng.normal(0, 4, size=n)

# Compute the exam score using a simple formula:
# 50 = baseline score (what you'd get with 0 hours studied, on average)
# 5 * hours = studying effect (each hour adds ~5 points)
# + noise = real-life randomness (test difficulty, guessing, stress, etc.)
score = 50 + 5 * hours + noise
```

<br>
