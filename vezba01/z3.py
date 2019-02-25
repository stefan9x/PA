#Napiši program koji na ulazu prima dva stringa i na osnovu njih formira 
# i ispisuje novi string koji se sastoji od dva puta ponovljena prva tri 
# karaktera iz prvog stringa i poslednja tri karaktera drugog stringa

if __name__ == "__main__":

    s = input('Unesite dva stringa:')
    s1, s2 = s.split(' ')
    s_out = s1[0:3]+s1[0:3]+s2[-3:]
    print(s_out)

    