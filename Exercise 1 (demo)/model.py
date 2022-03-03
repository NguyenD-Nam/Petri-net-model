import numpy as np
#import pandas as pd

class Model:
    def __init__(self, places, transitions):
        self.places = places
        self.transitions = transitions
        self.nextT = []

    def simulate(self, Imod):
        iteration = 0
        while iteration < Imod:

            for p in self.places:
                p.checkTokensStat()

            #1
            for t in self.transitions:
                if t.tСondition():
                    self.nextT.append(t)

            #2
            for t in self.nextT:
                t.choiceProb = 1/len(self.nextT)

            #3
            probabilities = []
            for t in self.nextT:
                probabilities.append(t.choiceProb)

            if self.nextT:
                choosenT = np.random.choice(self.nextT, p=probabilities)
            else:
                break
            
            print("\n-- Iteration: {} --".format(iteration+1))
            self.places = choosenT.perform(self.places)

            self.nextT = []
            iteration += 1

        #self.verification(iteration)

    # def verification(self, iteration):

    #     print("\n -- Verification --")

    #     names, maxp, minp, avgp = [],[],[],[]
    #     for p in self.places:
    #         names.append(p.name)
    #         maxp.append(p.tokensMax)
    #         minp.append(p.tokensMin)
    #         avgp.append(p.tokensAvg/iteration)

        #d = {'name': names, 'max num  of markers': maxp, 'min num  of markers': minp, 'avg num  of markers': avgp}
        #df_time = pd.DataFrame(data=d)
        #print(tabulate(df_time, headers='keys', tablefmt='psql'))