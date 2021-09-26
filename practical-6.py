import numpy as np
from Orange.data import Table, Domain
from Orange.preprocess import Discretize, Continuize, Normalize, Randomize

# Descretization
disc = Discretize()
data_set = Table("iris.tab")

disc_data_set = con(data_set)

print(con_data_set)


con_in_data = Table("bmw.csv")


# Continuization
con = Continuize()

con_in_data = con(in_data)

print(con_in_data)


# Normalization
nomalizer = Normalize()

normalized_in_data = nomalizer(in_data)

print(normalized_in_data)


# Randomization
randomizer = Randomize()

randomized_in_data = randomizer(in_data)

print(randomized_in_data)