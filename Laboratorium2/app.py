import re
from datetime import datetime
from typing import List, Union

def sprawdz_email(email: str) -> bool:
    """
    Sprawdza poprawność formatu adresu email.
    
    Args:
        email (str): Adres email do walidacji
        
    Returns:
        bool: True jeśli email jest poprawny, False w przeciwnym przypadku
        
    Przykłady:
        >>> sprawdz_email("test@example.com")
        True
        >>> sprawdz_email("niepoprawny.email")
        False
    """
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email) is not None

def oblicz_pole_prostokata(szerokosc: float, wysokosc: float) -> float:
    """
    Oblicza pole prostokąta o podanych wymiarach.
    
    Args:
        szerokosc (float): Szerokość prostokąta (musi być >= 0)
        wysokosc (float): Wysokość prostokąta (musi być >= 0)
        
    Returns:
        float: Obliczone pole prostokąta
        
    Raises:
        ValueError: Jeśli któryś z wymiarów jest ujemny
        
    Przykłady:
        >>> oblicz_pole_prostokata(3, 4)
        12.0
    """
    if szerokosc < 0 or wysokosc < 0:
        raise ValueError("Wymiary nie mogą być ujemne")
    return szerokosc * wysokosc

def filtruj_liczby_parzyste(liczby: List[Union[int, float]]) -> List[int]:
    """
    Filtruje i zwraca tylko parzyste liczby całkowite z listy.
    
    Args:
        liczby (List[Union[int, float]]): Lista liczb do filtracji
        
    Returns:
        List[int]: Lista zawierająca tylko parzyste liczby całkowite
        
    Przykłady:
        >>> filtruj_liczby_parzyste([1, 2, 3, 4.5, 6])
        [2, 6]
    """
    return [liczba for liczba in liczby if isinstance(liczba, int) and liczba % 2 == 0]

def konwertuj_date(data_str: str) -> str:
    """
    Konwertuje datę z formatu RRRR-MM-DD na DD.MM.RRRR.
    
    Args:
        data_str (str): Data w formacie RRRR-MM-DD
        
    Returns:
        str: Data w formacie DD.MM.RRRR
        
    Raises:
        ValueError: Jeśli podano datę w nieprawidłowym formacie
        
    Przykłady:
        >>> konwertuj_date("2023-12-31")
        '31.12.2023'
    """
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d")
        return data.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Nieprawidłowy format daty. Oczekiwano RRRR-MM-DD")

def czy_palindrom(tekst: str) -> bool:
    """
    Sprawdza czy podany tekst jest palindromem (czytany od tyłu jest taki sam).
    
    Args:
        tekst (str): Tekst do sprawdzenia
        
    Returns:
        bool: True jeśli tekst jest palindromem, False w przeciwnym przypadku
        
    Uwaga:
        - Ignoruje wielkość liter
        - Ignoruje znaki niebędące literami lub cyframi
        
    Przykłady:
        >>> czy_palindrom("Kajak")
        True
        >>> czy_palindrom("Python")
        False
    """
    przetworzony_tekst = ''.join(znak.lower() for znak in tekst if znak.isalnum())
    # Sprawdź czy tekst jest taki sam po odwróceniu
    return przetworzony_tekst == przetworzony_tekst[::-1]


# Przykłady użycia funkcji
if __name__ == "__main__":
    print("Czy 'test@domena.pl' to poprawny email?", sprawdz_email("test@domena.pl"))
    print("Pole prostokąta 5x7:", oblicz_pole_prostokata(5, 7))
    print("Parzyste liczby z [1, 2, 3, 4, 5, 6]:", filtruj_liczby_parzyste([1, 2, 3, 4, 5, 6]))
    print("Data 2023-05-15 w formacie europejskim:", konwertuj_date("2023-05-15"))
    print("Czy 'Kajak' to palindrom?", czy_palindrom("Kajak"))