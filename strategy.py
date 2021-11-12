from catboost import CatBoostRegressor, Pool
import random

# Initialize data


class strategy:
    def __init__(self, learning_rate=0.5, depth=5):
        self.learning_rate = learning_rate
        self.depth = depth
        self.model = CatBoostRegressor(iterations=1000,
                                        learning_rate=self.learning_rate,
                                        depth=self.depth,
                                        silent=True
                                        )

    # inputdata = [[input]]
    def predict(self, inputdata):
        preds = self.model.predict(inputdata)
        return preds

    def train(self, x_train, y_train, x_test, y_test):
        eval_pool = Pool(x_test, y_test)
        self.model.fit(x_train, y_train, eval_set=eval_pool, early_stopping_rounds=10)

    def accuracy(self, x, y, model):
        acc_count = 0.0
        acc_count_total = 0.0

        AMSE = 0.0

        for i in range(0, len(x)):

            pred = model.predict(x[i])
            sumval = abs(pred - y[i])
            AMSE += sumval
            if y[i] > 0.0 and pred > 0.0:
                acc_count += 1.0
            if y[i] < 0.0 and pred < 0.0:
                acc_count += 1.0
            if y[i] == 0.0 and pred == 0.0:
                acc_count += 1.0
            acc_count_total += 1.0


            """
            sumval = 0.0
            for k in range(0, len(pred)):
                sumval += abs(pred[k] - y[i][k])
            AMSE += sumval
            if y[i] > 0.0 and pred[0] > 0.0:
                acc_count += 1
            if y[i] < 0.0 and pred[0] < 0.0:
                acc_count += 1
            acc_count_total += 1
            """


        return AMSE, acc_count/acc_count_total



    # X = [[sample1], [sample2]]   Y = [label1, label2]
    def cv_accuracy(self, X, Y):

        
        templist = []
        for i in range(0, len(X)):
            templist.append([X[i], Y[i]])

        global_AMSE = 0.0
        global_AMSE_count = 0.0
        global_acc = 0.0
        global_acc_count = 0.0

        for idx in range(0, 100):
            random.shuffle(templist)
            
            lenval = int(float(len(templist))/5.0)

            testset = templist[:lenval]
            trainset = templist[lenval:]

            x_train = []
            y_train = []
            for k in range(0, len(trainset)):
                x_train.append(trainset[k][0])
                y_train.append(trainset[k][1])

            x_test = []
            y_test = []
            for k in range(0, len(testset)):
                x_test.append(testset[k][0])
                y_test.append(testset[k][1])

            model = CatBoostRegressor(iterations=1000,
                                        learning_rate=self.learning_rate,
                                        depth=self.depth,
                                        silent=True
                                        )

            eval_pool = Pool(x_test, y_test)
            model.fit(x_train, y_train, eval_set=eval_pool, early_stopping_rounds=10)

            acc = self.accuracy(x_test, y_test, model)

            global_AMSE += acc[0]
            global_AMSE_count += 1.0
            global_acc += acc[1]
            global_acc_count += 1.0

        global_AMSE *= 1.0/ global_AMSE_count
        global_acc *= 1.0/ global_acc_count

        return global_AMSE, global_acc



        """

        lenval = int(float(len(templist))/5.0)

        tempidx = []
        for i in range(0, len(templist)):
            if i == 0:
                tempidx.append(i)
            else:
                if i % lenval == 0:
                    tempidx.append(i)

        for i in range(0, len(tempidx)-1):
            
            testset = templist[tempidx[i:i+1]]
            trainset = templist[]

        """

        