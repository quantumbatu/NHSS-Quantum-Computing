"""
NHSS Hardware Execution Script
Target: IBM Quantum 'Heron' Processors (ibm_fez, ibm_torino)
Requirement: Dynamic Circuits Support
"""

from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.circuit import Parameter

def run_on_hardware():
    # --- AUTHENTICATION ---
    # WARNING: Do not commit your actual token to GitHub!
    # Use environment variables or local config in production.
    MY_TOKEN = "YOUR_IBM_QUANTUM_TOKEN_HERE" 
    
    try:
        service = QiskitRuntimeService(channel="ibm_cloud", token=MY_TOKEN)
    except:
        print("Error: Please set a valid IBM Quantum Token in nhss_hardware.py")
        return

    # Select backend with Dynamic Circuit support
    backend_name = "ibm_fez" 
    try:
        backend = service.backend(backend_name)
        print(f"Connected to backend: {backend.name}")
    except:
        print(f"Backend {backend_name} not found. Using least busy.")
        backend = service.least_busy(operational=True, simulator=False, dynamic_circuits=True)

    # --- CIRCUIT DEFINITION ---
    qc = QuantumCircuit(2, 2)
    phi = Parameter('phi')

    # NHSS Protocol V4
    qc.h(0)
    qc.cx(0, 1)
    qc.h(1)
    qc.measure(1, 0)
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(0)
    qc.rz(phi, 0)
    qc.h(0)
    qc.measure(0, 1)

    # --- EXECUTION ---
    sampler = Sampler(mode=backend)
    
    # Sweep 4 cardinal points
    angles = [0, 1.57, 3.14, 4.71]
    pubs = [(qc, [a]) for a in angles]

    print("Submitting NHSS Job to IBM Quantum...")
    job = sampler.run(pubs)
    print(f"Job ID: {job.job_id()}")
    
    # Wait for results
    result = job.result()
    for i, pub_result in enumerate(result):
        print(f"Angle {angles[i]}: {pub_result.data.c.get_counts()}")

if __name__ == "__main__":
    run_on_hardware()