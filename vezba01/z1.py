#Napisati funkciju koja računa zbir prvih N prirodnih brojeva

def zbir_n(n):
    zbir = 0
    for i in range(n):
        zbir+=i
    return zbir
    

if __name__ == "__main__":

    sum = zbir_n(10)

    print('Zbir prvih N brojeva:',sum)