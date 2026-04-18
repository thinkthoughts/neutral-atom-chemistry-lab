from __future__ import annotations

import numpy as np

from .ansatz import ansatz_state


def kron2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.kron(a, b)


PAULI = {
    "I": np.array([[1, 0], [0, 1]], dtype=complex),
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}


def pauli_string_matrix(label: str) -> np.ndarray:
    """Convert a 2-qubit Pauli string into a matrix."""
    if len(label) != 2:
        raise ValueError("Expected a 2-qubit Pauli string.")
    return kron2(PAULI[label[0]], PAULI[label[1]])


def hamiltonian_matrix(terms: list[tuple[str, float]]) -> np.ndarray:
    """Build a dense Hamiltonian matrix from Pauli terms."""
    ham = np.zeros((4, 4), dtype=complex)
    for label, coeff in terms:
        ham += coeff * pauli_string_matrix(label)
    return ham


def expectation_value(state: np.ndarray, operator: np.ndarray) -> float:
    """Real part of <psi|O|psi>."""
    value = np.vdot(state, operator @ state)
    return float(np.real_if_close(value))


def energy_of_state(state: np.ndarray, hamiltonian: np.ndarray) -> float:
    """Energy expectation value."""
    return expectation_value(state, hamiltonian)


def evaluate_params(params, hamiltonian: np.ndarray) -> dict:
    """Evaluate ansatz parameters against a Hamiltonian."""
    state = ansatz_state(params)
    return {
        "params": np.array(params, dtype=float),
        "state": state,
        "energy": energy_of_state(state, hamiltonian),
    }


def random_search_best(
    hamiltonian: np.ndarray,
    n_samples: int = 500,
    seed: int = 0,
) -> dict:
    """Simple random-search baseline for Notebook workflows."""
    rng = np.random.default_rng(seed)
    sampled_params = rng.uniform(0.0, 2.0 * np.pi, size=(n_samples, 4))

    best_energy = np.inf
    best_params = None
    best_state = None

    for params in sampled_params:
        result = evaluate_params(params, hamiltonian)
        if result["energy"] < best_energy:
            best_energy = result["energy"]
            best_params = result["params"]
            best_state = result["state"]

    return {
        "best_energy": float(best_energy),
        "best_params": best_params,
        "best_state": best_state,
    }
