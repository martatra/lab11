# Laboratorio 11
In questo laboratorio si svolgono esercizi su algoritmi e strutture dati.


## Esercizio 1
Scrivere una funzione ricorsiva che crei un [quadrato magico](https://it.wikipedia.org/wiki/Quadrato_magico) di dimensioni specificate dal programmatore (*N x N*, *N >= 3*).
Un quadrato magico di dimensione *N x N* è un quadrato in cui sono disposti tutti i numeri da *1* a *N^2*, senza ripetizioni.
La somma dei numeri su ogni riga colonna o diagonale deve essere la stessa.
La ricorsione deve fermarsi quando si trova la prima configurazione corretta.

Scrivere una seconda versione che controlli, ogni volta che un numero viene aggiunto, se
la regola magica e stata violata. In caso affermativo non si prosegua con la ricerca per quella
configurazione parziale. Il controllo deve verificare che nessuna riga, colonna o diagonale
abbia una somma diversa dalla costante magica, nel caso in cui sia completa, o maggiore uguale
della stessa, nel caso in cui manchino dei valori. La constante magica è pari a n(n^2 + 1)/2.

Testare a partendo da *N=3*, qual è la dimensione massima del quadrato che si riesce a generare, in tempi ragionevoli, con la prima versione?
E con la seconda versione?


## Esercizio 2
Scrivere la classe che permetta di rappresentare il grafo di una metropolitana.
I nodi del grafo sono le stazioni della metropolitana e i rami le connessioni tra stazioni.

Ogni stazione è identificata univocamente da un nome,
mentre una connessione ha come proprietà il nome della linea che effettua la connessione e il tempo di percorrenza in minuti.
Tra due stazioni adiacenti si assuma che ci sia soltanto una linea che le colleghi, e che la connessione sia bidirezionale.

Il grafo è pertanto **INDIRETTO** e **PESATO**.

La classe deve fornire metodi per:
- aggiungere una stazione dato il nome, lanciando un'eccezione se già presente
- controllare se una stazione è già presente
- aggiungere una connessione dati i nomi delle due stazioni, lanciando un'eccezione se già presente.
- ottenere le informazioni di una connessione tra due stazioni, restituendo ```None``` se non esiste.

Definire l'appropriata gerarchia di eccezioni per gestire i casi indicati.

Il file *data/london.csv* descrive la [metropolitana di Londra](https://content.tfl.gov.uk/standard-tube-map.pdf).
Ogni riga riporta i nomi di due stazioni, la linea che le congiunge e il tempo di percorrenza.
Tutti questo campi sono separati da punto e virgola ```;```.
Il file può contenere più connessioni tra la stesse due stazioni.

Scrivere ```@classmethod``` che, ottenuto il nome di un file con questo formato,
restituisca un istanza della classe rappresentante il grafo della metropolitana descritto nel file.
Se sono presenti connessioni multiple tra due stazioni, considerare unicamente la prima letta.
Utilizzare i metodi descritti sopra per fare i controlli e popolare il grafo.


## Esercizio 3
Creare una classe che erediti da quella sviluppata nel punto precedente e aggiunga un metodo che,
forniti i nomi di due stazioni, trovi un percorso tra di esse.
Il metodo deve restituire due valori:
- una lista ordinata che rappresentanti tutte le stazioni attraversate e le linee prese in ciascuna stazione
- il tempo totale impiegato per il percorso

Utilizzare l'algoritmo di esplorazione che si preferisce.
Qual è quello che restituisce il risultato migliore? Perché?

La [mappa della metropolitana di Londra](https://content.tfl.gov.uk/standard-tube-map.pdf)
può essere utile per controllare i risultati.
