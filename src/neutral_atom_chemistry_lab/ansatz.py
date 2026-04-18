from __future__ import annotations

import numpy as np


def ry(theta: float) -> np.ndarray:
    """Single-qubit RY rotation."""
    return np.array(
        [
            [np.cos(theta / 2), -np.sin(theta / 2)],
            [np.sin(theta / 2), np.cos(theta / 2)],
        ],
        dtype=complex,
    )


def cnot_01() -> np.ndarray:
    """CNOT with qubit 0 as control and qubit 1 as target."""
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
        ],
        dtype=complex,
    )


def ansatz_state(params: np.ndarray | list[float] | tuple[float, ...]) -> np.ndarray:
    """Two-qubit hardware-friendly ansatz state."""
    theta0, theta1, theta2, theta3 = params

    psi0 = np.array([1, 0, 0, 0], dtype=complex)
    u1 = np.kron(ry(theta0), ry(theta1))
    u2 = np.kron(ry(theta2), ry(theta3))
    uent = cnot_01()

    psi = u2 @ (uent @ (u1 @ psi0))
    norm = np.linalg.norm(psi)
    if norm == 0:
        raise ValueError("Ansatz state norm is zero.")
    return psi / norm
