#Ponoviti zadatak 6 ali umesto liste koristiti skup

if __name__ == "__main__":
    s = set()
    s.add((1, 1.12, 'qwe'))
    s.add((2, 2.34, 'rty'))
    s.add((3, 3.56, 'asd'))
    s.add((4, 4.78, 'fgh'))

    print('Prije:', s)
    s.pop()
    print('Posle:', s)