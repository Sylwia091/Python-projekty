import random

liczbazKostki = random.randint(1,6)
liczbazKostki2 = random.randint(1,6)
print('PROGRAM WYKONUJE RZUT KOSTKĄ'.center(69))
print('Kliknij ENTER aby wykonać rzut kostką'.center(69))
losowanie = input()
tekst1 = '''
          -------
          |     |
          |  ○  |
          |     |
          -------'''
tekst2 ='''
          -------
          | ○   |
          |     |
          |   ○ |
          -------'''
tekst3 = '''
          -------
          | ○   |
          |  ○  |
          |   ○ |
          -------'''

tekst4 = '''
          -------
          | ○ ○ |
          |     |
          | ○ ○ |
          -------'''
tekst5 = '''
          -------
          | ○ ○ |
          |  ○  |
          | ○ ○ |
          -------'''
tekst6 = '''
          -------
          | ○ ○ |
          | ○ ○ |
          | ○ ○ |
          -------'''

if liczbazKostki == 1:
    print (tekst1)
elif liczbazKostki == 2:
    print (tekst2)
elif liczbazKostki == 3:
    print (tekst3)
elif liczbazKostki == 4:
    print (tekst4)
elif liczbazKostki == 5:
    print (tekst5)
elif liczbazKostki == 6:
    print (tekst6)

print('Wylosowałeś liczbę oczek: '+ str(liczbazKostki))
print('Kliknij ENTER aby rzucić drugą kostką'.center(69))
losowanie = input()
if liczbazKostki2 == 1:
    print (tekst1)
elif liczbazKostki2 == 2:
    print (tekst2)
elif liczbazKostki2 == 3:
    print (tekst3)
elif liczbazKostki2 == 4:
    print (tekst4)
elif liczbazKostki2 == 5:
    print (tekst5)
elif liczbazKostki2 == 6:
    print (tekst6)
print('Wylosowałeś liczbę oczek: '+ str(liczbazKostki2))
print(('ŁĄCZNIE WYLOSOWAŁEŚ: ' + str(liczbazKostki+liczbazKostki2)+ ' oczek').center(69))
