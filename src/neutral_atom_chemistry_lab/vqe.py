from __future__ import annotations

import numpy as np

from .ansatz import two_qubit_ansatz
from .metrics import energy_proxy
from .noise import apply_amplitude_proxy


def run_toy_vqe(theta: float, gamma: float) -> dict:
    state = two_qubit_ansatz(theta)
    noisy_state = apply_amplitude_proxy(state, gamma)
    return {
        "theta": theta,
        "gamma": gamma,
        "state": noisy_state,
        "energy": energy_proxy(noisy_state),
    }


def sweep_gammas(theta: float, gammas: np.ndarray) -> list[dict]:
    return [run_toy_vqe(theta=theta, gamma=float(g)) for g in gammas]
