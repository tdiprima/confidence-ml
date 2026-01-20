```
=== Tiny Pipeline Predictions ===
   age  minutes_exercised  sleep_hours
0   25                 45            8
1   55                 10            5

Predictions (0=not healthy, 1=healthy):
[1 0]

Probabilities [P(0), P(1)]:
[[1.50743712e-04 9.99849256e-01]
 [9.99886591e-01 1.13409013e-04]]
```

### What you're seeing

Those are **prediction probabilities** for each person, for each class:

* **P(0)** = probability the model thinks the label is **0** ("not healthy")
* **P(1)** = probability the model thinks the label is **1** ("healthy")

So this:

```txt
Probabilities [P(0), P(1)]:
[[1.50743712e-04 9.99849256e-01]
 [9.99886591e-01 1.13409013e-04]]
```

means:

## Person 1

```txt
[1.50743712e-04, 9.99849256e-01]
```

* P(0) = 0.0001507  (~0.015%)
* P(1) = 0.9998493  (~99.985%)

✅ Model is basically screaming: **"this person is healthy"**

## Person 2

```txt
[9.99886591e-01, 1.13409013e-04]
```

* P(0) = 0.9998866 (~99.989%)
* P(1) = 0.0001134 (~0.011%)

✅ Model is basically screaming: **"this person is NOT healthy"**

### What is `e-04` ??

That's scientific notation.

Example:

* `1.50743712e-04` means: `1.50743712 × 10^-4`
* = `0.000150743712`

So it's just a tiny number written compactly.

### Why probabilities come in pairs

Because it's a **binary classifier**.
It always reports both:

* probability of class 0
* probability of class 1

and they should add up to ~1.

### Why are the probabilities so extreme (almost 0 or 1)?

Because:

* the dataset is synthetic
* the "healthy" rule is pretty clean
* logistic regression is confident when the pattern is obvious

In real world messy data, you'll usually see softer numbers like:
`[0.32, 0.68]`

<br>
