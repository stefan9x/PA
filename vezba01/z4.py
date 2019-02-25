#Inicijalizovati listu sa prvih 100 brojeva i 
# ispisati je u obrnutom redosledu

if __name__ == "__main__":

    l = []
    
    for i in range(100):
        l.append(i)

    for b in reversed(l):
        print(b)

    
    