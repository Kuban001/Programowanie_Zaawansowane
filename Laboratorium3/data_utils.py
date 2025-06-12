from typing import Any

def polacz_slowniki(slownik1: dict, slownik2: dict) -> dict:
    """
    Łączy dwa słowniki w jeden (w przypadku kolizji kluczy, wartości z drugiego słownika nadpisują pierwszy).
    
    Args:
        slownik1: Pierwszy słownik
        slownik2: Drugi słownik
        
    Returns:
        dict: Połączony słownik
    """
    return {**slownik1, **slownik2}

def filtruj_liste(lista: list[Any], warunek) -> list[Any]:
    """
    Filtruje listę według podanego warunku.
    
    Args:
        lista: Lista do przefiltrowania
        warunek: Funkcja określająca warunek filtracji
        
    Returns:
        list: Przefiltrowana lista
    """
    return [element for element in lista if warunek(element)]