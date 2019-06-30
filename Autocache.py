import os
Benchmarks = [
    "Benchmarks/amp.ss", 
    "Benchmarks/basicmath.ss",
    "Benchmarks/cc1.ss -O Benchmarks/1stmt.i",
    "Benchmarks/mm.ss"
    ]
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
    def arrangements(self):
        return self.cacheSize/(self.blockSize * self.associativity)
    def printCache(self):
        print("CacheSize: %d\nBlockSize: %d\nAssociativity: %d\nHits: %d \nMisses: %d \nLatency: %f \nEnergy: %f" % (self.cacheSize, self.blockSize, self.associativity, self.hits, self.misses, self.cacheLatency, self.cacheEnergy))
    def runSimCache(self, path):
        os.system("./%s -cache:il1 il1:%d:%d:%d:l -cache:il2 none -cache:dl1 dl1:%d:%d:%d:l -cache:dl2 none -redir:sim temp.txt -max:inst 100000 %s" % (
            path, 
            self.arrangements(), 
            self.blockSize, 
            self.associativity,
            self.arrangements(),
            self.blockSize,
            self.associativity,
            Benchmarks[0]))

cache = Cache(4096, 32, 8)
cache.runSimCache("simplesim-3.0/sim-cache")