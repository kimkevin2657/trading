from strategy import strategy
import time

class clustering:
    def __init__(self):
        self.temp = 1
        self.strategy = strategy()


    
    def subsections(self, cluster, clustertype, clustercategory, data, strategy=None):

        targetvec = []
        for i in range(0, len(cluster)):
            targetvec.append(cluster[i][len(cluster[i])-1])


        stdval = []
        
        for i in range(0, len(cluster)):

            if clustercategory[i] == "price":

                diststd = 0.0
                diststdcount = 0.0

                for t in range(0, len(cluster[i])):
                    if cluster[i][t] == -99999:
                        continue
                    else:
                        diststd += abs(cluster[i][t] - targetvec[i])
                        diststdcount += 1.0
                diststd *= 1.0/diststdcount

                stdval.append(diststd)

            if clustercategory[i] == "returns":
                posval = 0.0
                negval = 0.0
                posvaldenom = 0.0
                negvaldenom = 0.0
                for t in range(0, len(cluster[i])):
                    if cluster[i][t] == -99999:
                        continue
                    else:
                        if cluster[i][t] > 0.0:
                            posval += cluster[i][t]
                            posvaldenom += 1.0
                        else:
                            negval += abs(cluster[i][t])
                            negvaldenom += 1.0

                if posvaldenom != 0.0:
                    posval *= 1.0/posvaldenom
                if negvaldenom != 0.0:
                    negval *= 1.0/negvaldenom

                stdval.append([posval, negval])
            
            if clustertype[i] == "boolean":
                stdval.append("boolean")


        subsections = []

        subsectionsY = []

        totalcount = 0

        for t in range(0, len(cluster[0])-1):
        #for t in range(len(cluster[0])-100, len(cluster[0])):

            currvec = []
            breakbool = False
            for k in range(0, len(cluster)):
                currvec.append(cluster[k][t])
                if cluster[k][t] == -99999:
                    breakbool = True
                    break
            if breakbool:
                continue

            continuousscore = 0.0
            continuousscoredenom = 0.0
            for k in range(0, len(clustertype)):

                if clustercategory[k] == "price":
                    if abs(currvec[k] - targetvec[k]) > stdval[k]:
                        continuousscore += 0.0
                    else:
                        continuousscore += 1.0 - abs(currvec[k] - targetvec[k])/stdval[k]
                    continuousscoredenom += 1.0
                
                if clustercategory[k] == "returns":
                    if (currvec[k] <= 0.0 and targetvec[k] > 0.0) or (currvec[k] > 0.0 and targetvec[k] <= 0.0):
                        continuousscore += 0.0
                    else:
                        if currvec[k] > 0.0:
                            continuousscore += 1.0 - abs(currvec[k] - targetvec[k])/stdval[k][0]
                        if currvec[k] <= 0.0:
                            continuousscore += 1.0 - abs(currvec[k] - targetvec[k])/stdval[k][1]
                    continuousscoredenom += 1.0

            # this section is for boolean type
            # this section is for boolean type
            # this section is for boolean type
            """
            currvecbool = []
            targetvecbool = []
            for k in range(0, len(clustertype)):
                if clustertype[k] == "boolean":
                    currvecbool.append(currvec[k])
                    targetvecbool.append(targetvec[k])
            correctcount = 0.0
            for k in range(0, len(currvecbool)):
                if currvecbool == targetvecbool:
                    correctcount += 1.0

            correctcountscore = correctcount/float(len(currvecbool))
            
            for k in range(0, len(currvecbool)):
                continuousscore += correctcountscore
                continuousscoredenom += 1.0
            """

            """
            if t > len(cluster[0])-100:
                print(" ============    ", t, "    ==================  ")
                print( continuousscore, "     ", continuousscoredenom, "     ",continuousscore/continuousscoredenom)
                print(" stdval   ", stdval)
                print(currvec)
                print(targetvec)
            """


        #print( " =========== totalcount   ", totalcount)

            continuousscore *= 1.0/continuousscoredenom

            ###
            ### threshold absolutely above 0.75 seems okay. 
            ###

            if continuousscore > 0.75:

                subsections.append(currvec)

                if strategy == "ADA":
                    dataidx = 0
                    for l in range(0, len(data["name"])):
                        if data["name"] == "ADA":
                            dataidx = l

                    subsectionsY.append(data["returns"][dataidx][t])

                if strategy == "BCH":
                    dataidx = 0
                    for l in range(0, len(data["name"])):
                        if data["name"] == "BCH":
                            dataidx = l

                    subsectionsY.append(data["returns"][dataidx][t])

                if strategy == "BTC":
                    dataidx = 0
                    for l in range(0, len(data["name"])):
                        if data["name"] == "BTC":
                            dataidx = l

                    subsectionsY.append(data["returns"][dataidx][t])


                """
                totalcount += 1.0
                print()
                print(" ===========   similar ===========   ",t, "   ", continuousscore)
                print(currvec)
                print(targetvec)
                print(" ===========   similar ===========   ")
                print()
                """

        return subsections, subsectionsY


            

    def cluster(self, data, strategystr=None):


        pps = []
        for i in range(0, len(data["data"])):
            templist = []
            for j in range(0, len(data["data"])):
                templist.append(0.0)
            pps.append(templist)

        columns = [i for i in range(0, len(data["data"]))]

        print(columns, "   ", len(columns))

        maxval = -99999
        maxi = 0
        maxj = 0

        currtime2 = time.time()

        for i in range(0, len(columns)):
            for j in range(i, len(columns)):

                print(" ========    ",i, "   ", j , "    ==========  ")
                
                subsections = []
                subsectionsY = []

                if i != j:
                    cluster = []
                    clustertype = []
                    clustercategory = []
                    if isinstance(columns[i], list):
                        for k in range(0, len(columns[i])):
                            cluster.append(data["data"][columns[i]][k])
                            clustertype.append(data["type"][columns[i]][k])
                            clustercategory.append(data["category"][columns[i]][k])
                    else:
                        cluster.append(data["data"][columns[i]])
                        clustertype.append(data["type"][columns[i]])
                        clustercategory.append(data["category"][columns[i]])

                    if isinstance(columns[j], list):
                        for k in range(0, len(columns[j])):
                            cluster.append(data["data"][columns[j]][k])
                            clustertype.append(data["type"][columns[j]][k])
                            clustercategory.append(data["category"][columns[j]][k])
                    else:
                        cluster.append(data["data"][columns[j]])
                        clustertype.append(data["type"][columns[j]])
                        clustercategory.append(data["category"][columns[j]])

                    temp = self.subsections(cluster, clustertype, clustercategory, data, strategy=strategystr)

                if i == j:
                    cluster = []
                    clustertype = []
                    clustercategory = []
                    if isinstance(columns[i], list):
                        for k in range(0, len(columns[i])):
                            cluster.append(data["data"][columns[i]][k])
                            clustertype.append(data["type"][columns[i]][k])
                            clustercategory.append(data["category"][columns[i]][k])
                    else:
                        cluster.append(data["data"][columns[i]])
                        clustertype.append(data["type"][columns[i]])
                        clustercategory.append(data["category"][columns[i]])

                    temp = self.subsections(cluster, clustertype, clustercategory, data, strategy=strategystr)


                subsections = temp[0]
                subsectionsY = temp[1]


                currtime = time.time()
                currscore = self.strategy.cv_accuracy(subsections, subsectionsY)
                
                if currscore > maxval:
                    maxi = i
                    maxj = j

                    

                
                print(currscore[0], "   ", currscore[1], "   ", time.time() - currtime)


                #   most statisticians would say minimum 100 sample size required
                #   most statisticians would say minimum 100 sample size required
                #   most statisticians would say minimum 100 sample size required
                #if len(subsections) > 50:

        print(" ========= total time  ", currtime2 - time.time())



                


