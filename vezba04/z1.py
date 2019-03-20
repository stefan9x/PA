import random
import time

def rand_list(min, max, num):
    l = random.sample(range(min, max), num)
    return l

def Parent(i):
    return i // 2

def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2

def MaxHeapify(A, i, heap_size):
    l = Left(i)
    r = Right(i)
    if l <= heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, heap_size)

def BuildMaxHeap(A):
    heap_size = len(A) - 1
    for i in range(len(A)//2, -1, -1):
        MaxHeapify(A, i, heap_size)

    return heap_size

def HeapSort(A):
    heap_size = BuildMaxHeap(A)
    for i in range (len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        MaxHeapify(A, 0, heap_size)

if __name__ == "__main__":
    A = rand_list(0, 50, 20)
    print("Niz: ", A)
    HeapSort(A)
    print("Slozen: ", A)
    
    A = rand_list(0, 1000, 500)
    start_time = time.perf_counter()
    HeapSort(A)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)

    A = rand_list(0, 10000, 5000)
    start_time = time.perf_counter()
    HeapSort(A)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)

    A = rand_list(0, 100000, 50000)
    start_time = time.perf_counter()
    HeapSort(A)
    end_time = time.perf_counter() - start_time 
    print("Vreme za " + str(len(A)) + ":", end_time)
    
    