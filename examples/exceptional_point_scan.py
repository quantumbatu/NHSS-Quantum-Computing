import numpy as np
from src.nhss_simulator import create_nhss_circuit
from src.utils.parameter_sweep import sweep_parameters

qc, theta, phi = create_nhss_circuit()
angles = np.linspace(0, 2*np.pi, 8)
values = [(np.cos(a), np.sin(a)) for a in angles]

results = sweep_parameters(qc, [theta, phi], values)

for params, counts in results.items():
    print(params, counts)
