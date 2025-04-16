import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pymcdm.methods import TOPSIS, SPOTIS, VIKOR
from pymcdm.normalizations import minmax_normalization
from pymcdm.weights import entropy_weights

matrix = np.array([
    [3400, 3200, 8, 1.4, 512],
    [4200, 3600, 12, 1.7, 1024],
    [3900, 3100, 9, 1.5, 512],
    [4600, 4000, 11, 1.8, 2048]
])
alternatives = ['A1', 'A2', 'A3', 'A4']
criteria = ['Price (PLN)', 'Performance', 'Battery (h)', 'Weight (kg)', 'Storage (GB)']
types = np.array([-1, 1, 1, -1, 1])

#Wyznaczanie wagi
weights = entropy_weights(matrix)

#Normalizacja danych
norm_matrix = minmax_normalization(matrix)

#Uruchomienie metod decyzyjnych
bounds = np.column_stack((np.min(matrix, axis=0), np.max(matrix, axis=0)))
results = {
    'TOPSIS': TOPSIS()(norm_matrix, weights, types),
    'SPOTIS': SPOTIS(bounds)(matrix, weights, types),
    'VIKOR':  VIKOR()(norm_matrix, weights, types)
}

#Wyniki i ranking
df = pd.DataFrame(results, index=alternatives)
df['Rank_TOPSIS'] = df['TOPSIS'].rank(ascending=False).astype(int)
df['Rank_SPOTIS'] = df['SPOTIS'].rank(ascending=True).astype(int)
df['Rank_VIKOR']  = df['VIKOR'].rank(ascending=True).astype(int)

#Wyświetlenie wag i macierzy
print("\nMacierz decyzyjna:\n", pd.DataFrame(matrix, index=alternatives, columns=criteria))
print("\nWagi (metoda entropii):", np.round(weights, 4))

print("\nWyniki i rankingi:\n", df)

#Porównanie rankingów
df[['Rank_TOPSIS', 'Rank_SPOTIS', 'Rank_VIKOR']].plot(kind='bar')
plt.title('Porównanie rankingów metod MCDM')
plt.ylabel('Miejsce w rankingu (1 = najlepsze)')
plt.xticks(rotation=0)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
