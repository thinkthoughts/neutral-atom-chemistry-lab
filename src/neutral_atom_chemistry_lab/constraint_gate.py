from __future__ import annotations

import numpy as np

REFERENCE_STATE = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
THRESHOLD = 1.0 / np.sqrt(1.0**2 + 1.0**2)


def constraint_score(
    state: np.ndarray,
    reference: np.ndarray = REFERENCE_STATE,
) -> float:
    """Cosine-style overlap score against a reference state."""
    denom = np.linalg.norm(state) * np.linalg.norm(reference)
    if denom == 0:
        raise ValueError("Zero norm encountered in constraint_score.")
    value = np.vdot(reference, state) / denom
    return float(np.real_if_close(value))


def passes_constraint(
    state: np.ndarray,
    threshold: float = THRESHOLD,
) -> bool:
    """Return True if the state passes the validation threshold."""
    return constraint_score(state) >= threshold
