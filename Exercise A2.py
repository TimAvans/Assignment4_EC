import random
import matplotlib.pyplot as plt
import numpy as np

''' A.2.1 - A.2.2
Optimizing counting ones problem (maximize number of ones in 100bits)
'''

def gen_bits(length = 100):
    return [random.randint(0,1) for _ in range(length)]

def count_ones(bits):
    return sum(bits)

def mutate(bits, mutate_rate):
    mutated_bits = []
    for bit in bits:
        if random.random() < mutate_rate:
            mutated_bits.append(1-bit)
        else:
            mutated_bits.append(bit)    
    return mutated_bits

def GA(bits_length, generations, mutate_rate, elitist = True):
    fitness_hist = []
    start_bits = gen_bits(bits_length)

    for generation in range(generations):
        fitness = count_ones(start_bits)
        mutated_bits = mutate(start_bits, mutate_rate)
        mutation_fitness = count_ones(mutated_bits)

        if elitist:
            if mutation_fitness > fitness:
                start_bits = mutated_bits
                fitness_hist.append(mutation_fitness)
            else:
                fitness_hist.append(fitness)
        else:
            start_bits = mutated_bits
            fitness_hist.append(mutation_fitness)

    return start_bits, fitness_hist

bits_length = 100
generations = 1500
mutate_rate = 1/bits_length

bits_elitist, hist_elitist = GA(bits_length, generations, mutate_rate)
bits, hist = GA(bits_length, generations, mutate_rate, False)

fig, axes = plt.subplots(1, 2, figsize=(20, 10))
axes = axes.flatten()
fig.suptitle("1 run")
axes[0].set_title("Elitist")
axes[0].plot(hist_elitist)
axes[0].set_xlabel("Gen")
axes[0].set_ylabel("Best fit")
axes[1].plot(hist)
axes[1].set_xlabel("Gen")
axes[1].set_ylabel("Best fit")
axes[1].set_title("No-Elitist")



''' A.2.3
Purely based on the results of one run you cannot conclusively state anything
due to the stochastic nature of the algorithm. To make a fair comparison you would need
to do multiple independent runs and compare those.
'''

''' A.2.4
An experiment with multiple runs.
Then plot averages so we know which algorithm performs better on average (elitist ofc)
'''

def run(iterations, elitist, bits_length, generations):
    histories = []
    for i in range(iterations):
        bits_length = bits_length
        generations = generations
        mutate_rate = 1/bits_length

        _, hist = GA(bits_length, generations, mutate_rate, elitist)
        histories.append(hist)
    return histories

total_runs = 50
bits_length = 100
generations = 1500

hist_elitist = run(total_runs, True, bits_length, generations)
hist_non_elitist = run(total_runs, False, bits_length, generations)

fig_avg, axes_avg = plt.subplots(1, 2, figsize=(20, 10))
axes_avg = axes_avg.flatten()

hist_mean_elite = np.mean(np.array(hist_elitist), axis=0)
hist_mean = np.mean(np.array(hist_non_elitist), axis=0)

fig_avg.suptitle(str(total_runs) + " runs experiment")
axes_avg[0].set_title("Elitist")
axes_avg[0].plot(np.arange(generations), hist_mean_elite, label='Mean best fitness')
axes_avg[1].set_title("No-elitist")
axes_avg[1].plot(np.arange(generations), hist_mean, label='Mean best fitness')


plt.tight_layout()
plt.show()