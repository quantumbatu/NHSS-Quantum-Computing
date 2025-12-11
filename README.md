🚀 NHSS-Quantum-Computing
A new quantum computing paradigm based on Non-Hermitian dynamics and Exceptional Points (EPs)

NHSS (Non-Hermitian Spectral Steering) introduces a fundamentally new way of performing quantum computation by steering quantum states through Exceptional Points using measurement-induced non-unitary evolution.

Unlike traditional quantum computing, which uses unitary gates and tries to suppress noise, NHSS intentionally uses decoherence, dissipation, and measurement feedback as computational resources.

This repository provides the first full implementation of NHSS concepts using IBM Quantum Dynamic Circuits, including the definition of the Ep-bit — a new information unit based on topological state transitions.

🧠 What is NHSS?

In standard quantum computing:

Information is stored in amplitudes of |0⟩ and |1⟩

Operations must be reversible and unitary

Noise is a problem to be minimized

In NHSS:

Information is stored in topological properties of an effective non-Hermitian Hamiltonian

Measurement + feedback drives non-unitary evolution

Noise becomes part of an effective computational engine

The effective model takes the form:

𝐻
e
f
f
=
𝐻
+
𝑖
𝛾
𝑍
H
eff
	​

=H+iγZ

where γ represents measurement-conditioned gain/loss.

🔥 What is an Ep-bit?

An Ep-bit (Exceptional Point bit) is a new logical information unit defined by the system’s position relative to an Exceptional Point.

When the system encircles an EP:

1 loop (~2π) → eigenstate switching

2 loops (~4π) → returns to original state

This switching behavior acts like a logical bit flip, not based on amplitudes but on topological phase transitions.

Ep-bit = topological quantum memory.

🧩 Why NHSS is different (and important)
Traditional QC	NHSS
Uses unitary operations	Uses non-unitary evolution
Noise = error	Noise = part of computation
Info in amplitudes	Info in topology
Gates act locally	EP loops act globally
Hard to scale robustly	Potentially more stable due to topology

NHSS represents a new paradigm, not a modification of existing quantum gate models.

🧱 Repository Contents
NHSS-Quantum-Computing/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── theory_summary.md
│   ├── epbit_model.md
│   ├── device_requirements.md
│   └── NHSS_Whitepaper.md
│
├── src/
│   ├── nhss_simulator.py
│   ├── ibm_device_experiment.py
│   └── utils/
│       ├── measurement_feedback.py
│       └── parameter_sweep.py
│
└── examples/
    ├── epbit_basic_demo.py
    └── exceptional_point_scan.py

⚙️ Installation
1) Clone the repository
git clone https://github.com/<quantumbatu>/NHSS-Quantum-Computing.git
cd NHSS-Quantum-Computing

2) Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate


macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate

3) Install dependencies
pip install --upgrade pip
pip install qiskit qiskit-aer qiskit-ibm-runtime

▶️ Run NHSS Simulations (AerSimulator)
Basic Ep-bit demonstration:
python examples/epbit_basic_demo.py

EP trajectory scan:
python examples/exceptional_point_scan.py


These simulations show how measurement + feedback create EP-like transitions.

▶️ Run on IBM Quantum Hardware
1) Add your API token

Edit:

src/ibm_device_experiment.py


Replace:

MY_IBM_TOKEN = "PUT-YOUR-TOKEN-HERE"

2) Run real-device experiment:
python src/ibm_device_experiment.py


The script will:

Connect to ibm_fez or ibm_torino

Build the NHSS circuit

Sweep γ parameters

Show measurement results

Reveal EP-like eigenstate switching patterns

📚 Documentation Overview
docs/theory_summary.md

Explains NHSS physics and non-Hermitian Hamiltonians.

docs/epbit_model.md

Defines the Ep-bit and topological switching.

docs/device_requirements.md

IBM hardware features required (dynamic circuits, mid-circuit measurement).

docs/NHSS_Whitepaper.md

A compact whitepaper-style introduction to the paradigm.

🧪 Research Status

NHSS is:

a new theoretical paradigm,

experimentally implementable on IBM hardware,

uses non-Hermitian topology instead of Hilbert-space amplitudes,

introduces Ep-bits as new quantum information units.

This repo aims to make NHSS reproducible, testable, and improvable by the community.

📜 License

MIT License — free to use, modify, and share.

🤝 Contributions

Contributions are welcome in areas such as:

Non-Hermitian quantum mechanics

Exceptional Point physics

Measurement-based quantum control

IBM quantum hardware experiments

Topological quantum computing