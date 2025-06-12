import unittest
from moja_biblioteka.operacje_na_danych import polacz_slowniki, filtruj_liste

class TestOperacjeNaDanych(unittest.TestCase):
    def test_polacz_slowniki(self):
        slownik1 = {'a': 1, 'b': 2}
        slownik2 = {'b': 3, 'c': 4}
        wynik = {'a': 1, 'b': 3, 'c': 4}
        self.assertEqual(polacz_slowniki(slownik1, slownik2), wynik)
        
    def test_filtruj_liste(self):
        lista = [1, 2, 3, 4, 5]
        wynik = [2, 4]
        self.assertEqual(filtruj_liste(lista, lambda x: x % 2 == 0), wynik)