def odwroc_tekst(tekst: str) -> str:
    """
    Odwraca kolejność znaków w tekście.
    
    Args:
        tekst: Tekst do odwrócenia
        
    Returns:
        str: Odwrócony tekst
    """
    return tekst[::-1]

def czy_palindrom(tekst: str) -> bool:
    """
    Sprawdza czy tekst jest palindromem (ignoruje wielkość liter i znaki niealfanumeryczne).
    
    Args:
        tekst: Tekst do sprawdzenia
        
    Returns:
        bool: True jeśli tekst jest palindromem, False w przeciwnym przypadku
    """
    przetworzony = ''.join(c.lower() for c in tekst if c.isalnum())
    return przetworzony == przetworzony[::-1]