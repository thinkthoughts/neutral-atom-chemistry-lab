from __future__ import annotations

import numpy as np

from neutral_atom_chemistry_lab.constraint_gate import passes_constraint
from neutral_atom_chemistry_lab.plotting import plot_energy_curve
from neutral_atom_chemistry_lab.vqe import sweep_gammas


def main() -> None:
    gammas = np.linspace(0.0, 1.0, 25)
    results = sweep_gammas(theta=1.0, gammas=gammas)

    energies = [r["energy"] for r in results]
    valid = [passes_constraint(r["state"]) for r in results]

    plot_energy_curve(
        gammas,
        energies,
        title="H2 toy VQE under noise",
    )

    print("Constraint-passing points:", sum(valid), "of", len(valid))


if __name__ == "__main__":
    main()
