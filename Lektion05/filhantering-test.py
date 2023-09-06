import os
import time

if os.path.exists('textfil.txt'):
    # Öppna en befintlig fil
    print('Öpnnar fil, var god vänta')
    for i in range(10):
        print(str('.'), end='')
        time.sleep(0.5)
    f = open('textfil.txt', 'a')
    print('\nFilen är öpnnad')
else:
    # Skapa en ny fil
    print('Skapar fil, var god vänta')
    for i in range(10):
        print(str('.'), end='')
        time.sleep(0.5)
    f = open('textfil.txt', 'x')
    print('\nFilen är skapad')

f.write("Rad 1.\n")
f.write("Rad 2.\n")
f.write("Rad 3.\n")

print('\nInformationen är nu skriven till filen.')
with open('textfil.txt') as f:
    text = f.read()
print(text)

val = input('\nVill du ta bort textfil.txt? (j/n) ')
if val.lower() == 'j':
    if os.path.exists("textfil.txt"):
        os.remove("textfil.txt")
    else:
        print("The file does not exist")
