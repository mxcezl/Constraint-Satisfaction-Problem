import pprint
import csv
import time
from libs.CSPGenerator import CSPGenerator
from libs.CSPSolver import CSPSolver

pp = pprint.PrettyPrinter(indent=4)

def launch_solver_n_times(num_runs, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["num_variables", "domains_size", "density", "durete", "solver_type", "time", "iterations", "result"])
        
        for n in range(num_runs):
            for num_variables in range(5, 8):
                for domains_size in [3, 5]:
                    for density in [0.3, 0.5]:
                        for durete in [0.3, 0.5]:
                            generator = CSPGenerator(num_variables=num_variables, domains_size=domains_size, density=density, durete=durete)
                            variables, domains, constraints = generator.get_generated_csp()
                            generator.print_csp()
                            solver = CSPSolver(variables, domains, constraints)
                            for solver_type in ["backtracking", "forward_checking", "backjumping"]:
                                
                                if solver_type == "backtracking":
                                    temps, iterations, result = solver.solve("backtracking")
                                elif solver_type == "forward_checking":
                                    temps, iterations, result = solver.solve("forward_checking")
                                elif solver_type == "backjumping":
                                    temps, iterations, result = solver.solve("backjumping")
                                else:
                                    print("Invalid solver type!")
                                    return
                                
                                writer.writerow([num_variables, domains_size, density, durete, solver_type, temps, iterations, result])
                                print("Done : " + str(num_variables) + " " + str(domains_size) + " " + str(density) + " " + str(durete) + " " + solver_type + " " + str(temps) + " " + str(iterations) + " " + str(result) + (" " + str(solver.is_solution_valid()) if result is not None else ""))
                            print("--------------------")
            print("[+] Run " + str(n) + "/" + str(num_runs) + " done\n--------------------")

if __name__ == "__main__":
    launch_solver_n_times(10, "output.csv")