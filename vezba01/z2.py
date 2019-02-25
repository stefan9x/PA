#Napisati funkciju koja računa zbir kvadrata prvih N prirodnih brojeva
#parametar N se unosi kao ulazni argument programa;

import sys

def zbir2_n(n):
    zbir = 0
    for i in range(n):
        zbir+=i**2
    zbir+=n**2
    return zbir
    

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print('Unesite N kao argument')
    else:
        sum = zbir2_n(int(sys.argv[1]))
        print('Zbir kvadrata prvih N brojeva:', sum)