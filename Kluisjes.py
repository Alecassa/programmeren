#Alle kluizen nummer
alleKluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#het aantaal kluizen die op de station staat
aantalKluizen = len(alleKluizen)


#minimaal aantaal tekens voor het wachtwoord
minimaalAantalTekens = 4

def leesBestand():
    bestand = open('kluizen.txt')
    kluizenRegels = bestand.readlines()
    bestand.close()



    return kluizenRegels

def toonMenu():
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    watWilJeDoen = int(input("Wat wil je doen?"))
    doeOptie(watWilJeDoen)


def doeOptie(optie):
    if optie == 1:
        toonAantalKluizenVrij()
    elif optie ==2:
        nieuweKluisMaken()
    elif optie ==3:
        kluisOpenen()

def toonAantalKluizenVrij():
    kluisbestand = leesBestand()
    AantalKluizenVrij = aantalKluizen - len(kluisbestand)
    print(AantalKluizenVrij)

def nieuweKluisMaken():
    kluisbestand = leesBestand()
    beschikbareKluizen = alleKluizen
    for kluis in kluisbestand:
        kluisnummer = int(kluis[0])
        beschikbareKluizen.remove(kluisnummer)

    if len(beschikbareKluizen) == 0:
        print('Sorry, alle kluizen zitten vol..')
        return

    wachtwoord = input('Voer uw wachtwoord in: ')

    if len(wachtwoord) < minimaalAantalTekens:
        print('Een wachtwoord dient minimaal uit {}'.format(minimaalAantalTekens), 'tekens te bestaan!')
        return
    else:
        if len(wachtwoord) >= minimaalAantalTekens:
            kluisnummerVoorDeKlant = beschikbareKluizen[0]
            # kluisbestand.append([kluisnummerVoorDeKlant, wachtwoord])
            inBestandSchrijven([kluisnummerVoorDeKlant, wachtwoord])
            print('Uw kluisnummer is ' + str(kluisnummerVoorDeKlant))

def inBestandSchrijven(kluisgegeven):
    infile = open('kluizen.txt','a')

    infile.write(str(kluisgegeven[0]) + ';' + str(kluisgegeven[1] + '\n'))

    infile.close()

def kluisOpenen():
    print('U gaat nu een kluis opnenen...')
    kluisnummer = input('Geef uw kluisnummer op: ')
    wachtwoord = input('Geef uw wachtwoord op: ')
    alleRegelsVanKluizen = leesBestand()

    regel = str(kluisnummer) + ';' + str(wachtwoord) + '\n'

    kluisCombinatie = False

    for kluis in alleRegelsVanKluizen:

        if kluis == regel:
            kluisCombinatie = True

    if kluisCombinatie:
        print('Uw kluis is nu open')
    else:
        print('U heeft een verkeerde kluisnummer en/of wachtwoord ingevoerd')



toonMenu()
