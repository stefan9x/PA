from mergesort import MergeSort
import random

def ArrayFactory(n):
    l = random.sample(range(0, n*2), n)
    return l

def SortCheck(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            break

    if i == len(A) - 1:
        return "Niz je dobro slozen"
    else:
        return "Niz nije dobro slozen"

if __name__ == "__main__":
    A = ArrayFactory(40)
    B = A[:]
    print("Niz: ", A)
    MergeSort(A, 0, len(A) - 1)
    print("Slozen: ", A)  

    #Test
    B.sort(reverse = True)
    print("Test: ", SortCheck(A, B))

