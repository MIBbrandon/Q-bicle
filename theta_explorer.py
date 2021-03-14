# Imports
from mpl_toolkits.mplot3d import Axes3D
from qiskit import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
from random import randint

# Setup
# To open in a separate interactive window
mpl.use(backend='TkAgg')

# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

###############################################################################
# CONFIGURATION
###############################################################################
quality = 1000  # Establish how many theta values to test
shots = 100  # Establish the number of shots per theta value

# Measurement circuit is always the same, so no need to be inside the loop
# Establish the number of qubits and classical bits
num_bits = 2
meas = QuantumCircuit(num_bits, num_bits)
meas.measure(range(num_bits), range(num_bits))
###############################################################################

# Predefined functions for later use
def prepare_full_counts():
    """
    Detects the number of classical bits there will be and prepares the dict full_counts
    to receive counts for those values.
    :return:
    """
    full_counts = {}
    num_classical_bits = len(meas.clbits)
    formatting = '{0:0' + str(num_classical_bits) + 'b}'
    for val in range(2 ** num_classical_bits):
        full_counts[formatting.format(val)] = []
    return full_counts


def collect_counts(circuit: QuantumCircuit):
    """
    Collect the count of each state and put them in full_counts
    :param circuit:
    :return:
    """
    # Add measurement
    measured_circuit = circuit + meas
    # Execute the circuit on the qasm simulator
    job = execute(measured_circuit, simulator, shots=shots)
    # Grab results from the job
    result = job.result()
    # Returns counts
    counts = result.get_counts(measured_circuit)
    # Collecting the counts for each state in an array per state
    for state in full_counts:
        if state in counts:
            full_counts[state].append(counts[state])
        else:
            full_counts[state].append(0)


def polygon_under_graph(xlist, ylist):
    """
    Construct the vertex list which defines the polygon filling the space under
    the (xlist, ylist) line graph.  Assumes the xs are in ascending order.
    """
    return [(xlist[0], 0.), *zip(xlist, ylist), (xlist[-1], 0.)]


def plot_graph(title: str):
    # Preparing to plot the data
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.view_init(3, -6)
    # Make verts a list such that verts[i] is a list of (x, y) pairs defining
    # polygon i.
    verts = []

    num_classical_bits = len(meas.clbits)

    # The ith polygon will appear on the plane x = zs[i]
    zs = range(2 ** num_classical_bits)
    facecolors = []
    for state in full_counts:
        xs = full_counts[state]
        verts.append(polygon_under_graph(theta, xs))
        # Get a face colour for each state
        facecolors.append("#%06x" % randint(0, 0xFFFFFF))
    poly = PolyCollection(verts, facecolors=facecolors, alpha=.6)
    ax.add_collection3d(poly, zs=zs, zdir='x')
    ax.set_xlabel('states')
    ax.set_ylabel('theta')
    ax.set_zlabel('counts')
    ax.set_xlim(0, 2 ** num_classical_bits - 1)
    ax.set_ylim(0, 2 * np.pi)
    ax.set_zlim(0, shots)
    # Scale in the axis of the states
    ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([num_classical_bits*0.5, 1, 1, 1]))

    plt.xticks(zs, [state for state in full_counts], rotation=90)
    plt.yticks(np.arange(0, 2 * np.pi, np.pi / 2))
    plt.yticks(np.arange(0, 2 * np.pi, np.pi / 2), [r"$" + format(r / np.pi, ".2g") + r"\pi$" for r in plt.yticks()[0]])
    plt.title(title)
    plt.show()


# Store all the counts for all values of theta
full_counts = prepare_full_counts()

# Set up the theta sequence
theta = np.linspace(0., 2 * np.pi, quality)


# Circuit example 1
# Obtain counts per theta value
for theta_val in theta:
    # Circuit with always changing theta_value
    circuit = QuantumCircuit(num_bits, num_bits)
    circuit.rx(theta_val, 0)
    circuit.ry(theta_val, 1)
    circuit.ch(1, 0)
    circuit.ry(theta_val, 0)
    circuit.ch(0, 1)
    circuit.ry(theta_val, 0)
    circuit.rz(theta_val, 1)

    collect_counts(circuit)

# Plot the graph
plot_graph("Example Circuit")
