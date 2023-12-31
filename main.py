import numpy as np
import matplotlib.pyplot as plt

zones = [
    {"x": -150, "y": 150, "sigma_x": 30, "sigma_y": 10, "color": "red"},
    {"x": 0, "y": 0, "sigma_x": 30, "sigma_y": 50, "color": "blue"},
    {"x": 200, "y": -150, "sigma_x": 50, "sigma_y": 20, "color": "yellow"}
]

np.random.seed(None)

prag = 0.01


def genereaza_puncte(nr_de_puncte):
    puncte = []

    for i in range(nr_de_puncte):
        zona = np.random.choice(zones)

        # genereaza punct
        valori_X = np.random.normal(zona["x"], zona["sigma_x"], 1)
        valori_Y = np.random.normal(zona["y"], zona["sigma_y"], 1)

        puncte.append((valori_X[0], valori_Y[0], zona["color"]))
        i = i + 1

        # accepta puncte noise
        if np.random.rand() < prag:
            noise_X = np.random.uniform(-300, 300)
            noise_Y = np.random.uniform(-300, 300)
            puncte.append((noise_X, noise_Y, zona["color"]))
            i = i + 1

    return puncte


def salvareFisier(points, filename):
    with open(filename, "w") as file:
        for point in points:
            file.write(f"{point[0]} {point[1]} {point[2]}\n")


def genereazaPlot(filename):
    data = np.loadtxt(filename, dtype={'names': ('x', 'y', 'color'), 'formats': ('f8', 'f8', 'U10')})
    x = data['x']
    y = data['y']
    colors = data['color']

    for zona in zones:
        plt.scatter(x[colors == zona["color"]], y[colors == zona["color"]], color=zona["color"], s=1, marker=',')


points = genereaza_puncte(10000)
salvareFisier(points, "points.txt")
genereazaPlot("points.txt")

plt.axvline(0, c='black', ls='-')
plt.axhline(0, c='black', ls='-')
plt.xlim([-300, 300])
plt.ylim([-300, 300])
plt.show()
