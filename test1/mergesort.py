import math

def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L, R = [], []

    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])

    i = 0
    j = 0

    L.append(-math.inf)
    R.append(-math.inf)

    for k in range(p, r + 1):
        if L[i] >= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)