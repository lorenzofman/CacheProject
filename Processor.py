import re
import os
def readInfo(line):
    return int(re.findall(" (\d.*?) ", line)[0])
class Processor:
    dataCache = None
    instructionCache = None
    def __init__(self, dataCache, instructionCache):
        self.dataCache = dataCache
        self.instructionCache = instructionCache
    def runSimCache(self, executablePath, tempFilePath, benchmarkPath):
        os.system("./%s -cache:il1 il1:%d:%d:%d:l -cache:il2 none -cache:dl1 dl1:%d:%d:%d:l -cache:dl2 none -redir:sim %s %s" % (
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
    def runCacti(self, executablePath, catciConfigPath, cactiBasePath):
        self.dataCache.runCacti(executablePath, catciConfigPath, cactiBasePath)
        self.instructionCache.runCacti(executablePath, catciConfigPath, cactiBasePath)