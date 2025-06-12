import pandas as pd
import matplotlib.pyplot as plt

#Użycie Pandas
print("\n--- PRZYKŁADY PANDAS ---\n")

#Tworzenie DataFrame
data = {
    'Imię': ['Anna', 'Jan', 'Maria', 'Piotr'],
    'Wiek': [25, 32, 28, 41],
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław']
}
df = pd.DataFrame(data)

#Wyświetlenie
print("Pełne dane:")
print(df)

#Statystyki
print("\nStatystyki wieku:")
print(df['Wiek'].describe())

#Filtrowanie danych
print("\nOsoby powyżej 30 lat:")
print(df[df['Wiek'] > 30])

#Sortowanie
print("\nPosortowane według wieku:")
print(df.sort_values('Wiek'))

#Zapis do pliku CSV
df.to_csv('dane_osobowe.csv', index=False)
print("\nDane zapisane do pliku 'dane_osobowe.csv'")

#Użycie Matplotlib
print("\n--- PRZYKŁADY MATPLOTLIB ---\n")

#Wykres liniowy
lata = [2015, 2016, 2017, 2018, 2019, 2020]
sprzedaz = [120, 145, 160, 175, 200, 210]

plt.figure(figsize=(10, 5))
plt.plot(lata, sprzedaz, marker='o', linestyle='--', color='b', label='Sprzedaż')
plt.title('Sprzedaż w latach 2015-2020')
plt.xlabel('Rok')
plt.ylabel('Sprzedaż (w tys.)')
plt.grid(True)
plt.legend()
plt.savefig('sprzedaz.png')
print("Wykres liniowy zapisany jako 'sprzedaz.png'")

#Wykres słupkowy
plt.figure(figsize=(8, 4))
plt.bar(df['Imię'], df['Wiek'], color='green')
plt.title('Wiek osób w grupie')
plt.xlabel('Imię')
plt.ylabel('Wiek')
plt.savefig('wiek.png')
print("Wykres słupkowy zapisany jako 'wiek.png'")
plt.show()