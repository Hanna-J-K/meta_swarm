import numpy as np
import math

INERTIA_WEIGHT = 0.5
COGNITIVE_CONSTANT = 1
SOCIAL_CONSTANT = 2


def FUNCTION(x, y):
    return -(y + 47) * math.sin(math.sqrt(abs(x / 2 + (y + 47)))) - x * math.sin(math.sqrt(abs(x - (y + 47))))


global_best_x = 0
global_best_y = 0

rng = np.random.default_rng()


class Particle():
    def __init__(self, bounds_x: tuple, bounds_y):
        self.velocity_x = []
        self.velocity_y = []
        self.x = []
        self.y = []
        self.adaptation = []
        self.best_x = 0
        self.best_y = 0
        self.best_adaptation = np.inf
        self.bounds_x = bounds_x
        self.bounds_y = bounds_y

        self.velocity_x.append(0)
        self.velocity_y.append(0)
        self.x.append(rng.uniform(bounds_x[0], bounds_x[1]))
        self.y.append(rng.uniform(bounds_y[0], bounds_y[1]))

    def calculate_inertia(self):
        inertia_x = INERTIA_WEIGHT * self.velocity_x[-1]
        inertia_y = INERTIA_WEIGHT * self.velocity_y[-1]
        return inertia_x, inertia_y

    def calculate_cognitive_components(self):
        cognitive_x = (COGNITIVE_CONSTANT * rng.random()) * \
            (self.best_x - self.x[-1])
        cognitive_y = (COGNITIVE_CONSTANT * rng.random()) * \
            (self.best_y - self.y[-1])
        return cognitive_x, cognitive_y

    def calculate_social_components(self):
        social_x = (SOCIAL_CONSTANT * rng.random()) * \
            (global_best_x - self.x[-1])
        social_y = (SOCIAL_CONSTANT * rng.random()) * \
            (global_best_y - self.y[-1])
        return social_x, social_y

    def calculate_new_velocity(self):
        inertia_x, inertia_y = self.calculate_inertia()
        cognitive_x, cognitive_y = self.calculate_cognitive_components()
        social_x, social_y = self.calculate_social_components()
        self.velocity_x.append(inertia_x + cognitive_x + social_x)
        self.velocity_y.append(inertia_y + cognitive_y + social_y)

    def move_to_new_position(self):
        self.x[-1] += self.velocity_x[-1]
        self.y[-1] += self.velocity_y[-1]

        if self.x[-1] < self.bounds_x[0]:
            self.x[-1] = self.bounds_x[0]
        if self.x[-1] > self.bounds_x[1]:
            self.x[-1] = self.bounds_x[1]

        if self.y[-1] < self.bounds_y[0]:
            self.y[-1] = self.bounds_y[0]
        if self.y[-1] > self.bounds_y[1]:
            self.y[-1] = self.bounds_y[1]

    def find_best_adaptation(self):
        self.adaptation.append(FUNCTION(self.x[-1], self.y[-1]))
        if self.adaptation[-1] < self.best_adaptation:
            self.best_x = self.x[-1]
            self.best_y = self.y[-1]
            self.best_adaptation = self.adaptation[-1]
