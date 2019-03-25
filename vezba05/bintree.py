from fun import *
import random

def RandomData(min, max, el):
    N = []
    for i in range(el):
        a = random.randint(min, max)
        b = str(random.randint(min, max))
        D = Data(a,b)
        Nn = Node(d = D)
        N.append(Nn)

    return N

if __name__ == "__main__":
    
    elNum = 7
    N = RandomData(0,elNum*2,elNum)
    
    print("Nodes:")
    print(N[0].data.a1)
    for i in range(1, elNum):
        TreeInsert(N[0], N[i])
        print(N[i].data.a1)

    print("InOrder:")
    InOrderTreeWalk(N[0])

    print("TreeSearch for 5: ", TreeSearch(N[0], 5))
    print("IterativeTreeSearch for 5: ", IterativeTreeSearch(N[0], 5))
    print("TreeMinimum: ", TreeMinimum(N[0]))
    print("TreeMaximum: ", TreeMaximum(N[0]))
    print("N[%d]=%d TreeSuccessor: %d" %(3, N[3].data.a1, TreeSuccessor(N[3])))
    print("Deleting node N[%d] with data %d." %(3, N[3].data.a1))
    TreeDelete(N[0], N[3])
    InOrderTreeWalk(N[0])
    
    
    
    