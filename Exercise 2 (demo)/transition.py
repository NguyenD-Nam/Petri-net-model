class T:
    def __init__(self, name):
        self.name = name
        self.inArcs = []
        self.outArcs = []
        self.choiceProb = 0

    def tСondition(self):
        for arc in self.inArcs:
            if arc.prevP.tokens < arc.n:
                return False
        return True

    def perform(self, places):

        print("Transition {}".format(self.name))

        for a in self.inArcs:
            for pos in places:
                if pos.name == a.prevP.name:
                    pos.tokens -= 1
                    break
            print("from {}".format(a.prevP.name))

        for a in self.outArcs:
            for pos in places:
                if pos.name == a.nextP.name:
                    pos.tokens += 1
                    break
            print("to {}".format(a.nextP.name))

        return places