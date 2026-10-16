"""Entrena un reconocedor de dígitos escritos a mano y lo exporta a JSON.

El modelo es una red neuronal pequeña (MLP 64 -> 64 -> 10) entrenada con el
dataset `digits` de scikit-learn (imágenes de 8x8 píxeles con valores 0-16).
Los pesos se guardan en `model.json` para que `index.html` haga la predicción
directamente en el navegador, sin servidor. Así la demo funciona en GitHub Pages.

Uso:
    python train.py            # entrena, evalúa y escribe model.json
    python train.py --seed 7   # otra semilla para comparar resultados
"""

import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

OUTPUT = Path(__file__).with_name("model.json")


def augment(images: np.ndarray, labels: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Añade copias desplazadas 1 píxel a izquierda y derecha.

    Los dígitos que dibuja una persona nunca están perfectamente centrados,
    así que enseñamos al modelo a tolerar pequeños desplazamientos.
    """
    shifted = [images]
    for dx in (-1, 1):
        moved = np.roll(images, dx, axis=2)
        # np.roll da la vuelta a la imagen: vaciamos la columna que "entra".
        if dx == 1:
            moved[:, :, 0] = 0
        else:
            moved[:, :, -1] = 0
        shifted.append(moved)
    return np.concatenate(shifted), np.concatenate([labels] * len(shifted))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.images, digits.target, test_size=0.2, stratify=digits.target, random_state=args.seed
    )

    # Solo aumentamos el conjunto de entrenamiento: el de test queda intacto
    # para que la métrica sea honesta (sin fuga de datos).
    x_train, y_train = augment(x_train, y_train)

    # Normalizamos 0-16 -> 0-1 y aplanamos 8x8 -> 64 valores.
    x_train = x_train.reshape(len(x_train), -1) / 16.0
    x_test = x_test.reshape(len(x_test), -1) / 16.0

    model = MLPClassifier(
        hidden_layer_sizes=(64,),
        activation="relu",
        alpha=1e-3,
        max_iter=400,
        random_state=args.seed,
    )
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Precisión en test: {accuracy:.4f} ({len(y_test)} imágenes)")
    print("Matriz de confusión (filas = real, columnas = predicho):")
    print(confusion_matrix(y_test, predictions))

    exported = {
        "architecture": "mlp-64-64-10-relu-softmax",
        "input": "8x8 en escala 0-1 (valor original / 16), por filas",
        "accuracy": round(float(accuracy), 4),
        "n_train": int(len(y_train)),
        "n_test": int(len(y_test)),
        "seed": args.seed,
        "W1": np.round(model.coefs_[0], 4).tolist(),
        "b1": np.round(model.intercepts_[0], 4).tolist(),
        "W2": np.round(model.coefs_[1], 4).tolist(),
        "b2": np.round(model.intercepts_[1], 4).tolist(),
    }
    OUTPUT.write_text(json.dumps(exported, separators=(",", ":")))
    print(f"Modelo exportado a {OUTPUT.name} ({OUTPUT.stat().st_size / 1024:.1f} KB)")


if __name__ == "__main__":
    main()
