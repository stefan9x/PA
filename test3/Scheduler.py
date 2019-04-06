import math

class Task:

    def __init__(self, p = None, s = None, d = None, t = None, r = None):
        self.priority = p
        self.start_time = s
        self.duration = d
        self.type = t
        self.recorder = r

    def __str__(self):
        return ("P:" + str(self.priority) + ", S:" + str(self.start_time) + ", D:" + str(self.duration) + ", T:" + str(self.type) + ", R:" + str(self.recorder))

def Parent(i):
    return i//2

def Left(i):
    return 2 * i + 1

def Right(i): 
    return 2 * i + 2

def MaxHeapify(A, i, heap_size):
    l = Left(i)
    r = Right(i)
    if l < heap_size and A[l].priority > A[i].priority:
        largest = l
    else:
        largest = i
    
    if r < heap_size and A[r].priority > A[largest].priority:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest, heap_size)

def BuildMaxHeap(A):
    heap_size = len(A)
    for i in range (heap_size // 2, -1, -1):
        MaxHeapify(A, i, heap_size)

def HeapSort(A, heap_size):
    BuildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        MaxHeapify(A, 0, heap_size)

def GetNextTask(A):
    el = A[0]
    A.pop(0)
    return el

def GetAllTasksSorted(A):
    B = A[:]
    HeapSort(B, len(B))
    return B

    
    