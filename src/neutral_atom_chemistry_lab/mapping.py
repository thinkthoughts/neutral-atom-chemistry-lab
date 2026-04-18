from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NeutralAtomLayout:
    """Minimal two-atom layout description."""
    n_atoms: int
    spacing_um: float
    blockade_radius_um: float

    def blockade_active(self) -> bool:
        return self.spacing_um <= self.blockade_radius_um

    def blockade_strength(self) -> float:
        if self.spacing_um >= self.blockade_radius_um:
            return 0.0
        return 1.0 - (self.spacing_um / self.blockade_radius_um)


def blockade_energy_penalty(
    spacing_um: float,
    blockade_radius_um: float,
    scale: float = 0.30,
) -> float:
    """Simple mapped-energy penalty in the blockade regime."""
    if spacing_um >= blockade_radius_um:
        return 0.0
    strength = 1.0 - (spacing_um / blockade_radius_um)
    return scale * strength


def effective_gamma(
    gamma: float,
    spacing_um: float,
    blockade_radius_um: float,
    scale: float = 0.80,
) -> float:
    """Increase effective noise inside the blockade regime."""
    if spacing_um >= blockade_radius_um:
        return gamma
    strength = 1.0 - (spacing_um / blockade_radius_um)
    return gamma + scale * strength
