#Napisati program koji u listu smešta četiri torke formata (integer, float, string) 
# i ispisuje ih, nakon čega briše prvu torku koja je ubačena u listu;

if __name__ == '__main__':
    l = []
    l.append((1, 1.12, 'qwe'))
    l.append((2, 2.34, 'rty'))
    l.append((3, 3.56, 'asd'))
    l.append((4, 4.78, 'fgh'))

    print('Prije:', l)
    l.remove(l[0])
    print('Posle:', l)