import os
from random import shuffle

# Två listor som innehåller alla kortnamn/färger och värden
card_names = ['Klöver', 'Ruter', 'Hjärter', 'Spader']
card_values = ['Ess', '2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'Knekt', 'Dam', 'Kung']


# Klass innehållandes alla kort och metoder kopplade till korten
class Card:

    def __init__(self, names, values):
        self.names = names
        self.values = values

    # String representation av inmatat objekt vid utskrift.
    def __str__(self):
        return f'{self.names}, {self.values}'

    # Metod som vid anrop skapar en kortlek med alla 52 kort
    def card_deck_creation(self):
        card_list = []
        for c_name in self.names:
            for c_value in self.values:
                card_list.append([c_name, c_value])
        return card_list

    # Tar emot kortleken och blandar slumpmässigt alla kort
    @staticmethod
    def card_deck_shuffle(kortlek: list):
        shuffle(kortlek)
        return kortlek


# Klass som tar hand om den kortlek man spelar med för tillfället
class Hand:

    @staticmethod
    def kortlek():
        # Korten dras ett i taget från slutet av kortleken för att lättare matcha rätt indexvärde
        # vid borttagning av dragna kort.
        # Värdena sätts till globala för att stanna kvar utanför metoden
        global spelar_poang
        global i

        while i > -1:
            print(f'Du drog: {kortlek_blandad[i][0]} {kortlek_blandad[i][1]}')

            # Om kortet inte har en siffra hämtas värdet från dictionaryt kort_varden
            if kortlek_blandad[i][1] in kort_varden:
                spelar_poang += kort_varden[kortlek_blandad[i][1]]
            # Spelarval om kortet är ett ess
            elif kortlek_blandad[i][1] == 'Ess':
                ess_val = input('Välj värde: 1 eller 14 > ')
                if ess_val == '1':
                    spelar_poang += 1
                elif ess_val == '14':
                    spelar_poang += 14
                else:
                    print('Skriv 1 eller 14 !')
            else:
                spelar_poang += int(kortlek_blandad[i][1])

            kortlek_blandad.pop(i)  # Kortet tas bort från kortleken
            i -= 1  # Nedräkning av index för loopen
            print(f'Din poäng är: {spelar_poang}')
            print('-' * ui_width)
            kort_val = input('* Ett till kort? (j/n) > ').lower()
            if kort_val == 'j':
                continue
            elif kort_val == 'n':
                break

    @staticmethod
    def dator_kort():
        global dator_poang
        global i

        while i > -1:
            print(f'Datorn drog: {kortlek_blandad[i][0]} {kortlek_blandad[i][1]}')

            # Om kortet inte har en siffra hämtas värdet från dictionaryt kort_varden
            if kortlek_blandad[i][1] in kort_varden:
                dator_poang += kort_varden[kortlek_blandad[i][1]]
            # Datorval om kortet är ett ess
            elif kortlek_blandad[i][1] == 'Ess':
                # Datorn väljer värde utifrån poäng hittils
                # ess_val = input('Välj värde: 1 eller 14 > ')
                if dator_poang > 7:
                    dator_poang += 1
                else:
                    dator_poang += 14

            else:
                dator_poang += int(kortlek_blandad[i][1])

            kortlek_blandad.pop(i)  # Kortet tas bort från kortleken
            i -= 1  # Nedräkning av index för loopen
            print(f'Datorns poäng är: {dator_poang}')
            print('-' * ui_width)
            # Valmekanism för om datorn ska fortsätta eller inte
            if dator_poang >= 17:
                break
            else:
                continue


# Funktion för rensande av skärmen
def clear():
    if os.name == "nt":
        os.system("cls")

    elif os.name == "posix":
        os.system("clear")


# Objektet kort skapas och lagrar 2 listor med kortvärden
kort = Card(card_names, card_values)

# Hela kortleken sparas i attributet .kortlek
kort.kortlek = Card.card_deck_creation(kort)

# Här lagras kortleken med blandade kort
kortlek_blandad = Card.card_deck_shuffle(kort.kortlek)

# En dictonary som översätter kortvärden till poäng
kort_varden = {
    'Knekt': 11,
    'Dam': 12,
    'Kung': 13
}
# Spelarens poäng
spelar_poang = 0
# Datorns poäng
dator_poang = 0
# Räknare för kortleken
i = 51

ui_width = 30

# UI skrivs ut
while True:
    clear()
    print('-' * ui_width)
    print('|'.ljust(28), '|')
    print('|', 'Välkommen till'.center(26), '|')
    print('|', 'Kortspelet Tjugoett'.center(26), '|')
    print('-' * ui_width)
    print('| Siffrorna på korten\n| motsvarar deras värden och\n| knekt(11), dam(12), kung(13)\n| ess (1 eller 14)')
    print('-' * ui_width)
    print('| 1 | Börja spela')
    print('| 2 | Avsluta')
    print('-' * ui_width)

    val = input('> ')

    if val == '1':
        Hand.kortlek()
        if spelar_poang > 21:
            print(f'\nDatorn vann! Du fick {spelar_poang} poäng')
            print('-' * ui_width)
            input('Tryck Enter för att fortsätta')

        elif spelar_poang == 21:
            print(f'\nDu vann! Du fick {spelar_poang} poäng')
            input('Tryck Enter för att börja om')

        elif spelar_poang < 21:
            clear()
            print(f'\nDu fick {spelar_poang} poäng')
            print('Nu är det datorns tur.')
            Hand.dator_kort()
            if dator_poang > 21:
                print('Grattis du vann!')
                input('Tryck Enter för att börja om')
                continue
            elif spelar_poang > dator_poang:
                print(f'Grattis du vann! Du fick {spelar_poang} poäng')
                input('Tryck Enter för att börja om')
                continue
            else:
                print(f'Datorn vann med {dator_poang} poäng.\nDu fick {spelar_poang} poäng')
                input('Tryck Enter för att börja om')

        # Nollställning av poäng inför nästa omgång
        spelar_poang = 0
        dator_poang = 0

    # Avslut av programmet
    elif val == '2':
        print('Tack för att du spelade Tjugoett!')
        print(len(kortlek_blandad))
        break
