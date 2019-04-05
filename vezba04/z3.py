import random
import time

def rand_list(min, max, num):
    l = random.sample(range(min, max), num)
    return l

def CountingSort(A, B, k):
    
    C = [0] * k
    
    for j in range(len(A)):
        C[A[j]] += 1
    
    for i in range(1, k):
        C[i] += C[i - 1]

    for j in range(len(A)):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

if __name__ == "__main__":
    A = rand_list(0, 50, 5)
    B = [0] * len(A)
    k = max(A) + 1
    print("Niz: ", A)
    CountingSort(A, B, k)
    print("Slozen: ", B)

    A = rand_list(0, 1000, 500)
    B = [0] * len(A)
    k = max(A) + 1
    start_time = time.perf_counter()
    CountingSort(A, B, k)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)

    A = rand_list(0, 10000, 5000)
    B = [0] * len(A)
    k = max(A) + 1
    start_time = time.perf_counter()
    CountingSort(A, B, k)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)

    A = rand_list(0, 100000, 50000)
    B = [0] * len(A)
    k = max(A) + 1
    start_time = time.perf_counter()
    CountingSort(A, B, k)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)