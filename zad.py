class Student():
     def __init__(self, imie, nazwisko, kierunek):
        self.imie =  imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.lista_ocen = [2.0, 5.0, 3.0, 5.0]

     def dodaj_ocene(self, ocena):
         # Sprawdzam zakres ocen
         if ocena >= 2.0 and ocena <= 6.0:
             self.lista_ocen.append(ocena)
             return True
         else:
             return False

     # if dodaj_ocene(1.0):
     #     print("Dodano ocenę")
     # else:
     #     print("Nie udało się dodać oceny")

     def wylicz_srednia(self):
         print (sum(self.lista_ocen)/len(self.lista_ocen))

     def wylicz_srednia_n(self, n):
         self.lista_ocen.reverse()
         print (sum(self.lista_ocen[0:n])/len(self.lista_ocen[0:n]))


adam_nowak = Student("Adam", "Nowak", "tester")
print(adam_nowak.imie)
print(adam_nowak.lista_ocen)
adam_nowak.wylicz_srednia()
adam_nowak.wylicz_srednia_n(3)
