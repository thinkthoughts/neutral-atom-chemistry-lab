from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NeutralAtomLayout:
    n_atoms: int
    spacing_um: float
    blockade_radius_um: float

    def is_blockaded(self) -> bool:
        return self.spacing_um <= self.blockade_radius_um


def default_two_atom_layout() -> NeutralAtomLayout:
    return NeutralAtomLayout(
        n_atoms=2,
        spacing_um=6.0,
        blockade_radius_um=7.0,
    )
