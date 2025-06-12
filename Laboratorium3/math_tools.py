import math

def srednia_arytmetyczna(liczby: list[float]) -> float:
    """
    Oblicza średnią arytmetyczną z listy liczb.
    
    Args:
        liczby: Lista liczb
        
    Returns:
        float: Średnia arytmetyczna
        
    Raises:
        ValueError: Jeśli lista jest pusta
    """
    if not liczby:
        raise ValueError("Lista liczb nie może być pusta")
    return sum(liczby) / len(liczby)

def czy_pierwsza(liczba: int) -> bool:
    """
    Sprawdza czy liczba jest pierwsza.
    
    Args:
        liczba: Liczba do sprawdzenia
        
    Returns:
        bool: True jeśli liczba jest pierwsza, False w przeciwnym przypadku
    """
    if liczba < 2:
        return False
    for i in range(2, int(math.sqrt(liczba)) + 1):
        if liczba % i == 0:
            return False
    return True