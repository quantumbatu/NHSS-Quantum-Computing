def add_midcircuit_feedback(qc, system, ancilla, clbit, phi):
    qc.measure(ancilla, clbit)
    with qc.if_test((qc.clbits[clbit], 1)):
        qc.rz(phi, system)
        qc.x(ancilla)
    return qc
