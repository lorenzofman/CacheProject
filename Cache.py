class Cache:
    cacheSize = 4096
    blockSize = 32
    associativity = 8
    hits = 0
    misses = 0
    writebacks = 0
    cacheLatency = 0
    cacheEnergy = 0
    def __init__(self, cacheSize, blockSize, associativity):
        self.cacheSize = cacheSize
        self.blockSize = blockSize
        self.associativity = associativity
    def arrangements(self):
        return self.cacheSize/(self.blockSize * self.associativity) 
