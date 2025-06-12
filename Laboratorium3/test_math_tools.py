import unittest
from moja_biblioteka.narzedzia_matematyczne import srednia_arytmetyczna, czy_pierwsza

class TestNarzedziaMatematyczne(unittest.TestCase):
    def test_srednia_arytmetyczna(self):
        self.assertAlmostEqual(srednia_arytmetyczna([1, 2, 3]), 2)
        self.assertAlmostEqual(srednia_arytmetyczna([10, 20, 30]), 20)
        
    def test_srednia_pusta_lista(self):
        with self.assertRaises(ValueError):
            srednia_arytmetyczna([])
            
    def test_czy_pierwsza(self):
        self.assertTrue(czy_pierwsza(2))
        self.assertTrue(czy_pierwsza(17))
        self.assertFalse(czy_pierwsza(1))
        self.assertFalse(czy_pierwsza(15))