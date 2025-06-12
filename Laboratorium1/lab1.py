import math

# Funkcja zip() łączy elementy z dwóch lub więcej iterowalnych obiektów 
# (np. list, krotek) w pary. Zwraca obiekt zip, który można przekonwertować na listę lub inny typ.
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))  #https://docs.python.org/3/library/functions.html#zip
print("Zipped lists:", zipped)

#Moduł Math
digit = 16
square_root = math.sqrt(digit)
print(f"Square root of  {digit}: {square_root}")

# Błąd ZeroDivisionError występuje gdy próbujemy podzielić liczbę przez zero. 
try:
    result = 10 / 0  #https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
