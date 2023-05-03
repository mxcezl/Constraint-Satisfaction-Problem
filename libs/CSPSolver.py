import time

class CSPSolver:

    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.solution = None

    # définir la fonction qui vérifie si une affectation est valide
    def is_solution_valid(self):
        if self.solution is None:
            return False
        return self._is_assignments_valid_for_constraints(self.solution, self.constraints)

    # fonction pour résoudre le CSP avec l'algorithme passé en paramètre
    def solve(self, algo):
        if algo == "backtracking":
            return self.backtracking()
        elif algo == "forward_checking":
            return self.forward_checking()
        elif algo == "backjumping":
            return self.backjumping()
        else:
            print("Algorithme " + algo + " non reconnu.\nAlgorithmes possibles : backtracking, forward_checking et backjumping.")

    def backtracking(self):
        # initialiser l'affectation avec des variables non affectées
        assignments = {variable: None for variable in self.variables}

        # chronométrer la résolution du CSP
        start_time = time.time()

        # appeler la fonction de recherche
        iterations, self.solution = self._backtracking(assignments, self.domains, self.constraints)

        return str(time.time() - start_time), iterations, self.solution

    def _backtracking(self, assignments, domains, constraints, iterations=0):
            
            # print("Checking : " + str(assignment) + " ...")
    
            # si toutes les variables sont affectées, vérifier l'affectation
            if all(assignments.values()):
                if self._is_assignments_valid_for_constraints(assignments, constraints):
                    return iterations, assignments
                else:
                    return iterations, None
            
            # trouver la prochaine variable non affectée
            variable = next(v for v in assignments if assignments[v] is None)
    
            # essayer chaque valeur possible pour cette variable
            for value in domains[variable]:
                # affecter la valeur à la variable
                assignments[variable] = value
                
                # récursivement essayer de résoudre le reste du CSP
                iterations, result = self._backtracking(assignments, domains, constraints, iterations + 1)
                
                if result:
                    return iterations, result

                # si la tentative de résolution échoue, annuler l'affectation
                assignments[variable] = None
            
            # si aucune valeur ne fonctionne pour cette variable, renvoyer None
            return iterations, None

    def _is_assignments_valid_for_constraints(self, assignments, constraints):
        for constraint, values in constraints.items():
            x, y = constraint
            x_value = assignments[x]
            y_value = assignments[y]

            if x_value is None or y_value is None:
                continue

            if (x_value, y_value) not in values:
                return False

        return True

    # définir la fonction qui résout le CSP
    def forward_checking(self):
        # initialiser l'affectation avec des variables non affectées
        assignments = {variable: None for variable in self.variables}

        # chronométrer la résolution du CSP
        start_time = time.time()

        # appeler la fonction de recherche
        iterations, self.solution = self._forward_checking(assignments, self.domains, self.constraints)

        return str(time.time() - start_time), iterations, self.solution

    # définir la fonction qui effectue la recherche
    def _forward_checking(self, assignments, domains, constraints, iterations=0):
        
        # print("Checking : " + str(assignment) + " ...")

        # si toutes les variables sont affectées, renvoyer l'affectation
        if all(assignments.values()) and self._is_assignments_valid(assignments, constraints):
            return iterations, assignments
        
        # trouver la prochaine variable non affectée
        variable = next(v for v in assignments if assignments[v] is None)

        # essayer chaque valeur possible pour cette variable
        for value in domains[variable]:

            # vérifier si cette valeur est compatible avec les contraintes existantes
            if self._is_value_valid_for_constraints(value, variable, assignments, constraints):
                # affecter la valeur à la variable
                assignments[variable] = value

                # récursivement essayer de résoudre le reste du CSP
                iterations, result = self._forward_checking(assignments, domains, constraints, iterations + 1)

                if result:
                    return iterations, result

                # si la tentative de résolution échoue, annuler l'affectation
                assignments[variable] = None
        
        # si aucune valeur ne fonctionne pour cette variable, renvoyer None
        return iterations, None

    # définir la fonction qui vérifie si une valeur est compatible avec les contraintes existantes
    # pour une variable donnée, utilisée dans la fonction de recherche avec forward checking
    def _is_value_valid_for_constraints(self, value, variable, assignments, constraints):
        constraints = {constraint: constraints[constraint] for constraint in constraints if variable in constraint}
        
        if not constraints:
            return True

        found_constraint_not_satisfied = False
        for constraint in constraints:
            index_other_variable = 0 if constraint[1] == variable else 1
            other_variable = constraint[index_other_variable] if constraint[index_other_variable] == variable else constraint[index_other_variable]
            new_tuple_formed = (assignments[other_variable], value) if index_other_variable == 0 else (value, assignments[other_variable])

            if None in new_tuple_formed:
                continue

            if new_tuple_formed not in constraints[constraint]:
                found_constraint_not_satisfied = True

        return not found_constraint_not_satisfied

    def backjumping(self):
        # initialiser l'affectation avec des variables non affectées
        assignments = {variable: None for variable in self.variables}

        # chronométrer la résolution du CSP
        start_time = time.time()

        # appeler la fonction de recherche
        iterations, self.solution = self._backjumping(assignments, self.domains, self.constraints)

        return str(time.time() - start_time), iterations, self.solution
    
    def _backjumping(self, assignments, domains, constraints, iterations=0, last_variable=None):

        if all(assignments.values()):
            return iterations, assignments

        variable = next(v for v in assignments if assignments[v] is None and v != last_variable)

        if (last_variable is not None) and (not self._is_variable_valid(variable, last_variable, assignments, constraints)):
            return iterations, None

        for value in domains[variable]:
            # print(variable, last_variable, value, assignments)
            assignments[variable] = value

            if self._is_assignments_valid(assignments, constraints):
                iterations, result = self._backjumping(assignments, domains, constraints, iterations + 1, last_variable=variable)

                if result:
                    return iterations, result

            assignments[variable] = None
        
        return iterations, self._backjumping(assignments, domains, constraints, iterations + 1, last_variable=variable)

    def _is_variable_valid(self, variable, last_variable, assignments, constraints):

        # On vérifie si la variable est compatible avec les contraintes
        for constraint in constraints:
            if last_variable in constraint and variable in constraint:
                index_variable = 0 if constraint[0] == variable else 1
                value_variable = assignments[variable]
                value_last_variable = assignments[last_variable]
                if value_variable is None or value_last_variable is None:
                    continue

                if index_variable == 0:
                    if (value_variable, value_last_variable) not in constraints[constraint]:
                        return False
                else:
                    if (value_last_variable, value_variable) not in constraints[constraint]:
                        return False
        return True

    def _is_assignments_valid(self, assignments, constraints):
        for constraint in constraints:
            x, y = constraint
            x_value, y_value = assignments[x], assignments[y]
            if x_value is not None and y_value is not None and (x_value, y_value) not in constraints[constraint]:
                return False
        return True

if __name__ == "__main__":

    # Valeurs de test
    variables = [ 'X1', 'X2', 'X3', 'X4' ]

    domains = {
        'X1': [ 1, 2, 3 ],
        'X2': [ 1, 2, 3 ],
        'X3': [ 1, 2, 3 ],
        'X4': [ 1, 2, 3 ],
    }

    constraints = {
        ('X1', 'X2'): [ (2, 1), (2, 3), (3, 2) ], 
        ('X1', 'X3'): [ (2, 3) ]
    }

    solver = CSPSolver(variables, domains, constraints)

    solver.solve("backjumping")

    print("Solution : " + str(solver.solution))