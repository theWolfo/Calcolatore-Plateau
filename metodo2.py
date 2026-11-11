import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
t , p = np.loadtxt('pressione.dat', usecols=(0,1), unpack=True)

# Calcola la deviazione standard mobile su una finestra di 15 punti (1.5 secondi a 10 Hz)
finestra = 15
soglia_rumore = 0.03  # in kPa (aggiustala se serve: più è bassa, più è selettiva)

rolling_std = pd.Series(p).rolling(window=finestra, center=True).std()
is_flat = rolling_std < soglia_rumore

# Identifica i blocchi continui di punti piatti (lunghi almeno 20 punti = 2 secondi)
gruppi = (is_flat != is_flat.shift()).cumsum()
plt.figure(figsize=(10, 5))
plt.plot(t, p, color='lightgray', label='Dati grezzi')

step_num = 0
for _, idx_group in pd.Series(t).groupby(gruppi):
    indices = idx_group.index
    if is_flat.iloc[indices[0]] and len(indices) >= 20:
        t_plat = t[indices]
        p_plat = p[indices]
        plt.plot(t_plat, p_plat, '.', label=f'Plateau {step_num}: {np.mean(p_plat):.3f} kPa')
        step_num += 1

plt.xlabel('Tempo (s)')
plt.ylabel('Pressione (kPa)')
plt.legend()
plt.grid(True)
plt.show()