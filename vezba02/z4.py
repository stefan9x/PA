# Implementirati algoritam za binarnu pretragu brojeva. Ulazni podaci su niz (lista)
# brojeva i tražena vrednost. Izlaz je pozicija na kojoj se nalazi tražena vrednost.

from z1 import insertion_sort
from z1 import rand_list

# Resenje sa rekurzijom
def bin_search_recur(niz, vr, pocetak , kraj):
    poz = int((pocetak + kraj)/2)
    if vr == niz[poz]:
        return poz
    elif pocetak >= kraj or poz == pocetak or poz == kraj:
        return "Nije pronadjen"
    elif vr < niz[poz]:
        return bin_search_recur(niz, vr, pocetak, poz)
    else:
        return bin_search_recur(niz, vr, poz, kraj)

# Resenje bez rekurzije
def bin_search(niz, vr):
    pocetak = 0
    kraj = len(niz)
    while pocetak <= kraj:
        mid = int((pocetak + kraj) / 2)
        if vr > niz[mid]:
            pocetak = mid + 1
        elif vr < niz[mid]:
            kraj = mid - 1
        else:
            return mid
    return "Nije pronadjen"

if __name__ == "__main__":
    A = rand_list(0, 20, 10)
    
    insertion_sort(A)
    print("Slozen niz:", A)

    vr = int(input("Broj za pretragu: "))
    poz = bin_search(A, vr)
    print("Pozicija broja %d: %s" %(vr, poz))    

