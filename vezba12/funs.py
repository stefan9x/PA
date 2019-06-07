import string
import random

def LCS(S, n, T, m):
    if n < 0 or m < 0:
        return 0
    if S[n] == T[m]:
        return 1 + LCS(S, n - 1, T, m - 1)
    else:
        return max(LCS(S, n - 1, T, m), LCS(S, n, T, m - 1)) 

def LCS_Length(x, y):
    m = len(x) + 1
    n = len(y) + 1

    b = []
    c = []

    for i in range(m):
        b.append([])
        c.append([])
        for j in range(n):
            b[i].append(0)
            c[i].append(0)

    for i in range(1, m):
        for j in range(1, n):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "↖"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "↑"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "←"
    
    return (c, b)

def print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return 0
    
    if b[i][j] == "↖":
        print_LCS(b, X, i - 1, j - 1)
        print(X[i - 1], end = "")
    elif b[i][j] == "↑":
        print_LCS(b, X, i - 1, j)
    else:
        print_LCS(b, X, i, j - 1)

def print_matrix(c, b):
    for i in c:
        print(i)

    print()
    for j in b:
        print(j)

def gen_rand_string(len_x, len_y):
    
    s1 = []
    s2 = []

    for i in range(len_x):
        rnd = random.randint(0, len(string.ascii_uppercase) - 1)
        s1.append(string.ascii_uppercase[rnd])

    for i in range(len_y):
        rnd = random.randint(0, len(string.ascii_uppercase) - 1)
        s2.append(string.ascii_uppercase[rnd])

    return ("".join(s1), "".join(s2))
    