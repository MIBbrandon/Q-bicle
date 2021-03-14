# Q-bicle
Quantum Code related stuff, mainly using Qiskit.

## Theta explorer
Simply graphs the counts of states that a quantum circuit produces as a single value (theta) is varied from 0 to 2*pi.

<p align="center">
  <img width=450 src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/gifs/q-bicle-show_theta_explorer.gif" />
</p>

### Example 1

<p align="center">
  <img width=450 src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example1.png" />
</p>
<p align="center">
  <img src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example1_circuit.png" />
<p>

``` Python
circuit = QuantumCircuit(2, 2)
circuit.ry(theta_val, 0)
circuit.cx(0, 1)
```
<br>

### Example 2

<p align="center">
  <img width=450 src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example2.png" />
</p>
<p align="center">
  <img src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example2_circuit.png" />
<p>

``` Python
circuit = QuantumCircuit(2, 2)
circuit.rx(theta_val, 0)
circuit.ch(0, 1)
```
<br>

### Example 3

<p align="center">
  <img width=450 src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example3.png" />
</p>
<p align="center">
  <img src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example3_circuit.png" />
<p>

``` Python
circuit = QuantumCircuit(2, 2)
circuit.rx(theta_val, 0)
circuit.cry(theta_val, 0, 1)
circuit.ch(1, 0)
```
<br>

### Example 4

<p align="center">
  <img width=450 src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example4.png" />
</p>
<p align="center">
  <img src="https://github.com/MIBbrandon/Q-bicle/blob/master/media/images/example4_circuit.png" />
<p>

``` Python
circuit = QuantumCircuit(2, 2)
circuit.rx(theta_val, 0)
circuit.ry(theta_val, 1)
circuit.ch(1, 0)
circuit.rz(theta_val, 0)
circuit.ch(0, 1)
circuit.ry(theta_val, 0)
circuit.rz(theta_val, 1)
```
<br>
