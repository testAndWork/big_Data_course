from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
from random import random, randint
import statistics as st

ages = [23, 45, 67, 34, 56, 12, 34, 45]

print(st.mean(ages))
print('La moda es:', st.mode(ages))
print('La desviación estandar es: ', round(st.stdev(ages), 2))


print(random())
print(randint(1, 9))

"""x = np.arange(0, 10)
y = x**2

plt.plot(x, y)
plt.show()

# Crear scatterplot
x = np.arange(0, 20)
y = np.random.rand(20) 
plt.scatter(x, y)"""


X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

Kmeans = KMeans(n_clusters=3)
Kmeans.fit(X)
print(Kmeans.labels_)
