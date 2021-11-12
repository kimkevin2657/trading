from datetime import datetime

from lshashing import LSHRandom
import numpy as np

from sklearn.neighbors import NearestNeighbors

import json
import dcor

temp = [1,2,3,4,5]
temp2 = [5,4,3,2,1]

temp = np.asarray(temp)
temp2 = np.asarray(temp2)

result = dcor.distance_correlation(temp, temp2, method="MERGESORT")
print(result)

temp = [[1,1],[5,2],[2,3]]

temp2 = sorted(temp)
print(temp2[::-1])


"""
sample_data = np.random.randint(size = (10000, 25), low = 3000, high = 8000)
point = np.random.randint(size = (1,25), low = 3000, high = 8000)


lshashing = LSHRandom(sample_data, hash_len=25, num_tables=10, parallel = True)
print(sample_data[:20])
print()
print(point)
print()

print(lshashing.knn_search(sample_data, point[0], k=100, buckets=100, radius=2))
print()
print("================================== ")

X = np.append(sample_data, point, axis=0)
print(X[:20])
print()
nbrs = NearestNeighbors(n_neighbors=100, algorithm="ball_tree").fit(X)
distances, indices = nbrs.kneighbors(X)
print(indices[-1])
print()
print(distances[-1])


"""


