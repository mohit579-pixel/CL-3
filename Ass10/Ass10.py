import numpy as np

cities = np.array([[0, 0], [1, 2], [3, 1], [5, 3], [2, 4]])
num_cities = len(cities)

num_ants = 5
num_iterations = 100
alpha = 1  
beta = 2   
rho = 0.1 
Q = 1     

pheromone = np.ones((num_cities, num_cities))

def distance(city1, city2):
    return np.linalg.norm(city1 - city2)

best_tour = None
best_distance = np.inf

for iteration in range(num_iterations):
    ant_tours = []
    tour_distances = []
    
    for ant in range(num_ants):
        current_city = np.random.randint(num_cities)
        tour = [current_city]
        distance_traveled = 0
        
        while len(tour) < num_cities:
            probabilities = []
            for city in range(num_cities):
                if city not in tour:
                    pheromone_level = pheromone[current_city][city]
                    dist = distance(cities[current_city], cities[city])
                    prob = (pheromone_level ** alpha) * ((1 / dist) ** beta)
                    probabilities.append((city, prob))
            
            probabilities = np.array(probabilities)
            probabilities[:, 1] /= np.sum(probabilities[:, 1])
            
            next_city = np.random.choice(probabilities[:, 0], p=probabilities[:, 1])
            tour.append(int(next_city))
            distance_traveled += distance(cities[current_city], cities[int(next_city)])
            current_city = int(next_city)
        
        ant_tours.append(tour)
        tour_distances.append(distance_traveled)
    
    pheromone *= (1 - rho)
    for i in range(num_ants):
        tour = ant_tours[i]
        for j in range(num_cities - 1):
            pheromone[tour[j]][tour[j+1]] += (Q / tour_distances[i])
        pheromone[tour[-1]][tour[0]] += (Q / tour_distances[i])
    
    min_distance_idx = np.argmin(tour_distances)
    if tour_distances[min_distance_idx] < best_distance:
        best_tour = ant_tours[min_distance_idx]
        best_distance = tour_distances[min_distance_idx]

print("Best tour:", best_tour)
print("Best distance:", best_distance)
