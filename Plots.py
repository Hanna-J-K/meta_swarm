import numpy as np
import Particle
import Swarm
import matplotlib.pyplot as plt


def plot_comparison(data, title, labels, filename):
    x_1, y_1, z_1 = data[0]
    x_2, y_2, z_2 = data[1]
    x_3, y_3, z_3 = data[2]
    plt.figure()
    plt.title(title)
    plt.plot(np.arange(Swarm.ITERATIONS), z_1,
             color='palevioletred', label=labels[0])
    print(f'x={x_1[-1]}, y={y_1[-1]}, z={z_1[-1]}')

    plt.plot(np.arange(Swarm.ITERATIONS), z_2,
             color='olive', label=labels[1])
    print(f'x={x_2[-1]}, y={y_2[-1]}, z={z_2[-1]}')

    plt.plot(np.arange(Swarm.ITERATIONS), z_3,
             color='black', label=labels[2])
    print(f'x={x_3[-1]}, y={y_3[-1]}, z={z_3[-1]}')
    plt.xlabel('Iterations')
    plt.ylabel('Adaptation value')
    plt.legend()
    plt.savefig(filename)


def plot_inertia(bounds, function_name):
    print('Inertia')
    data = []

    Particle.INERTIA_WEIGHT = 0.1
    swarm_inertia_1 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_inertia_1))

    Particle.INERTIA_WEIGHT = 0.5
    swarm_inertia_2 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_inertia_2))

    Particle.INERTIA_WEIGHT = 0.9
    swarm_inertia_3 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_inertia_3))

    Particle.INERTIA_WEIGHT = 0.5
    title = f'{function_name} (Inertia)'
    labels = ['Inertia = 0.1', 'Inertia = 0.5', 'Inertia = 0.9']
    filename = f'{function_name}_inertia.png'
    plot_comparison(data, title, labels, filename)


def plot_cognitive(bounds, function_name):
    print('Cognitive')
    data = []

    Particle.COGNITIVE_CONSTANT = 0
    swarm_cognitive_1 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_cognitive_1))

    Particle.COGNITIVE_CONSTANT = 1
    swarm_cognitive_2 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_cognitive_2))

    Particle.COGNITIVE_CONSTANT = 2
    swarm_cognitive_3 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_cognitive_3))

    Particle.COGNITIVE_CONSTANT = 1
    title = f'{function_name} (Cognitive)'
    labels = ['Cognitive = 0', 'Cognitive = 1', 'Cognitive = 2']
    filename = f'{function_name}_cognitive.png'
    plot_comparison(data, title, labels, filename)


def plot_social(bounds, function_name):
    print('Social')
    data = []

    Particle.SOCIAL_CONSTANT = 0
    swarm_social_1 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_social_1))

    Particle.SOCIAL_CONSTANT = 1
    swarm_social_2 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_social_2))

    Particle.SOCIAL_CONSTANT = 2
    swarm_social_3 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_social_3))

    Particle.SOCIAL_CONSTANT = 2
    title = f'{function_name} (Social)'
    labels = ['Social = 0', 'Social = 1', 'Social = 2']
    filename = f'{function_name}_social.png'
    plot_comparison(data, title, labels, filename)


def plot_population(bounds, function_name):
    print('Population')
    data = []

    Swarm.POPULATION = 50
    swarm_population_1 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_population_1))

    Swarm.POPULATION = 75
    swarm_population_2 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_population_2))

    Swarm.POPULATION = 100
    swarm_population_3 = Swarm.generate_swarm(*bounds)
    data.append(Swarm.find_minimum(swarm_population_3))

    Swarm.POPULATION = 90
    title = f'{function_name} (Population)'
    labels = ['Population = 50', 'Population = 75', 'Population = 100']
    filename = f'{function_name}_population.png'
    plot_comparison(data, title, labels, filename)


def plot_experiment(function, bounds, function_name):
    print(function_name)
    Particle.FUNCTION = function

    plot_inertia(bounds, function_name)
    plot_cognitive(bounds, function_name)
    plot_social(bounds, function_name)
    plot_population(bounds, function_name)
