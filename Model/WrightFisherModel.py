import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

"""
This is a script for Wright-Fisher Model simulation written by Fengyu Tu
on June 10th, 2020.
The Wright-Fisher model describes the sampling of alleles in a population 
with no selection, no mutation, no migration, non-overlapping generation 
times and random mating. In each generation the entire population is 
replaced by the offspring from the previous generation. Parents are chosen 
via random sampling with replacement. 
"""


# Iinitial parameters settings
n_gen = 100  # number of generation
n_reps = 10  # number of replicates per simulation
pop_size = 100  # population size
ini_freq = 0.5  # initial allele frequency

figsize = 9, 6 # plot size
figure, ax = plt.subplots(figsize=figsize)

# Main loop:
l = 0
while l < n_reps:
    l += 1
    allele_frequency_list = [ini_freq]
    population = []
    allele_frequency = ini_freq
    i = 0
    while i < n_gen:
        i += 1
        population = np.random.choice(
            2, pop_size, p=[allele_frequency, 1 - allele_frequency])
        allele_frequency = Counter(population)[0] / pop_size
        allele_frequency_list.append(allele_frequency)
    if allele_frequency_list[-1] == 0:
        plt.plot(allele_frequency_list, marker='.',
            linestyle='-', color='steelblue')
    elif allele_frequency_list[-1] == 1:
        plt.plot(allele_frequency_list, marker='.',
            linestyle='-', color='palevioletred')
    else:
        plt.plot(allele_frequency_list, marker='.',
            linestyle='-', color='tan')

# Plot Setting (Available)
plt.grid(linestyle='--', color='lightgrey', alpha=0.8)
plt.axhline(y=ini_freq, linestyle='--', color='dimgrey')

font1 = {'family':'Cambria', 'size':14}
plt.xlabel('Generation(t)', font1)
plt.ylabel('${f_A}$(t)', font1)

plt.xlim((0, n_gen))
plt.ylim((0, 1))
plt.xticks(np.arange(0, n_gen+1, 10))
plt.yticks(np.arange(0, 1.1, 0.1))

plt.tick_params(labelsize=12)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Cambria') for label in labels]

plt.text(n_gen+1,0,'Lost:0',font1, color='steelblue')
plt.text(n_gen+1,1,'Fixed:1',font1, color='palevioletred')
plt.text((n_gen/2),1.03,'N='+str(pop_size),font1, color='black')


plt.savefig('Wright-Fisher Model.png', dpi=300)
plt.show()
