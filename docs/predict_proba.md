`04_tiny_pipeline_predict.py`

### `proba` just means "probability"

It's a super common variable name in ML code.

So in your script:

```python
proba = pipeline.predict_proba(new_people)
```

`proba` becomes a 2D array of **prediction probabilities**.

## What `predict_proba()` returns

For each row/person, it returns:

```txt
[P(class 0), P(class 1)]
```

So if you had 2 people, you get 2 rows:

```txt
[
  [P0, P1],
  [P0, P1]
]
```

## Difference between `predict()` and `predict_proba()`

### `predict()`

Gives the final decision (hard answer):

```python
[1, 0]
```

Meaning:

* person 1 → healthy
* person 2 → not healthy

### `predict_proba()`

Gives the confidence behind it (soft answer):

```python
[
  [0.00015, 0.99985],
  [0.99988, 0.00011]
]
```

## Why it matters

Because in real life you might want to say:

* "Only label them healthy if probability 0.8"
* "Flag if probability is between 0.4 and 0.6"
* "Treat borderline cases as 'needs review'"

That's *way* more useful than just 0/1 sometimes.

<br>
