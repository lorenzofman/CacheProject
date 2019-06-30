from Processor import Processor
from Cache import Cache
Benchmarks = [
    "Benchmarks/amp.ss",
    "Benchmarks/cc1.ss -O Benchmarks/1stmt.i",
    "Benchmarks/basicmath.ss",
    "Benchmarks/mm.ss"
]
bench = Benchmarks[3]
processor = Processor(Cache(32768, 32, 4), Cache(32768, 32, 4))
processor.runSimCache("simplesim-3.0/sim-cache", "temp.txt", bench)
processor.runCacti("cacti65/cacti", "cacti65/cache.cfg", "cacti65/cacheImmutable.cfg")