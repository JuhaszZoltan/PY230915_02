print('hello, world!')

nev:str = input('szia, ird be a neved: ')
print(f'Milyen szép név az, hogy {nev}!')

# tipusok

# numerikus (egész és a lebegőpontos)
x:int = 42
y:float = 3.14

# numerikus operátorok
print(10 + 20)
print(20 - 10)
print(10 * 20)
print(20 / 3) # sima osztás
print(20 // 3) # egészosztás
print(20 % 3) # maradékszámítás
print(2 ** 10) # hatványozás (2^10)
print(9 ** .5) # négyzetgyökvonás == 0.5.-re emelés

# karakteres/szöveges
kar01:str = 'egyik jelöles'
kar02:str = "másik jelölés"

kar03:str = "I'm out of this shit"
kar04:str = 'Pisti mondja: "engedd el!"'
kar05:str = 'Peter said: "I' + "'m out of this shit" +'"'
print(kar05)

# konkatenáció (összefűzés)
v01:str = 'kutya'
v02:str = 'eledel'
print(v01 + v02)

v03:str = 'hörcsög'
print(1000 * f'{v03} ')

# logikai
b:bool = True # False

# compare (összehasonlító) operátorok

# <, >, <=, >=, ==, !=
# compare operator eredménye logikai (True/False) érték
x:int = 10
y:int = 20
print(x > y)

# logikai operátorok:
# and (logikai és) -> akkor igaz, ha mindkét operandus igaz
# or (logikai vagy) -> akkor igaz, ha legalább az egyik igaz
# not (logikai negáció, egy operandusú)
print(not 'cica' == 'kutya') # -> True
# not True -> False
# not False -> True
