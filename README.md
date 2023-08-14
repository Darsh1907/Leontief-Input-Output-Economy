# Leontief Model Solver

This repository contains a Python program that implements the Leontief Input-Output model to solve for production levels required to meet an expected external demand. The Leontief model is a fundamental tool in economics for analyzing economic interdependencies among various sectors of an economy.

## Overview

The Leontief model is used to study the economic relationships between different sectors or industries within an economy. It is based on the concept of an Input-Output matrix, which represents the inputs and outputs required by each sector to produce a unit of output. This program utilizes the Leontief model to calculate the total production needed to satisfy a given external demand, taking into account the interdependencies between sectors.

## How to Use

1. Clone the Repository:
```
git clone https://github.com/Darsh1907//Leontief-Input-Output-Economy.git
cd Leontief-Input-Output-Economy
```

2. Run the Program:
```
python code.py
```

3. Input-Output Matrix (IOM):
Modify the `A` array in the `leontief_solver.py` file to represent the Input-Output matrix of your specific economy.

4. Expected External Demand:
Modify the D array to represent the expected demand vector. The vector should be defined as follows:
```
D = np.array([d1, d2, d3])
```

5. Run the Program:
Run the modified code.py script to calculate the required production levels and determine if the internal demand can be met.

## Results
The program will output the calculated production levels required to meet the expected external demand. It will also indicate whether the internal demand can be satisfied or not based on the calculated production levels.

## Note
In case the Input-Output matrix is a Markov matrix, indicating an equilibrium state in the economy, the program will detect and provide a relevant message.

### Feel free to contribute by submitting pull requests or suggesting improvements.
