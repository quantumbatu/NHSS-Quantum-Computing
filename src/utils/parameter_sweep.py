from qiskit_aer import AerSimulator

def sweep_parameters(qc, params, values, shots=1024):
    sim = AerSimulator()
    results = {}
    for v in values:
        bound = qc.bind_parameters(dict(zip(params, v)))
        counts = sim.run(bound, shots=shots).result().get_counts()
        results[str(v)] = counts
    return results
