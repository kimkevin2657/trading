from datetime import datetime

from lshashing import LSHRandom
import numpy as np

from sklearn.neighbors import NearestNeighbors
import time
import json
import csv
import dcor
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

ADA = []
f = open("ADA_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    ADA.append(data[i][4])

AXS = []
f = open("AXS_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    AXS.append(data[i][4])

BCH = []
f = open("BCH_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    BCH.append(data[i][4])

BTC = []
f = open("BTC_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    BTC.append(data[i][4])

DOGE = []
f = open("DOGE_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    DOGE.append(data[i][4])

DOT = []
f = open("DOT_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    DOT.append(data[i][4])

ETH = []
f = open("ETH_KRW-1h.json")
data = json.load(f)
for i in range(0, len(data)):
    ETH.append(data[i][4])

#minlen = min(len(ADA), len(AXS), len(BCH), len(BTC), len(DOGE), len(DOT), len(ETH))
minlen = min(len(ADA), len(BCH), len(BTC), len(ETH))
minlen -= 1

print(minlen)

print(len(ADA), '  ', len(AXS),'   ', len(BCH), '  ', len(BTC), '  ', len(DOGE), '  ', len(DOT), '  ', len(ETH))

ADA2 = []
for t in range(len(ADA)-1, 0, -1):
    ADA2.append(ADA[t])
    if len(ADA2) == minlen:
        break


"""
AXS2 = []
for t in range(len(AXS)-1, 0, -1):
    AXS2.append(AXS[t])
    if len(AXS2) == minlen:
        break
"""

BCH2 = []
for t in range(len(BCH)-1, 0, -1):
    BCH2.append(BCH[t])
    if len(BCH2) == minlen:
        break

BTC2 = []
for t in range(len(BTC)-1, 0, -1):
    BTC2.append(BTC[t])
    if len(BTC2) == minlen:
        break

"""
DOGE2 = []
for t in range(len(DOGE)-1, 0, -1):
    DOGE2.append(DOGE[t])
    if len(DOGE2) == minlen:
        break

DOT2 = []
for t in range(len(DOT)-1, 0, -1):
    DOT2.append(DOT[t])
    if len(DOT2) == minlen:
        break
"""


ETH2 = []
for t in range(len(ETH)-1, 0, -1):
    ETH2.append(ETH[t])
    if len(ETH2) == minlen:
        break


data = [ADA2[::-1], BCH2[::-1], BTC2[::-1], ETH2[::-1]]

data = np.asarray(data)

print("  data  shape   ", data.shape)


"""
data2 = []
for i in range(0, len(data)):
    temp = []
    for t in range(1, len(data[i])):
        temp.append(data[i][t]/data[i][t-1])
    data2.append(temp)

data = np.asarray(data2)
"""


print(" data shape   ", data.shape)


def flatten(data):
    temp = []
    for i in range(0, len(data)):
        temp.append(data[i].flatten())
    return np.asarray(temp)

def flatteninput(data):
    temp = data.flatten()
    return temp



window_size = 10

currstate = data[:,len(data[0])-window_size:len(data[0])]

print("   currstate shape   ", currstate.shape)


nextreturns_subsections = []
potential_subsections = []
for t in range(window_size, len(data[0])):
    potential_subsections.append(data[:,t-window_size:t])
    
    nextreturns_subsections.append(data[:,t]/data[:,t-1])

potential_subsections = np.asarray(potential_subsections)
nextreturns_subsections = np.asarray(nextreturns_subsections)

print("  potential subsections shape  ", potential_subsections.shape)

print("   next returns subsections    ", nextreturns_subsections.shape)



flattened_subsections = flatten(potential_subsections)

print("   subsections flattened shape   ", flattened_subsections.shape)

flattend_currstate = flatteninput(currstate)

print("   currstate flattened shape   ", flattend_currstate.shape)



"""
currtime = time.time()
lshashing = LSHRandom(flattened_subsections, hash_len=20, num_tables=5, parallel=True)

result = lshashing.knn_search(flattened_subsections, flattend_currstate, k=100, buckets=10, radius=2)

print(result)
print(time.time() - currtime)
"""


temp = [1,2,3,4,5]
temp2 = [5,4,3,2,1]

temp = np.asarray(temp)
temp2 = np.asarray(temp2)

result = dcor.distance_correlation(temp, temp2, method="MERGESORT")
print(result)

currtime = time.time()
rankings = []
for i in range(0, len(flattened_subsections)):
    result = dcor.distance_correlation(flattened_subsections[i], flattend_currstate, method="MERGESORT")
    rankings.append([result, i])


rankings = sorted(rankings)
rankings = rankings[::-1][:10]

for i in range(0, len(rankings)):
    print(i, "   ", rankings[i][0], "  ", rankings[i][1])



subsections = []
nextreturns = []
for i in range(0, len(rankings)):
    if rankings[i][0] > 0.7:
        subsections.append(potential_subsections[rankings[i][1]])
        nextreturns.append(nextreturns_subsections[rankings[i][1]])




"""
currtime = time.time()
X = np.append(flattened_subsections, np.asarray([flattend_currstate]), axis=0)

nbrs = NearestNeighbors(n_neighbors=100, algorithm="ball_tree").fit(X)
distances, indices = nbrs.kneighbors(X)
print(indices[-1])
print()
print(distances[-1])
print(time.time() - currtime)

idx = indices[-1]
subsections = []
nextreturns = []
for i in range(1, len(idx)):
    subsections.append(potential_subsections[idx[i]])
    nextreturns.append(nextreturns_subsections[idx[i]])
"""






f = open("temp2.csv", "w", newline="")
wr = csv.writer(f)

for i in range(0, len(subsections)):
    startfund = []
    startfund2 = []
    for q in range(0, len(currstate)):
        startfund.append(1.0)
        startfund2.append(1.0)
    for t in range(0, len(subsections[i][0])):
        currvec = []
        for a in range(0, len(subsections[i])):
            """
            currvec.append(startfund[a]*subsections[i][a][t])
            currvec.append(startfund2[a]*currstate[a][t])
            startfund[a] *= subsections[i][a][t]
            startfund2[a] *= currstate[a][t]
            """
            currvec.append(subsections[i][a][t])
            currvec.append(currstate[a][t])

        
        currvec.append(i)
        for a in range(0, len(nextreturns[i])):
            currvec.append(nextreturns[i][a])
        wr.writerow(currvec)

f.close()


