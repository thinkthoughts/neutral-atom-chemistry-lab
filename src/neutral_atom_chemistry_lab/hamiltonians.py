from __future__ import annotations

from typing import List, Tuple

PauliTerm = Tuple[str, float]


def h2_minimal() -> List[PauliTerm]:
    """Return a small toy 2-qubit Hamiltonian for H2-style demos."""
    return [
        ("II", -1.0523732458),
        ("ZI", 0.3979374248),
        ("IZ", -0.3979374248),
        ("ZZ", -0.0112801043),
        ("XX", 0.1809311998),
    ]
