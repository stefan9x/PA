from cls import *

def TreeSearch(x, k):
    if x == None or k == x.data.a1:
        return x
    if k < x.data.a1:
        return TreeSearch(x.left, k)
    else:
        return TreeSearch(x.right, k)
    
def IterativeTreeSearch(x, k):
    while x != None and k != x.data.a1:
        if k < x.data.a1:
            x = x.left
        else:
            x = x.right
    return x

def TreeMinimum(x):
    while x.left != None:
        x = x.left
    return x.data.a1

def TreeMaximum(x):
    while x.right != None:
        x = x.right
    return x.data.a1

def TreeSuccessor(x):
    if x.right != None:
        return TreeMinimum(x.right)
    y = x.parent
    while y != None and x == y.right:
        x = y       
        y = y.parent
    return y.data.a1

def InOrderTreeWalk(x):
    if x != None:
        InOrderTreeWalk(x.left)
        print(x.data.a1)
        InOrderTreeWalk(x.right) 

def TreeInsert(root, z):
    y = None
    x = root
    while x != None:
        y = x
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y == None:
        root = z
    elif z.data.a1 < y.data.a1:
        y.left = z
    else:
        y.right = z

def Transplant(root, u, v):
    if u.parent == None:
        root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent

def TreeDelete(root, z):
    if z.left == None:
        Transplant(root, z, z.right)
    elif z.right == None:
        Transplant(root, z, z.left)
    else:
        y = TreeMinimum(z.right)
        if y.parent != z:
            Transplant(root, y, y.right)
            y.right = z.right
            y.right.parent = y

        Transplant(root, z, y)
        y.left = z.left
        y.left.parent = y
