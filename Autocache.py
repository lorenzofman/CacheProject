from Processor import Processor
from Cache import Cache
Benchmarks = [
    "Benchmarks/amp.ss", 
    "Benchmarks/basicmath.ss",
    "Benchmarks/cc1.ss -O Benchmarks/1stmt.i",
    "Benchmarks/mm.ss"
]

processor = Processor(Cache(4096, 32, 8), Cache(4096, 32, 8))
processor.runSimCache("simplesim-3.0/sim-cache", "temp.txt", Benchmarks[0])