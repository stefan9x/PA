import math 
import random
import time

class Data:
    def __init__(self, key):
        self.key = key
        self.literal = str(key)

def randList(min, max, num):
    l = []
    for i in range(num):
        rand = random.randint(min, max)
        l.append(rand)
    return l

def h1(k, m):
    return k.key % m

def h2(k, m):
    return 1 + (k.key % (m - 1))

def linProb(k, m, i):
    return (h1(k, m) + i) % m

def quadProb(k, m, i):
    c1 = c2 = 1/2

    return (h1(k, m) + c1 * i + c2 * i * i) % m

def doubleHash(k, m):
    return (h1(k, m) + h2(k, m)) % m

def hashInsert(T, k, m):
    i = 0

    while(i != m):
        j = linProb(k, m, i)
        if T[j] == None:
            T[j] = k
            return j
        else:
            i += 1

    return -1

def hashSearch(T, k, m):
    i = 0
    
    while True:
        j = linProb(k, m, i)
            
        if T[j].key == k.key:
            return j

        i += 1

        if T[j] == None or i == m:
            return None

""" def hashDelete(T, k, m):
    i = 0
    
    while True:
        j = linProb(k, m, i)
            
        if T[j].key == k.key:
            T[j] = "Deleted"
            break
        else:
            i += 1 """

if __name__ == "__main__":
    
    for n in [10000, 50000, 100000]:
        L = randList(0, n*2, n)
            
        for m in [n, n//2, n//4]:
                
            T = [None] * m

            startTime = time.perf_counter()
            print("\n")
            for l in L:
                k = Data(l)
                res = hashInsert(T, k, m)
                
                if res == -1:
                    print("Hash overflow")
                    break
                
            endTime = time.perf_counter() - startTime

            print("Time for table form(n=%d, m=%d):" %(n, m), endTime)
    
            r = random.randint(0, n)
            src = Data(L[r])
            print("Searching for %d" %(src.key))

            startTime = time.perf_counter()

            src_res = hashSearch(T, src, m)

            endTime = time.perf_counter() - startTime

            #del_res = hashDelete(T, src, m)

            if src_res != None:
                print("Found! Took:", endTime)
            else:
                print("Not Found! Took:", endTime)

            
    