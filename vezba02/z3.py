# Implementirati algoritam za linearnu pretragu brojeva. Ulazni podaci su niz (lista)
# brojeva i tražena vrednost. Izlaz je pozicija na kojoj se nalazi tražena vrednost.

import random

def rand_list(min, max, num_of_el):
    list = random.sample(range(min, max), num_of_el)
    return list

def lin_search(niz, a):
    poz = "Nije pronadjen"
    for i in range(0, len(niz)):
        if niz[i] == a:
            poz = i
            break
    return poz

if __name__ == "__main__":
    A = rand_list(0, 20, 10)
    
    print("Niz:", A)
    vr = int(input("Broj za pretragu: "))
    poz = lin_search(A, vr)
    print("Pozicija broja %d: %s" %(vr, poz))    