import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

''' A.1.1

'''

def fitness_1(x):
    return abs(x)

def fitness_2(x):
    return x**2

def fitness_3(x):
    return 2*(x**2)

def fitness_4(x):
    return x**2 + 20


individuals_x = [2, 3, 4]

fitness_functions = [
    ("fitness_1", fitness_1),
    ("fitness_2", fitness_2),
    ("fitness_3", fitness_3),
    ("fitness_4", fitness_4),
]

fitness_results = []
selection_probability_results = []

fig_table, axes_table = plt.subplots(2, 2, figsize=(10, 10))
axes_table = axes_table.flatten()
fig_pie, axes_pie = plt.subplots(2, 2, figsize=(10, 10))
axes_pie = axes_pie.flatten()

for idx, (key, func) in enumerate(fitness_functions):   
    fitness = []
    for individual in individuals_x:
        fitness.append(func(individual))

    selection_probabilities = fitness / np.sum(fitness)

    table = pd.DataFrame({
        "Individual": individuals_x,
        "Fitness": fitness,
        "Selection probability": selection_probabilities
    })

    plot_table = axes_table[idx].table(cellText = table.values,
            rowLabels = table.index,
            colLabels = table.columns,
            loc = "center"
            )
    plot_table.auto_set_font_size(False)
    plot_table.set_fontsize(8)
    plot_table.scale(1, 1.5) 
    axes_table[idx].set_title("Function: " + key)
    axes_table[idx].axis("off")

    axes_pie[idx].pie(selection_probabilities, labels=[f"x={x}" for x in individuals_x], autopct="%1.1f%%")
    axes_pie[idx].set_title("Function: " + key)

fig_pie.tight_layout()
fig_table.tight_layout()
plt.tight_layout()
plt.show()

''' A.1.2
When you multiplicatively increase fitness it does not alter the fitness scaling in comparison to eachother.
And with that it does not change the selection pressure.
Whereas when you additively scale the selection probabilities it does change the differences between the individuals and thus change the selection pressure.
'''