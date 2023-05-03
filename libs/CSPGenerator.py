import random
import networkx as nx
import matplotlib.pyplot as plt

# Class that will randomly generate a CSP (Constraint Satisfaction Problem)
class CSPGenerator:
    def __init__(self, num_variables, domains_size, density = 1.0, durete = 1.0):
        self.num_variables = num_variables
        self.domains_size = domains_size
        self.density = density
        self.durete = durete
        self.variables = []
        self.domains = {}
        self.constraints = {}
        self.generate_variables()
        self.generate_domains()
        self.generate_constraints()
    
    # generate variables (X1, X2, X3, ..., XN)
    def generate_variables(self):
        for i in range(self.num_variables):
            self.variables.append("X"+str(i + 1))
    
    # generate domains ({1, 2, 3, ..., N}, ...)
    def generate_domains(self):
        for i in range(self.num_variables):
            self.domains[self.variables[i]] = []
            for j in range(self.domains_size):
                self.domains[self.variables[i]].append(j + 1)
    
    # generate constraints (dictionary of tuples : (Xi, Xj) -> {(1, 1), (1, 2), (1, 3), ..., (N, N)})
    def generate_constraints(self):
        for i in range(self.num_variables):
            for j in range(self.num_variables):
                if i != j and (self.constraints.get((self.variables[i], self.variables[j])) == None and self.constraints.get((self.variables[j], self.variables[i])) == None):
                    self.constraints[(self.variables[i], self.variables[j])] = self._generate_constraint(self.variables[i], self.variables[j])
                    self._apply_durete(self.constraints[(self.variables[i], self.variables[j])])
        self._apply_density()
    
    # create constraints between two variables
    def _generate_constraint(self, var1, var2):
        constraint = []
        domainVar1 = self.domains[var1]
        domainVar2 = self.domains[var2]
        for i in range(len(domainVar1)):
            for j in range(len(domainVar2)):
                if (domainVar1[i], domainVar2[j]) not in constraint:
                    constraint.append((domainVar1[i], domainVar2[j]))
        return constraint
    
    # apply density to constraints (remove some constraints)
    def _apply_density(self):
        nbConstraints = self.constraints.__len__()
        nbConstraintsToKeep = int(nbConstraints * self.density)
        while nbConstraints > nbConstraintsToKeep:
            constraintToDelete = self._get_random_constraint()
            self.constraints.pop(constraintToDelete)
            nbConstraints = self.constraints.__len__()
    
    # get a random constraint from constraints
    def _get_random_constraint(self):
        return list(self.constraints.keys())[random.randint(0, self.constraints.__len__() - 1)]
    
    # apply durete to constraints (remove some tuples in constraints)
    def _apply_durete(self, constraint):
        nbConstraints = constraint.__len__()
        nbConstraintsToKeep = int(nbConstraints * self.durete)
        while nbConstraints > nbConstraintsToKeep:
            constraint.pop(random.randint(0, constraint.__len__() - 1))
            nbConstraints = constraint.__len__()
    
    # show graph of CSP
    def show_graph(self):
        # initialize graph directed
        G = nx.DiGraph()
        
        # add nodes and edges
        G.add_nodes_from(self.variables)
        for constraint in self.constraints:
            # edge between variables with arc direction
            G.add_edge(constraint[0], constraint[1])
        nx.draw(G, with_labels=True)
                    
        # show graph            
        plt.show()
    
    # print CSP
    def print_csp(self):
        print("Variables : ", self.variables)
        print("Domains : ", self.domains)
        print("Constraints : ", self.constraints)
    
    # get variables
    def get_variables(self):
        return self.variables
    
    # get domains
    def get_domains(self):
        return self.domains
    
    # get constraints
    def get_constraints(self):
        return self.constraints
    
    # get generated CSP
    def get_generated_csp(self):
        return self.variables, self.domains, self.constraints

    # override str method
    def __str__(self):
        return "CSPGenerator : " + str(self.num_variables) + " variables, " + str(self.domains_size) + " domains size, " + str(self.density) + " density, " + str(self.durete) + " durete"

if __name__ == "__main__":
    csp = CSPGenerator(4, 3, 1, 0.5)
    csp.print_csp()
    