import numpy as np
import matplotlib.pyplot as plt

t , p = np.loadtxt('pressione.dat', usecols=(0,1), unpack=True)

# Assumendo che tu abbia già gli array t (tempo) e p (pressione)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, p, '.-', markersize=3, label='Dati pressione')
ax.set_xlabel('Tempo t (s)')
ax.set_ylabel('Pressione (kPa)')
ax.grid(True)

print("Clicca INIZIO e FINE di ogni plateau (premi Tasto Centrale o INVIO quando hai finito):")
# n=-1 permette click infiniti finché non premi Invio; clicca a coppie (inizio, fine)
punti = plt.ginput(n=-1, timeout=0)

# Elabora le coppie di click (t_inizio, t_fine)
for i in range(0, len(punti), 2):
    t1, t2 = punti[i][0], punti[i+1][0]
    mask = (t >= t1) & (t <= t2)
    
    p_mean = np.mean(p[mask])
    p_std = np.std(p[mask], ddof=1)
    
    # Disegna il plateau trovato sul grafico per verifica visiva
    ax.hlines(p_mean, t1, t2, colors='red', linewidth=2.5)
    print(f"Plateau {i//2}: t in [{t1:.1f}, {t2:.1f}] s -> p = {p_mean:.4f} ± {p_std:.4f} kPa (N={np.sum(mask)} punti)")

plt.show()