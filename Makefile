venv:
	python3 -m venv .venv

install:
	. .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

run-reg:
	. .venv/bin/activate && python 01_steady_hand_regression.py

run-cls:
	. .venv/bin/activate && python 02_yes_no_classification.py

train:
	. .venv/bin/activate && python 03_tiny_pipeline_train.py

predict:
	. .venv/bin/activate && python 04_tiny_pipeline_predict.py

run-all: run-reg run-cls train predict
