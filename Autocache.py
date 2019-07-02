from Processor import Processor
from Cache import Cache
Benchmarks = [
    "Benchmarks/cc1.ss -O Benchmarks/1stmt.i",
    "Benchmarks/mm.ss"
]
processors = []
cachePossibilities = [512, 1024, 2048, 4096, 8192]
blockSizePossibilities = [32, 64, 128]
associativityPossibilites = [1, 2, 4, 8, 16, 32]
for cache in cachePossibilities:
    for blockSize in blockSizePossibilities:
        for associativity in associativityPossibilites:
            for bench in Benchmarks:
                if cache > blockSize * associativity * 8:
                    processor = Processor(Cache(cache, blockSize, associativity), Cache(cache, blockSize, associativity))
                    processor.runSimCache("simplesim-3.0/sim-cache", "temp.txt", bench)
                    processor.runCacti("cacti65/cacti", "cacti65/cache.cfg", "cacti65/cacheImmutable.cfg")
                    processor.dataCache.printCache()
                    processors.append(processor)
out = open("out.csv", "w")
out.write("Cache size, Block Size, Associativity, Cache Latency, Cache Energy, Data Hits, Data Misses, Writebacks, Instructions Hits, Instruction Misses\n")
for proc in processors:
    out.write("%d,%d,%d,%f,%f,%d,%d,%d,%d,%d\n" % (
        proc.dataCache.cacheSize, 
        proc.dataCache.blockSize,
        proc.dataCache.associativity,
        proc.dataCache.cacheLatency,
        proc.dataCache.cacheEnergy,
        proc.dataCache.hits,
        proc.dataCache.misses,
        proc.dataCache.writebacks,
        proc.instructionCache.hits,
        proc.instructionCache.misses))    
out.close()
    
