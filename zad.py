lista_ocen = [2.0, 5.0, 3.0, 5.0]

# Zad 1
def dodaj_ocene(ocena):
    # Sprawdzam zakres ocen
    if ocena >= 2.0 and ocena <= 6.0:
        lista_ocen.append(ocena)
        return True
    else:
        return False

if dodaj_ocene(1.0):
    print("Dodano ocenę")
else:
    print("Nie udało się dodać oceny")

# Zad 2
def wylicz_srednia():
    print (sum(lista_ocen)/len(lista_ocen))

wylicz_srednia()

# Zad 3
def wylicz_srednia_n(n):
    lista_ocen.reverse()
    print (lista_ocen)
    print (sum(lista_ocen[0:n])/len(lista_ocen[0:n]))

wylicz_srednia_n(3)
