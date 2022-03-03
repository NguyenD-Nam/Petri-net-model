class P:
    def __init__(self, name, markers):
        self.name = name
        self.tokens = markers
        self.tokensMin = 0
        self.tokensMax = 0
        self.tokensAvg = 0
        if self.tokens:
            self.tokensMin = self.tokens

    def checkTokensStat(self):
        if self.tokens < self.tokensMin:
            self.tokensMin = self.tokens

        if self.tokens > self.tokensMax:
            self.tokensMax = self.tokens

        self.tokensAvg += self.tokens