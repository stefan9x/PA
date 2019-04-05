import random
import time

def rand_list(min, max, num):
    l = random.sample(range(min, max), num)
    return l

def ind(i):
    return i//10

def BucketSort(A):
    size = max(A) // 10 + 1
    B = [0] * size
    
    for i in range(size):
        B[i] = []

    for i in range(len(A)):
        B[ind(A[i])].append(A[i])

    for i in range(size - 1):
        B[i].sort()
    
    A.clear()

    for i in range(size):
        A += B[i]

if __name__ == "__main__":
 
    A = rand_list(0, 99, 5)

    print("Niz: ", A)
    BucketSort(A)
    print("Slozen: ", A)

    A = rand_list(0, 99, 2)
    start_time = time.perf_counter()
    BucketSort(A)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)

    A = rand_list(0, 99, 8)
    start_time = time.perf_counter()
    BucketSort(A)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)