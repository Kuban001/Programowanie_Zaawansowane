import re
from datetime import datetime
from typing import List, Union, Optional

class DataValidator:
    """Klasa zawierająca narzędzia do walidacji danych"""
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Sprawdza poprawność formatu adresu email
        
        Args:
            email (str): Adres email do walidacji
            
        Returns:
            bool: True jeśli email jest poprawny, False w przeciwnym przypadku
            
        Examples:
            >>> DataValidator.is_valid_email("test@example.com")
            True
            >>> DataValidator.is_valid_email("niepoprawny.email")
            False
        """
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.fullmatch(email_pattern, email))

class MathOperations:
    """Klasa zawierająca podstawowe operacje matematyczne"""
    
    @staticmethod
    def calculate_rectangle_area(width: float, height: float) -> float:
        """
        Oblicza pole prostokąta o podanych wymiarach
        
        Args:
            width (float): Szerokość prostokąta (musi być dodatnia)
            height (float): Wysokość prostokąta (musi być dodatnia)
            
        Returns:
            float: Obliczone pole prostokąta
            
        Raises:
            ValueError: Jeśli któryś z wymiarów jest ujemny
            
        Examples:
            >>> MathOperations.calculate_rectangle_area(3, 4)
            12
        """
        if width < 0 or height < 0:
            raise ValueError("Wymiary muszą być dodatnie")
        return width * height

class ListOperations:
    """Klasa zawierająca operacje na listach"""
    
    @staticmethod
    def filter_even_numbers(numbers: List[Union[int, float]]) -> List[int]:
        """
        Filtruje parzyste liczby całkowite z listy
        
        Args:
            numbers (List[Union[int, float]]): Lista liczb do filtracji
            
        Returns:
            List[int]: Lista zawierająca tylko parzyste liczby całkowite
            
        Examples:
            >>> ListOperations.filter_even_numbers([1, 2, 3, 4, 5.5])
            [2, 4]
        """
        return [num for num in numbers if isinstance(num, int) and num % 2 == 0]

class DateFormatter:
    """Klasa do konwersji formatów dat"""
    
    @staticmethod
    def convert_iso_to_dmy(iso_date: str) -> str:
        """
        Konwertuje datę z formatu ISO (YYYY-MM-DD) na format europejski (DD.MM.YYYY)
        
        Args:
            iso_date (str): Data w formacie RRRR-MM-DD
            
        Returns:
            str: Data w formacie DD.MM.RRRR
            
        Raises:
            ValueError: Jeśli podano datę w nieprawidłowym formacie
            
        Examples:
            >>> DateFormatter.convert_iso_to_dmy("2023-05-15")
            '15.05.2023'
        """
        try:
            date_obj = datetime.strptime(iso_date, "%Y-%m-%d")
            return date_obj.strftime("%d.%m.%Y")
        except ValueError as e:
            raise ValueError(f"Nieprawidłowy format daty: {iso_date}") from e

class TextAnalyzer:
    """Klasa zawierająca narzędzia do analizy tekstu"""
    
    @staticmethod
    def is_palindrome(text: str) -> bool:
        """
        Sprawdza czy tekst jest palindromem (czytany od przodu i tyłu jest taki sam)
        
        Args:
            text (str): Tekst do sprawdzenia
            
        Returns:
            bool: True jeśli tekst jest palindromem, False w przeciwnym przypadku
            
        Notes:
            - Ignoruje wielkość liter
            - Ignoruje znaki nie-alphanumeryczne
            
        Examples:
            >>> TextAnalyzer.is_palindrome("Kajak")
            True
            >>> TextAnalyzer.is_palindrome("Python")
            False
        """
        cleaned = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned == cleaned[::-1]


#Przykłady użycia
if __name__ == "__main__":
    #Test walidacji emaila
    print("Czy 'test@example.com' to poprawny email?", DataValidator.is_valid_email("test@example.com"))
    
    #Test obliczania pola prostokąta
    try:
        print("Pole prostokąta 3x4:", MathOperations.calculate_rectangle_area(3, 4))
    except ValueError as e:
        print("Błąd:", e)
    
    #Test filtracji liczb parzystych
    print("Parzyste liczby z [1, 2, 3, 4]:", ListOperations.filter_even_numbers([1, 2, 3, 4]))
    
    #Test konwersji daty
    try:
        print("Data 2023-05-15 w formacie DMY:", DateFormatter.convert_iso_to_dmy("2023-05-15"))
    except ValueError as e:
        print("Błąd:", e)
    
    #Test palindromu
    print("Czy 'Kajak' to palindrom?", TextAnalyzer.is_palindrome("Kajak"))