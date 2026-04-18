from __future__ import annotations

import numpy as np


def apply_amplitude_proxy(state: np.ndarray, gamma: float) -> np.ndarray:
    """Simple noise proxy for early repo demos."""
    if gamma < 0:
        raise ValueError("gamma must be nonnegative")
    noisy = state * np.exp(-gamma)
    norm = np.linalg.norm(noisy)
    return noisy if norm == 0 else noisy / norm
