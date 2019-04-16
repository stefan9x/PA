import math 
import random
import time

class Data:
    def __init__(self, key):
        self.key = key
        self.literal = str(key)

def randList(min, max, num):
    l = []
    for i in range(0, num):
        rand = random.randint(min, max)
        l.append(rand)
    return l

def divHash(k, m):
    return k.key % m

def multiHash(k, m):
    A = 0.6180339887
    return math.floor(m * ((k.key * A) % 1))

def uniHash(k, m, p):
    a = random.randint(0, p)
    b = random.randint(1, p)

    return ((a * k.key + b) % p) % m

def chainInsert(T, x, h):
    chainDel(T, x, h)

    T[h].append(x)

def chainSrc(T, k, h):
    for i in T[h]:
        if i.key == k.key:
            return i
        else:
            return None
    
def chainDel(T, x, h):
    if x in T[h]:
        T[h].remove(x)

if __name__  == "__main__":
    
    for p in [23, 9973, 99991]:
        for n in [10000, 50000, 100000]:
            L = randList(0, p, n)
            
            for m in [p, p//2, p//4]:
                
                T = []
                for i in range(0, m):
                    T.append([])
                
                startTime = time.perf_counter()

                for l in L:
                    k = Data(l)
                    h = divHash(k, m)
                    chainInsert(T, k, h)

                endTime = time.perf_counter() - startTime

                print("\nTime for table form(n=%d, p=%d, m=%d):" %(n, p, m), endTime)

                r = random.randint(0, n)
                src = Data(L[r])
                h_src = divHash(src, m)
                print("Searching for %d" %(src.key))

                startTime = time.perf_counter()

                src_res = chainSrc(T, src, h_src)

                endTime = time.perf_counter() - startTime

                if src_res != None:
                    print("Found! Took:", endTime)
                else:
                    print("Not Found! Took:", endTime)

                
              

