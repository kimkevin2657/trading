from datetime import datetime

from lshashing import LSHRandom
import numpy as np

from sklearn.neighbors import NearestNeighbors
import time
import json
import csv
import dcor

from featuregenerator import featuregen
from datagenerator import datagenerator
from clustering import clustering

fileslist = ["ADA_KRW-1h.json", "BCH_KRW-1h.json", "BTC_KRW-1h.json"]

datagen = datagenerator()

price_block = datagen.price_block_generator(fileslist)


data = price_block


fgen = featuregen()

data = fgen.returns(data, differencing=0, slide=2, relative="false", axis="row")
data = fgen.returns(data, differencing=1, slide=0, relative="false", axis="row")
data = fgen.returns(data, differencing=1, slide=1, relative="false", axis="row")
data = fgen.returns(data, differencing=5, slide=0, relative="false", axis="row")



cluster = clustering()

tempcluster = [data["data"][0], data["data"][1], data["data"][2], data["data"][6], data["data"][7], data["data"][8]]
tempclustertype = ["nonstationary", "nonstationary", "nonstationary", "stationary", "stationary", "stationary"]
tempclustercategory = ["price", "price", "price", "returns", "returns", "returns"]

cluster.cluster(data, strategystr="BCH")



"""
return02 = fgen.returns(data["data"], differencing=0, slide=2, relative="false", axis="row")
return10 = fgen.returns(data["data"], differencing=1, slide=0, relative="false", axis="row")
return11 = fgen.returns(data["data"], differencing=1, slide=1, relative="false", axis="row")
return50 = fgen.returns(data["data"], differencing=5, slide=0, relative="false", axis="row")

print(len(return01[0]))
print(len(return01[0]))
print(len(return01[0]))
print(len(return01[0]))
print(len(return01[0]))
"""
















