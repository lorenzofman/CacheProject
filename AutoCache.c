#define CACHE 5
#define BLOCKSIZE 7
#define ASSOCIATIVITY 6

struct CacheResult 
{
    int cacheSize;
    int blockSize;
    int associativity;
    int hits;
    int misses;
    double cacheLatency;
    double cacheEnergy;
};

int main()
{
    const char* cactiFolder = "../cacti65/";
    const char* simCacheFolder = "../simplesim-3.0";
    int *cache = {1024,2048,4096,8192,16384};
    int *blockSize = {1,2,4,8,16,32,64};
    int *associativity = {0, 1, 2, 4, 8, 16, 32};
    for(int i = 0; i < CACHE; i++)
    {
        for(int j = 0; j < BLOCKSIZE; j++)
        {
            for(int k = 0; k < ASSOCIATIVITY; k++)
            {
                int c = cache[i];
                int b = blockSize[j];
                CreateCacheCombination();
            }
        }
    }
    int status = system("./");
}