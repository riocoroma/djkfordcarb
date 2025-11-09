# DjkFordibrid
Algoritmo cammini a costo minimo ideale per archi costi negativi,rileva cicli negativi,GRAFI POCO DENSI
Descrizione:
E' una variante originale dell’algoritmo di Dijkstra progettata per gestire archi con pesi negativi, purché non ci siano cicli negativi raggiungibili dalla sorgente. L’algoritmo combina un heap di priorità per selezionare i nodi con distanza minima stimata con rilassamenti multipli, permettendo di rilevare eventuali cicli negativi.

Caratteristiche principali

Gestisce grafi con archi negativi (a differenza del Dijkstra classico).

Rileva cicli negativi reali e segnala un errore se presenti.

Mantiene un comportamento heap-based, ottimizzando le estrazioni dei nodi minimi.

Ideale per grafi sparsi dove Bellman-Ford sarebbe corretto ma più lento.

Limitazioni

Non può calcolare cammini minimi se ci sono cicli negativi reali.

Complessità nel caso peggiore: 
𝑂(𝑉⋅𝐸log𝑉)
O(V⋅ElogV) → più lenta del Dijkstra classico.

Non è uno standard ufficiale, ma una variante originale ispirata a Dijkstra e Bellman-Ford.

<img width="636" height="246" alt="image" src="https://github.com/user-attachments/assets/e50bd894-86aa-446c-866c-14c7071edf97" />


