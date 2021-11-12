


class featuregen:
    def __init__(self):
        self.temp = 1


    # price_block = price only block, relative = price relative or not, axis = whether features are rows or columns
    def returns(self, inputdata, differencing=1, slide=0, relative="true", axis="row"):
        import itertools 

        data = inputdata

        price = []
        name = []
        for i in range(0, len(data["category"])):
            if data["category"][i] == "price":
                price.append(data["data"][i])
                name.append(data["name"][i])


        # transposes if row != features and column != time
        if axis == "column":
            price = list(map(list, itertools.zip_longest(*price, fillvalue=None)))

        returns_block = []
        for a in range(0, len(price)):
            temp = []
            for t in range(0, len(price[a])):
                if t < differencing + slide:
                    temp.append(-99999)
                else:
                    if relative == "true":
                        if differencing > 0:
                            temp.append(float(price[a][t-slide])/float(price[a][t-slide-differencing]))
                        if differencing == 0:
                            temp.append(float(price[a][t-slide]))
                    if relative == "false":
                        if differencing > 0:
                            temp.append(float(price[a][t-slide])/float(price[a][t-slide-differencing])-1.0)
                        if differencing == 0:
                            temp.append(float(price[a][t-slide]))
            returns_block.append(temp)

        returnsblock = []
        if axis == "column":
            returnsblock = list(map(list, itertools.zip_longest(*returns_block, fillvalue=None)))
        
        if axis == "row":
            returnsblock = returns_block

        for i in range(0, len(returnsblock)):
            data["data"].append(returnsblock[i])
            if differencing > 0:
                data["type"].append("stationary")
            if differencing == 0:
                data["type"].append("nonstationary")
            data["category"].append("returns")
            data["name"].append(name[i]+"returns"+str(differencing)+str(slide))

        return data
        



    

