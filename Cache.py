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
    def printCache(self):
        print("CacheSize: %d\nBlockSize: %d\nAssociativity: %d\nHits: %d \nMisses: %d\nWritebacks: %d \nLatency: %f \nEnergy: %f" % (self.cacheSize, self.blockSize, self.associativity, self.hits, self.misses, self.writebacks, self.cacheLatency, self.cacheEnergy))
