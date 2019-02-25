def mapiranje(str, list):
    dict = {}
    dict[str] = list    
   
    del list[0]

    print("Recnik:", dict)


if(__name__ == "__main__"):
    list = []
    for i in range(10):
        list.append((i, i+1))

    print (list)
    mapiranje("string", list[:])
    
    print("Lista:", list)

    a = complex(1,2)
    b = complex(1,2)

    print(a)
    print(b)

    if (a is b):
        print("True")    
    elif (type(a) == type(b)):
        print("same type")
    else:
        print("not true")

    print('\n\n\n')

    a = "pera pepric"
    print(a[0:8:2])
    print(a[-1])
    print(a[::-1])
