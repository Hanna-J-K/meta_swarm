import numpy as np
from Particle import Particle
import matplotlib.pyplot as plt

POPULATION = 90
ITERATIONS = 100


def generate_swarm(bounds_x, bounds_y):
    return [Particle(bounds_x, bounds_y) for _ in range(POPULATION)]


def find_minimum(swarm):
    global_best_adaptation = np.inf
    best_positions_x = []
    best_positions_y = []
    best_adaptations = []
    for _ in range(ITERATIONS):
        for particle in swarm:
            particle.find_best_adaptation()
            particle.calculate_new_velocity()
            particle.move_to_new_position()

            if particle.best_adaptation < global_best_adaptation:
                best_positions_x.append(particle.best_x)
                best_positions_y.append(particle.best_y)
                global_best_adaptation = particle.best_adaptation
        best_adaptations.append(global_best_adaptation)

    return best_positions_x, best_positions_y, best_adaptations


if __name__ == '__main__':
    swarm = generate_swarm((-512, 512), (-512, 512))
    best_positions_x, best_positions_y, best_adaptations = find_minimum(swarm)
    print(best_positions_x)
    print(best_positions_y)
    plt.plot(np.arange(ITERATIONS), best_adaptations)
    plt.show()
