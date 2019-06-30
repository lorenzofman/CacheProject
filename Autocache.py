import os
Benchmarks = []
class Cache:
    cacheSize = 4096
    blockSize = 32
    associativity = 8
    hits = 0
    misses = 0
    cacheLatency = 0
    cacheEnergy = 0
    def __init__(self, cacheSize, blockSize, associativity):
        self.cacheSize = cacheSize
        self.blockSize = blockSize
        self.associativity = associativity
    def printCache(self):
        print("CacheSize: %d\nBlockSize: %d\nAssociativity: %d\nHits: %d \nMisses: %d \nLatency: %f \nEnergy: %f" % (self.cacheSize, self.blockSize, self.associativity, self.hits, self.misses, self.cacheLatency, self.cacheEnergy))
    def runSimCache(self, path):
        os.system("./%s" % path)


cache = Cache(4096, 32, 8)
cache.runSimCache("simplesim-3.0/sim-cache")