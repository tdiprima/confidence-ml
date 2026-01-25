`Makefile`

## How to run it

### First-time setup

```bash
make .venv
make install
```

### Run each project

Regression:

```bash
make run-reg
```

Classification:

```bash
make run-cls
```

Train pipeline + save model:

```bash
make train
```

Load saved model + predict:

```bash
make predict
```

### Run everything

```bash
make run-all
```

### Optional (but nice): sanity check that files got created

After `make train`, you should see:

* `data/health.csv`
* `models/health_pipeline.joblib`

You can verify with:

```bash
ls -lah data models
```

<br>
