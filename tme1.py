"""

int a 10 digit N puis N^2 si ce carré a moins de 20digits on complete avec des 0 a gauche
  xxxxxxxxx -> N a 10 digits
  xxxxxxxxxxxxxxxxxx -> N^2
  si N^2 est moins de 20digits on rajoute des 0 a gauche
  et apres on garde que les 10 nombres au milieu
    xxxxx|    xxxxxxxx       |xxxxx
      5        succ (N)         5

pour recuperer un nbombre x de digit on va diviser par 10^(la taille du nombre - x)

  """
from math import log, log10, ceil

"""question 1
N= 1 010 101 010
N^2 = 0 1 020 | 304 050 403 0 | 20 100

le successeur est : 3040504030

"""
"""question 2 
N = 100 000
N^2 =  000 00 |0 000 10 000 0 |00 000

on trouve 100 000 donc lambda = 1  (mauvais generateur) 


"""
"""question 3
attention c'est pas obligatoire que le carré ait 20digits
donc il faut recuperer le nombre de digit de ce carré puis retirer 5 a droite et le reste a gauche 
pour garder que 10 



"""
"""
def successeur1 (nb) :
    x= nb**2
    y = x // (10**5)
    z = x // (10**15)
    return y - (z * (10**10))


def successeur (nb, nbdigit = 10 ) :
    a = (nb**2)
    l = ceil(log10(a)) + 1
    droite = a // (10**(nbdigit/2))
    gauche = droite % (10**(nbdigit))
    return (gauche)


print(successeur(1578750190))

"""





"""exo 4 

1 - nombre de suites possible  10^(10^6)

2- prob ( suite 10^5 0 , 10^5 1 ,.....) = #nbr de suite qui realise ça / #nbr suites totale (10^10^6)



exo 5 

1- c'est a cause de la ligne 12 on fait un mod 10^10 et donc on garde que 10 digits

--- Algo K
"""



def getDigit(number, digit):
    return number // (10 ** digit) % 10

def etapes(x, current):
    match current:
        case 3:
            if x < 5 * 10**9:
                x += 5 * 10**9
                print("etape 3", x)
            return etapes(x, current + 1)
        case 4:
            x = (x**2 // 10**5) % 10**10
            print("etape 4", x)
            return etapes(x, current + 1)
        case 5:
            x = (1001001001 * x) % (10 ** 10)
            print("etape 5", x)
            return etapes(x, current + 1)
        case 6:
            if x < 10 ** 8:
                x += 9814055677
            else:
                x = (10 ** 10) - x
            print("etape 6", x)
            return etapes(x, current + 1)
        case 7:
            x = 10 ** 5 * (x % 10 ** 5) + (x // 10 ** 5)
            print("etape 7", x)
            return etapes(x, current + 1)
        case 8:
            x = (1001001001 * x) % (10 ** 10)
            print("etape 8", x)
            return etapes(x, current + 1)
        case 9:
            for i in range(10):
                d = getDigit(x, i)
                if d > 0:
                    x -= 10 ** i
            print("etape 9", x)
            return etapes(x, current + 1)
        case 10:
            if x < 10 ** 5:
                x = x ** 2 + 99999
            else:
                x -= 99999
            print("etape 10", x)
            return etapes(x, current + 1)
        case 11:
            while x < 10 ** 9:
                x *= 10
            print("etape 11", x)
            return etapes(x, current + 1)
        case 12:
            x = ((x * (x - 1)) // 10 ** 5) % 10 ** 10
            print("etape 12", x)
            return x  # Retourne enfin x après la dernière étape

def algorithmeKnuth(x):
    y = getDigit(x, 9)  # Récupère le 10ème chiffre de x
    for _ in range(y + 1):
        z = getDigit(x, 8) + 3  # Récupère le 9ème chiffre et ajoute 3
        print("Début avec x:", x, "et z:", z )

        x = etapes(x, z)  # Lance les étapes à partir de z
    return x

# Exemple d'exécution
result = algorithmeKnuth(6065038420)
print("Résultat final :", result)

"""
on constate que y a des graines ou la periode est egale a 1

si on regarde a la deuxieme iteration a l'etape 11 et on regarde la 4eme iteration a partir de ce nombre
on trouve le nombre successeur et le successeur de ce successeur on le trouve a la 6eme iteration a partir de ce nombre

"""