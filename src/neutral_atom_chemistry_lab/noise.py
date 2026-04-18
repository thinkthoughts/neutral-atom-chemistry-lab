from __future__ import annotations

import numpy as np

REFERENCE_STATE = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)


def apply_noise_proxy(state: np.ndarray, gamma: float) -> np.ndarray:
    """Simple dephasing-style proxy used in the notebooks."""
    noisy = state.copy()
    noisy[1:] *= np.exp(-gamma)

    norm = np.linalg.norm(noisy)
    if norm == 0:
        raise ValueError("Noisy state norm is zero.")
    return noisy / norm
