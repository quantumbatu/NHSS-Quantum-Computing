from src.nhss_simulator import create_nhss_circuit
from qiskit_aer import AerSimulator

qc, theta, phi = create_nhss_circuit()
bound = qc.bind_parameters({theta: 0.8, phi: 1.2})

sim = AerSimulator()
result = sim.run(bound, shots=2048).result()
print(result.get_counts())
