"""Comprueba que model.json existe, tiene la forma correcta y predice bien.

Claude Code usa estos tests como "criterio de éxito": después de cambiar el
entrenamiento, ejecuta `python -m pytest -q` y solo da la tarea por terminada
si pasan.
"""

import json
from pathlib import Path

import numpy as np
import pytest
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split

MODEL_PATH = Path(__file__).resolve().parent.parent / "model.json"


@pytest.fixture(scope="module")
def model():
    if not MODEL_PATH.exists():
        pytest.fail("No existe model.json: ejecuta primero `python train.py`")
    return json.loads(MODEL_PATH.read_text())


def forward(model, x):
    """La misma cuenta que hace index.html en JavaScript."""
    hidden = np.maximum(0, x @ np.array(model["W1"]) + np.array(model["b1"]))
    return hidden @ np.array(model["W2"]) + np.array(model["b2"])


def test_shapes(model):
    assert np.array(model["W1"]).shape == (64, 64)
    assert np.array(model["b1"]).shape == (64,)
    assert np.array(model["W2"]).shape == (64, 10)
    assert np.array(model["b2"]).shape == (10,)


def test_accuracy_on_held_out_data(model):
    digits = load_digits()
    _, x_test, _, y_test = train_test_split(
        digits.images, digits.target, test_size=0.2, stratify=digits.target, random_state=model["seed"]
    )
    logits = forward(model, x_test.reshape(len(x_test), -1) / 16.0)
    accuracy = (logits.argmax(axis=1) == y_test).mean()
    assert accuracy >= 0.93, f"Precisión demasiado baja: {accuracy:.3f}"


def test_reported_accuracy_matches(model):
    digits = load_digits()
    _, x_test, _, y_test = train_test_split(
        digits.images, digits.target, test_size=0.2, stratify=digits.target, random_state=model["seed"]
    )
    logits = forward(model, x_test.reshape(len(x_test), -1) / 16.0)
    accuracy = (logits.argmax(axis=1) == y_test).mean()
    # Los pesos están redondeados a 4 decimales: admitimos una diferencia mínima.
    assert abs(accuracy - model["accuracy"]) <= 0.01
