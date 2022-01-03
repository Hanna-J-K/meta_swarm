import Plots
import math


def eggholder(x, y):
    return -(y + 47) * math.sin(math.sqrt(abs(x / 2 + (y + 47)))) - x * math.sin(math.sqrt(abs(x - (y + 47))))


def three_hump_camel(x, y):
    return 2 * x**2 - 1.05 * x**4 + x**6 / 6 + x * y + y**2


if __name__ == '__main__':
    Plots.plot_experiment(
        eggholder, ((-512, 512), (-512, 512)), 'Eggholder')
    Plots.plot_experiment(
        three_hump_camel, ((-5, 5), (-5, 5)), 'Three hump camel')
