# Program som omvandlar tal till heltal
try:
    tal = input('Tal >')
    tal = int(tal)
    resultat = tal * 2
    print(resultat)
except:
    print('\'',tal,'\'', 'kan inte översättas till ett heltal')
