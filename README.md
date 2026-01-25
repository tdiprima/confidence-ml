# Gradient Hammer 🔨 

Tiny, explainable ML projects built for *understanding*, not virality.

These scripts intentionally use small synthetic datasets and simple models so I can confidently explain every line — from data → training → evaluation → saved model → prediction.

## Projects

### 1) Regression — `01_exam_score_regression.py`
Predicts a continuous value (exam score) from a single feature (hours studied).

### 2) Classification — `02_yes_no_classification.py`
Predicts a yes/no label (loan approved) from basic numeric features.

### 3) End-to-End Pipeline — `03_tiny_pipeline_train.py` + `04_tiny_pipeline_predict.py`
Train + evaluate + save a full preprocessing+model pipeline, then load it later to make predictions on new inputs.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Run

```sh
python 01_steady_hand_regression.py
python 02_yes_no_classification.py
python 03_tiny_pipeline_train.py
python 04_tiny_pipeline_predict.py
```

## Why this repo exists

Accuracy is cool, but confidence is cooler.

This repo is practice for building ML intuition, writing reproducible scripts, and being able to explain what's happening — clearly and honestly.

## What I learned

- How to frame a problem as **features (X)** and a **target (y)** and keep that mental model consistent across projects.
- The practical difference between **regression** (predict a number) and **classification** (predict a label).
- How to evaluate models using basic, explainable metrics (ex: **MAE**, **accuracy**) without overcomplicating things.
- Why train/test splits exist and how to avoid accidentally "grading the model on the homework."
- How to build and save an end-to-end **Pipeline** so preprocessing and the model stay bundled together and predictions remain consistent.
- How to keep ML code **readable and reproducible**, which matters more than chasing perfect metrics on toy projects.

<br>
