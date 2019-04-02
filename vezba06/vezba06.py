class Histogram():
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.parent = None

class Node():
    def __init__(self, e1, e2, value, freq):
        self.left = e1
        self.right = e2
        self.value = value
        self.freq = freq
        
def GetHistogram(char_list):
    d = dict()
    l = []

    for char in char_list:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
        
    for i in d:
        a = Histogram(i, d[i])
        l.append(a)

    return l

def GetMinFreqElem(l):
    m = l[0]

    for e in l:
        if e.freq < m.freq:
            m = e

    return m

def RemoveElem(e, l):
    l.remove(e)

def PutElem(e, l):
    l.append(e)

def MakeNewElem(e1, e2):
    freq = e1.freq + e2.freq
    val = e1.value+e2.value
    
    n = Node(e1, e2, val, freq)
    e1.parent = n
    e2.parent = n

    return n

def GetEncVal(e, l):
    encoded = ""

    while e not in l:
        if e.parent.left == e:
            encoded += "0"
        else:
            encoded += "1"
        e = e.parent
    return encoded[::-1]
            
if __name__ == "__main__":

    input1 = ['a', 'b']
    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
    
    ulaz = [input1, input2, input3, input4, input5]

    for u in ulaz:
        hist = GetHistogram(u)
        temp = hist[:]

        print("Input:", u)
        size = 0

        for l in hist:
            print("Value:", l.value, ", Freq:", l.freq, sep='')
            size += l.freq * 8
            
        while len(hist) > 1:
            e1 = GetMinFreqElem(hist)
            RemoveElem(e1, hist)
            e2 = GetMinFreqElem(hist)
            RemoveElem(e2, hist)
            hist.append(MakeNewElem(e1, e2))

        d = dict()
        print("Char codes:")
        huf_size = 0
        for h in temp:
            a = GetEncVal(h, hist)
            d[h.value] = a
            print("|", h.value,"|", a, "|", sep="")
            huf_size += h.freq * len(a)

        out = ""
        for c in u:
            out += d[c]

        print("Encoded input:", out)
        print("Text size: ", size, "bits, Huffman size: ", huf_size, "bits", sep="")
        print("***************")
            
