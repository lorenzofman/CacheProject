import subprocess
import re
def readFloatInfo(line):
    return float(re.findall("(\d.*?) ", line)[0])
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
        print("CacheSize: %d\tBlockSize: %d\tAssociativity: %d\tHits: %d \tMisses: %d\tWritebacks: %d" % (self.cacheSize, self.blockSize, self.associativity, self.hits, self.misses, self.writebacks))
    def runCacti(self, executablePath, catciConfigPath, cactiBasePath):
        # Memory cache
        finalFile = open(catciConfigPath, "w")
        finalFile.write("-size (bytes) %d\n-block size (bytes) %d\n-associativity %d\n" % (self.cacheSize,self.blockSize, self.associativity))

        with open(cactiBasePath, "r") as otherParameters :
            filedata = otherParameters.read()
            finalFile.write(filedata)
        finalFile.close()
        out = str(subprocess.check_output([executablePath,'-infile',catciConfigPath]))
        for line in out.splitlines():
            if line.startswith("    Access time"):
                self.cacheLatency = readFloatInfo(line + " ")
            elif line.startswith("    Read Energy "):
                self.cacheEnergy = readFloatInfo(line + " ")