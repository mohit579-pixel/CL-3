import numpy as np

def objective_function(x):
    return np.sum(x**2)

num_antibodies = 20
num_generations = 100
clone_factor = 5
mutation_rate = 0.1
dimension = 5

antibodies = np.random.uniform(-10, 10, (num_antibodies, dimension))

for generation in range(num_generations):
    fitness = np.array([objective_function(antibody) for antibody in antibodies])
    
    top_antibodies = antibodies[np.argsort(fitness)[:int(num_antibodies/2)]]
    
    new_antibodies = []
    for antibody in top_antibodies:
        clones = [antibody + mutation_rate * np.random.randn(dimension) for _ in range(clone_factor)]
        new_antibodies.extend(clones)
    
    new_fitness = np.array([objective_function(antibody) for antibody in new_antibodies])
    
    antibodies = np.array(new_antibodies)[np.argsort(new_fitness)[:num_antibodies]]

best_antibody = antibodies[np.argmin([objective_function(antibody) for antibody in antibodies])]
print("Best solution found:", best_antibody)
print("Objective function value:", objective_function(best_antibody))
