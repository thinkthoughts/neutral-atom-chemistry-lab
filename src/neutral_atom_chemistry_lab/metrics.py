from __future__ import annotations

import numpy as np


def energy_proxy(state: np.ndarray) -> float:
    """Placeholder metric for early plotting."""
    return float(np.sum(state**2))
