from datetime import datetime

import numpy as np

import time
import json
import csv

#
#   needs to include a method for generating price block for different frequency, different rebalancing hour
#

class datagenerator:
    def __init__(self):
        self.temp = 1

    def price_block_generator(self, files, type="json", relative="false"):

        if type == "json":


            templist = []
            for file in files:
                f = open(file)
                data = json.load(f)
                temp = []
                for i in range(0, len(data)):
                    temp.append(data[i][4])
                templist.append(temp)

            templength = [len(templist[i]) for i in range(0, len(templist))]
            minlen = min(templength)
            minlen -= 1

            templist2 = []
            for i in range(0, len(templist)):
                temp = []
                for t in range(len(templist[i])-1, 0, -1):
                    temp.append(templist[i][t])
                    if len(temp) == minlen:
                        break
                temp = temp[::-1]
                templist2.append(temp)

            returns = []
            for i in range(0, len(templist2)):
                temp = []
                for t in range(0, len(templist2[i])-1):
                    if relative == "false":
                        temp.append(float(templist2[i][t+1])/float(templist2[i][t])-1.0)
                    if relative == "true":
                        temp.append(float(templist2[i][t+1])/float(templist2[i][t]))
                temp.append(0.0)
                returns.append(temp)

            data = dict()
            data["data"] = templist2

            data["returns"] = returns

            templist2 = ["ADA", "BCH", "BTC"]
            data["name"] = templist2

            type = ["nonstationary", "nonstationary", "nonstationary"]
            data["type"] = type

            category = ["price", "price", "price"]
            data["category"] = category

            return data



