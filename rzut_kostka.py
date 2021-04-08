import random

liczbazKostki = random.randint(1,6) 
print('PROGRAM WYKONUJE RZUT KOSTKĄ'.center(65))
print('Kliknij ENTER aby wykonać rzut kostką'.center(65))
losowanie = input()
print( 'Wylosowałeś liczbę: ' + str(liczbazKostki) )

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





