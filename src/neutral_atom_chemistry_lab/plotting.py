from __future__ import annotations

import matplotlib.pyplot as plt


def plot_energy_curve(gammas, energies, title: str) -> None:
    plt.figure(figsize=(7, 4))
    plt.plot(gammas, energies)
    plt.xlabel("Noise gamma")
    plt.ylabel("Energy proxy")
    plt.title(title)
    plt.tight_layout()
    plt.show()
