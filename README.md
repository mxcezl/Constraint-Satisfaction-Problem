# CSP - Constraint Satisfaction Problem

## Introduction

This project is a simple implementation of a CSP solver. It contains a simple CSP generator and a solver that uses the backtracking algorithm such as backtrack, forward checking and backjumping.

## Usage

### Generator

The generator is a simple python script that generates a CSP problem.

You can find it under the `libs` folder as [`CSPGenerator.py`](./libs/CSPGenerator.py).

Inside that file, you'll find a class named `CSPGenerator`. This class has 4 attributes:

- **num_variables** : The number of variables in the CSP problem
- **domains_size** : The number of values per variable
- **density** : The density of the CSP problem between 0 and 1 (1 by default)
- **durete** : The hardness of the CSP problem between 0 and 1 (1 by default)

Exemple:

```python
csp = CSPGenerator(4, 3, 1, 0.5)
```

This will generate a CSP problem with 4 variables, 3 values per variable, a density of 1 and a hardness of 0.5.

CSP Exemple:

```
Variables :  ['X1', 'X2', 'X3', 'X4']
Domains :  {'X1': [1, 2, 3], 'X2': [1, 2, 3], 'X3': [1, 2, 3], 'X4': [1, 2, 3]}
Constraints :  {('X1', 'X2'): [(1, 1), (1, 2), (2, 1), (3, 3)], ('X1', 'X3'): [(1, 1), (2, 2), (3, 2), (3, 3)], ('X1', 'X4'): [(2, 1), (3, 1), (3, 2), (3, 3)], ('X2', 'X3'): [(1, 2), (2, 3), (3, 2), (3, 3)], ('X2', 'X4'): [(1, 1), (1, 2), (2, 1), (3, 2)], ('X3', 'X4'): [(1, 3), (2, 1), (2, 2), (3, 3)]}
```

### Solver

The solver is a simple python script that solves a CSP problem created by the generator.

You can find it under the `libs` folder as [`CSPSolver.py`](./libs/CSPSolver.py).

Inside that file, you'll find a class named `CSPSolver`. This class can solve a CSP with 3 different algorithms:

- `backtrack`
- `forward checking`
- `backjumping`

Exemple:

```python
csp = CSPGenerator(4, 3, 1, 0.5)
solver = CSPSolver(csp)
solver.solve("backtrack")
```

This will generate a CSP problem with 4 variables, 3 values per variable, a density of 1 and a hardness of 0.5 and solve it with the backtrack algorithm.

You can change the algorithm by changing the string in the `solve` function with one of the 3 algorithms listed above.

## Results

There is a [`main.py`](./main.py) file at the root of the project that generates a CSP problem and solves it with the 3 algorithms.

Each run will be stored and save a csv file as òutput.csv` in the root of the project.

This report file will contain the following information:

- **num_variables** : The number of variables in the CSP problem
- **domains_size** : The number of values per variable
- **density** : The density of the CSP problem between 0 and 1 (1 by default)
- **durete** : The hardness of the CSP problem between 0 and 1 (1 by default)
- **solver_type** : The type of solver used to solve the CSP problem
- **time** : The time in seconds it took to solve the CSP problem
- **iterations** : The number of iterations it took to solve the CSP problem
- **result** : The result of the CSP problem

Exemple:

```
num_variables;domains_size;density;durete;solver_type;time;iterations;result
5;3;0.3;0.3;backtracking;3.1948089599609375e-05;20;{'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}
5;3;0.3;0.3;forward_checking;3.504753112792969e-05;7;{'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}
5;3;0.3;0.3;backjumping;2.5987625122070312e-05;7;{'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}
```

View it as a table:

| num_variables | domains_size | density | durete | solver_type     | time (s)          | iterations | result |
| ------------- | ------------ | ------- | ------ | --------------- | ----------------- | ---------- | ------ |
| 5             | 3            | 0.3     | 0.3    | backtracking    | 3.1948089599609375e-05     | 20      | {'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}             |
| 5             | 3            | 0.3     | 0.3    | forward_checking| 3.504753112792969e-05      | 7          | {'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}             |
| 5             | 3            | 0.3     | 0.3    | backjumping     | 2.5987625122070312e-05     | 7          | {'X1': 1, 'X2': 1, 'X3': 2, 'X4': 1, 'X5': 3}             |

## Authors

- [Maxence ZOLNIERUCK](https://www.linkedin.com/in/maxence-zol/)
- [Josue VIDREQUIN](https://www.linkedin.com/in/josuevidrequin/)