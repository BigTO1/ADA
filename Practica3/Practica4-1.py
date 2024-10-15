import math
import time
import random

# Genera puntos aleatorios
def generate_random_points(num_points, coord_range=(-100, 100)):
    return [[random.randint(*coord_range), random.randint(*coord_range)] for _ in range(num_points)]

# Encuentra el par de puntos más cercanos y mide el tiempo de ejecución
def closest_pair_brute_force(points):
    min_distance = float('inf')
    closest_pair = (None, None)
    start_time = time.time()
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    
    end_time = time.time()
    execution_time = end_time - start_time
    return closest_pair, execution_time

# Ejemplo de uso con puntos aleatorios
num_points = 100000  # Número de puntos a generar
points = generate_random_points(num_points)
# Encuentra el par de puntos más cercanos y el tiempo de ejecución
closest_pair, execution_time = closest_pair_brute_force(points)

print("El par de puntos más cercano es:", closest_pair)
print(f"Tiempo de ejecución: para {num_points} puntos generados es {execution_time} segundos")
