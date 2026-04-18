from __future__ import annotations

import numpy as np


DEFAULT_THRESHOLD = 1.0 / np.sqrt(1.0**2 + 1.0**2)


def constraint_score(state: np.ndarray, reference: np.ndarray | None = None) -> float:
    """Cosine-overlap score against a reference state."""
    if reference is None:
        reference = np.array([1.0, 0.0, 0.0, 0.0], dtype=float)

    denom = np.linalg.norm(state) * np.linalg.norm(reference)
    if denom == 0:
        raise ValueError("Zero norm encountered in constraint_score")
    return float(np.dot(state, reference) / denom)


def passes_constraint(state: np.ndarray, threshold: float = DEFAULT_THRESHOLD) -> bool:
    return constraint_score(state) >= threshold
