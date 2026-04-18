# neutral-atom-chemistry-lab

Small, reproducible workflows for mapping quantum chemistry algorithms to neutral-atom hardware under realistic constraints.

---

## Overview

This repository demonstrates an end-to-end pipeline:

Chemistry Hamiltonian → Parameterized Circuit → Neutral-Atom Mapping → Noise Model → Validation 📐

The goal is not only to simulate quantum algorithms, but to identify **where they remain stable under hardware and noise constraints**.

---

## Motivation

Many quantum algorithm demos stop at ideal simulation. Real hardware introduces:

- limited connectivity and geometry constraints  
- Rydberg blockade effects  
- noise and decoherence  

This repo adds a **validation step** to determine which configurations are physically viable.

---

## Core Components

- **Quantum chemistry baseline**
  - H₂ Hamiltonian (minimal example)
  - Variational Quantum Eigensolver (VQE)

- **Neutral-atom mapping**
  - simple layout + blockade-aware constraints
  - geometry-sensitive execution

- **Noise modeling**
  - amplitude / dephasing proxies
  - effective γ-based sweeps

- **Constraint-based validation**
  - overlap threshold: cosθ ≥ 1/√(1² + 1²) 📐
  - filters unstable execution regions

---

## Repository Structure

```
notebooks/
  01_h2_vqe_neutral_atom.ipynb   # end-to-end demo
  02_blockade_mapping.ipynb      # geometry effects
  03_noise_constraint_gate.ipynb # stability regions

src/neutral_atom_chemistry_lab/
  hamiltonians.py
  ansatz.py
  vqe.py
  mapping.py
  noise.py
  constraint_gate.py

examples/
  h2_minimal.py

docs/
  overview.md
```

---

## Quickstart

```bash
pip install -r requirements.txt
python examples/h2_minimal.py
```

Or open:

```
notebooks/01_h2_vqe_neutral_atom.ipynb
```

---

## Example: Noise vs Stability

The core experiment sweeps noise (γ) and evaluates:

- energy (or proxy)
- whether the state passes a stability constraint

Result:

- **low noise → stable execution**
- **high noise → filtered as invalid**

This identifies **regions where quantum chemistry workflows remain physically meaningful**.

---

## Why This Matters

Neutral-atom systems are promising for scalable quantum computing, but:

> Not all circuits that work in simulation are executable on hardware.

This repo focuses on:

- translating algorithms → hardware constraints  
- understanding noise-limited behavior  
- identifying stable operating regimes  

---

## Roadmap

- [ ] refine H₂ energy estimation (full expectation values)
- [ ] LiH extension
- [ ] improved Rydberg geometry modeling
- [ ] effective γ (γ + λγφ) noise model
- [ ] fault-tolerance bridge (logical vs physical qubits)

---

## Notes

This repository is intentionally minimal and application-focused.  
It is designed to be readable, reproducible, and directly relevant to neutral-atom quantum workflows.

---

## License

MIT (or add your preferred license)
