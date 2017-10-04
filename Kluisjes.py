#Alle kluizen nummer
alleKluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#het aantaal kluizen die op de station staat
aantalKluizen = len(alleKluizen)
kluisbestand =
def leesBestand:
    bestand = open('kluizen.txt','r')
def toonMenu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    watWilJeDoen = int(input("Wat wil je doen?"))
    doeOptie(watWilJeDoen)

def doeOptie(optie):
    if optie == 1:
        toonAantalKluizenVrij()

def toonAantalKluizenVrij():
    print('test')

toonMenu()

