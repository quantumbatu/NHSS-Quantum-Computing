"""
NHSS Core Simulation Engine
Paradigm: Non-Hermitian Spectral Steering
Version: V4 (Eraser & Recovery)
"""

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import Parameter
from qiskit_aer import AerSimulator

def run_nhss_simulation():
    print(">>> Initializing NHSS Protocol (Simulation Mode)...")
    
    # --- ARCHITECTURE ---
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, cr)
    
    phi = Parameter('phi')

    # 1. PREPARATION (Entanglement)
    qc.h(0)
    qc.cx(0, 1)

    # 2. NON-HERMITIAN STEP (Quantum Eraser Measurement)
    # Measuring Ancilla in X-Basis to erase 'which-path' info
    qc.h(1)
    qc.measure(1, 0) 

    # 3. SPECTRAL STEERING & RECOVERY (Feed-Forward)
    # Real-time logic: If parity is flipped (meas=1), correct the phase.
    with qc.if_test((cr[0], 1)):
        qc.z(0) 

    # Apply the topological phase steering
    qc.rz(phi, 0)

    # 4. FINAL READOUT (Interference Verification)
    qc.h(0)
    qc.measure(0, 1)

    # --- EXECUTION ---
    sim = AerSimulator()
    phi_values = [0, 0.78, 1.57, 2.35, 3.14, 3.92, 4.71, 5.49, 6.28]
    
    print(f"{'PHI (Rad)':<10} | {'SYSTEM |0>':<15} | {'SYSTEM |1>':<15}")
    print("-" * 45)

    for val in phi_values:
        bound_qc = qc.assign_parameters({phi: val})
        # Optimization level 0 to preserve dynamic circuit structure
        transpiled_qc = transpile(bound_qc, sim)
        
        result = sim.run(transpiled_qc, shots=1000).result()
        counts = result.get_counts()
        
        zeros = counts.get('00', 0) + counts.get('01', 0)
        ones = counts.get('10', 0) + counts.get('11', 0)
        
        # Visualization
        bar = "█" * (zeros // 100)
        print(f"{val:.2f}       | {zeros:4d} {bar:<10} | {ones:4d}")

if __name__ == "__main__":
    run_nhss_simulation()