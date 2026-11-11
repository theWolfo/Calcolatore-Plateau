# Calcolatore-Plateau
Allora

questi programmi python permettono di visualizzare e calcolare i plateau delle pressioni

- tramite plateau.py si può semplicemente graficare il plateau
- tramite metodo1.py si possono calcolare manualmente i plateau
    * per farlo fare 1 click col mouse all'inizio del plateau e 1 click alla fine (dovrebbero apparire due crocette rosse, rispettivamente all'inizio e alla fine)
    * ripetere per ogni plateau
    * una volta che sono stati segnati tutti i plateau premere INVIO e il programma stamperà sul terminale gli intervalli di tempo designati con relativa media della pressione
    * ! il programma traccerà una retta parallela all'asse delle ascisse basandosi sui punti che gli avete segnato come inzio e fine del plateau, cercate di essere precisi
- tramite metodo2.py il programma cerca automaticamente i plateau derivando la curva
    * ! potrebbe sbagliare visto che le curve non sono perfette
    * ! non rilascia gli intervalli di tempo, solo la pressione calcolata per il plateau, per prendere il tempo guardare la componente x della curva portando il cursore sul un punto del grafico.

Per far funzionare i programmi bisogna incolare tutti i dati interessati in pressione.dat con il tempo in secondi sulla prima colonna e la pressione in kPa sulla seconda

! Attenzione che i separatori decimali siano con i . e non con le , visto che python riconosce solo i primi
Per lanciare i programmi scrivere sul terminale `python3 nome_file.py` e premete invio
