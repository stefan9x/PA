#Koristeći strukturu rečnink izračunati broj 
# ponavljanja reči koje se nalaze u datoteci dict_test.txt

if __name__ == "__main__":

    file = open('dict_test.txt', 'r')
    d = {}
    
    for line in file:
        words = []
        words += line.split(' ')
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1

    print(d)
    file.close()
        
    
            