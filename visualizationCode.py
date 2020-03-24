# This code is complementary to circuit.py, and is used to visualize the results
# by running these code portions in Jupyter Notebook (remember to use qiskit_env)

#PLOT HISTOGRAM
from qiskit.tools.visualization import plot_histogram
#counts = execute(circuit, simulator, shots=asManyAsYouWant).result().get_counts(circuit)
plot_histogram(counts) 

#PLOT BLOCH SPHERE (Bloch Mulitvector)
from qiskit.tools.visualization import plot_bloch_multivector
plot_bloch_multivector(job.get_statevector(circuit))