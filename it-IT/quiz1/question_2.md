--- question ---
---
legend: Domanda 2 di 3
---

In questo progetto hai usato la generazione procedurale — il computer crea e posiziona parti del tuo mondo per te. Anche se farlo fa risparmiare molto tempo, soprattutto se stai creando livelli molto grandi, può creare alcuni problemi. A quali di questi problemi dovresti prestare attenzione quando testi la tua generazione procedurale?

--- choices ---

- (x) A tutti loro

  --- feedback ---

Corretto! Tutto ciò può accadere quando si utilizza la generazione procedurale. Puoi aggiungere altro codice per verificare e risolvere questi problemi o anche provare diverse seeds finché non ne trovi una che funzioni.

  --- /feedback ---

- ( ) Potrebbero essere generati ostacoli che lasciano il giocatore senza percorso da seguire.

  --- feedback ---

Non proprio. Ciò può accadere con ostacoli generati proceduralmente, in particolare all'avvio del gioco.


**Suggerimento:** Potresti aggirare questo problema impedendo che gli ostacoli appaiano troppo vicini alla posizione iniziale del giocatore. Ti vengono in mente altre soluzioni?

  --- /feedback ---

- ( ) Gli ostacoli appaiono direttamente sotto il giocatore.

  --- feedback ---

Non proprio. Ciò può accadere sia all'inizio del gioco, sia quando vengono aggiunti nuovi ostacoli all'aumentare del livello di difficoltà, se capita che scelgano una posizione vicina a quella del giocatore.


**Suggerimento:** Una potenziale soluzione potrebbe essere quella di rendere il giocatore temporaneamente immune alla collisione con tutti gli ostacoli, o anche solo con quelli appena creati, per un breve periodo dopo un aumento di livello. Quali problemi potrebbe creare la scelta di una nuova posizione dell'ostacolo se fosse troppo vicino al giocatore?

  --- /feedback ---

- ( ) Gli ostacoli sono tutti raggruppati insieme, lasciando troppo spazio aperto altrove.

  --- feedback ---

Non proprio. La generazione casuale può scegliere gruppi di numeri vicini tra loro, questo può essere un problema.


**Suggerimento:** Una soluzione potrebbe essere quella di passare alla generazione semi-casuale — dividi lo schermo in pezzi e usa numeri casuali per generare ostacoli all'interno di ciascuno di questi pezzi. Riesci a pensare a come potresti utilizzare questo tipo di generazione procedurale per rendere il tuo gioco più interessante o più impegnativo?

  --- /feedback ---

--- /choices ---

--- /question ---
