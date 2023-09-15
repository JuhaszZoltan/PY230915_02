jegy:int = int(input('milyen jegyet kaptál? '))

if   jegy == 1: print('azt úgy mondják, hogy "elégtelen"')
elif jegy == 2: print('azt úgy mondják, hogy "elégséges"')
elif jegy == 3: print('azt úgy mondják, hogy "közepes"')
elif jegy == 4: print('azt úgy mondják, hogy "jó"')
elif jegy == 5: print('azt úgy mondják, hogy "jeles"')
else          : print('nincs is ilyen jegy... :O')
