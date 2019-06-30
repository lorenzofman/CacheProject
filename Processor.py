import os
import re
def readInfo(line):
    return int(re.findall(" \d.*? ", line)[0])
class Processor:
    dataCache = None
    instructionsCache = None
    def __init__(self, dataCache, instructionsCache):
        self.dataCache = dataCache
        self.instructionCache = instructionsCache
    def runSimCache(self, executablePath, tempFilePath, benchmarkPath):
        os.system("./%s -cache:il1 il1:%d:%d:%d:l -cache:il2 none -cache:dl1 dl1:%d:%d:%d:l -cache:dl2 none -redir:sim %s -max:inst 100000 %s" % (
            executablePath, 
            self.dataCache.arrangements(), 
            self.dataCache.blockSize, 
            self.dataCache.associativity,
            self.instructionCache.arrangements(),
            self.instructionCache.blockSize,
            self.instructionCache.associativity,
            tempFilePath,
            benchmarkPath))
        file = open(tempFilePath, "r")
        for line in file:
            if line.startswith("il1.hits"):
                self.instructionCache.hits = readInfo(line)
            elif line.startswith("il1.misses"):
                self.instructionCache.misses = readInfo(line)
            elif line.startswith("dl1.hits"):
                self.dataCache.hits = readInfo(line)
            elif line.startswith("dl1.misses"):
                self.dataCache.misses = readInfo(line)
            elif line.startswith("dl1.writebacks"): 
                self.dataCache.writebacks = readInfo(line)
        print "\nInstructions cache"
        self.instructionCache.printCache()
        print "\nData cache"
        self.dataCache.printCache()