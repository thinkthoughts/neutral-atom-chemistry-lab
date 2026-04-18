from __future__ import annotations

import numpy as np


def two_qubit_ansatz(theta: float) -> np.ndarray:
    """Very small real-valued ansatz state for toy demos."""
    state = np.array([
        np.cos(theta / 2.0),
        0.0,
        0.0,
        np.sin(theta / 2.0),
    ], dtype=float)
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("State norm is zero.")
    return state / norm
