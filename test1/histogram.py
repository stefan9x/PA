def GetHistogram(l):
    D = dict()

    for c in l:
        if c in D:
            D[c] += 1
        else:
            D[c] = 1

    return D

if __name__ == "__main__":
    
    input1 = ["a", "a", "b", "c"]
    print("Input1: ", input1)
    print("Output1: ", GetHistogram(input1))
    print("-------------------")

    input2 = ["a", "a", "b", "c", "c", "c"]
    print("Input1: ", input2)
    print("Output1: ", GetHistogram(input2))
    print("-------------------")

    input3 = ["a", "a", "b", "c", "d", "d", "e"]
    print("Input1: ", input3)
    print("Output1: ", GetHistogram(input3))
    print("-------------------")

    input4 = ["a", "a", "b", "c", "c", "d", "e", "f", "f", "f", "f", "f"]
    print("Input1: ", input4)
    print("Output1: ", GetHistogram(input4))
    print("-------------------")
