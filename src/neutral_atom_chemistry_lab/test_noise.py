import numpy as np

from neutral_atom_chemistry_lab.noise import apply_amplitude_proxy


def test_noise_preserves_shape():
    state = np.array([1.0, 0.0, 0.0, 0.0])
    noisy = apply_amplitude_proxy(state, 0.5)
    assert noisy.shape == state.shape
