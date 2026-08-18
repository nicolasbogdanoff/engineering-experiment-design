"""Two-level full-factorial designs and coded-model effect estimates."""

from __future__ import annotations

from itertools import product

import numpy as np


def full_factorial(factors: list[str] | tuple[str, ...]) -> tuple[list[str], np.ndarray]:
    """Return factor names and a -1/+1 coded design matrix."""
    names = list(factors)
    if not names or len(set(names)) != len(names):
        raise ValueError("factors must be a non-empty sequence of unique names")
    matrix = np.asarray(list(product((-1.0, 1.0), repeat=len(names))))
    return names, matrix


def estimate_effects(design: np.ndarray, response: np.ndarray) -> np.ndarray:
    """Estimate intercept and main effects using a coded least-squares model."""
    x = np.asarray(design, dtype=float)
    y = np.asarray(response, dtype=float)
    if x.ndim != 2 or y.ndim != 1 or len(x) != len(y):
        raise ValueError("design must be 2-D and response must match its row count")
    model = np.column_stack([np.ones(len(x)), x])
    return np.linalg.lstsq(model, y, rcond=None)[0]
