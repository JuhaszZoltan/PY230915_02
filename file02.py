# programozási vezérlők

# elágazás / szelekció / "if - if+else - elif..."
# if (ha) <logikai értéket visszaadó feltétel>:
    # egy indentációval (bekezdéssel/behúzással) jobbra 
    # az a szubrutin, ami akkor fut le,
    # ha a feltétel True (igaz) értéket ad vissza
# else (különben):
    # elhagyható, nem kell feltétlenül else ágat írni
    # egy indentációval (bekezdéssel/behúzással) jobbra 
    # az a szubrutin, ami akkor fut le,
    # ha az if utáni feltétel False (hamis) értéket ad vissza


nev:str = input('írd be a neved: ')
valasz:str = input(f'Szia {nev}, szeretsz programozni? ')

if valasz == 'igen':
    print('az tök jó, akkor még sokra viheted az életben! :3 uwu')
else:
    print('akkor rábasztál, mert én azt tanítom :((((')

