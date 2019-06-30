import os
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