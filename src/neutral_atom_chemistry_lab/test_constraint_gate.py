import numpy as np

from neutral_atom_chemistry_lab.constraint_gate import passes_constraint


def test_constraint_accepts_reference_state():
    state = np.array([1.0, 0.0, 0.0, 0.0])
    assert passes_constraint(state)
