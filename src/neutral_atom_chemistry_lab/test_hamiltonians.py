from neutral_atom_chemistry_lab.hamiltonians import h2_minimal


def test_h2_has_terms():
    terms = h2_minimal()
    assert len(terms) > 0
