### `rng` = Random Number Generator

In your `02_yes_no_classification.py` you probably have something like:

```python
rng = np.random.default_rng(seed=42)
```

That creates a **random-number generator object**.

Then later you do stuff like:

```python
income = rng.normal(60000, 15000, size=n)
debt = rng.normal(15000, 7000, size=n)
```

So `rng` is the thing that *produces* the random data.

---

## Why not just use `np.random.normal(...)`?

You *could*, but this is better practice.

### ✅ 1) It's reproducible

Because of `seed=42`, the script makes the **same random numbers every time**.

Meaning:

* you run it today: same data
* you run it tomorrow: same data
* someone else runs it: same data

That's HUGE for ML experiments.

---

### ✅ 2) It's "local" randomness

Everything random comes from `rng`, not from some global shared random state.

So it's easier to reason about and debug.

---

## What does `seed` mean?

Think of seed like: *the starting point for randomness.*

Same seed → same "random" sequence.

Different seed → different fake dataset.

---

## TL;DR

* `rng` is your **random data factory**
* `seed=42` makes your randomness **repeatable**
* you use `rng.normal()` to generate your fake "income" and "debt" values

<br>
