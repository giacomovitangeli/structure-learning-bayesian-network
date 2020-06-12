# Structure-Learning-Bayesian-Network
Progetto sull'apprendimento della struttura di reti Bayesiane per l'esame di Intelligenza Artificiale.

## Riferimenti a fonti esterne
I riferimenti a fonti esterne possono essere consultati nel file *Structure_Learning_in_Bayesian_Network.pdf*.

## Utilizzo
Per utilizzare il codice sarà sufficente eseguire il codice contenuto nel file *Main.py*.
Breve descrizione dei vari file di progetto:

### BayesianNet.py
Questo file si occupa della generazione della rete Bayesiana e della sua **matrice di adiacenza** partendo da un modello.
In questo caso viene utilizzato il modello *Alarm* contenuto nel file *Earthquake.py*.

### Dataset.py
In questa sezione del programma viene generato un **dataset pseudocasuale**.
La classe omonima a questo file prende in input un oggetto di tipo *BayesianNet* e un numero di casi da generare.
Il metodo `get_prob` si occupa di ritornare la probabilità che un evento si verifichi, in funzione del verificarsi o meno dei nodi da cui tale evento dipende.

### DFS.py
La funzione `dfs` si occupa dell'**ordinamento topologico** dei nodi della rete, in modo da impedire che un nodo venga analizzato prima dei suoi padri.

### Earthquake.py
Contiene il modello utilizzato per il test del codice. 
**Alarm** è un modello molto utilizzato nell'ambito delle reti Bayesiane.

### Main.py
Il file principale per l'eseguzione del programma. 
È possibile notare l'uso delle istanze necessarie al funzionamento del programma.
L'apprendimento della struttura viene calcolato 1000 volte su dataset della dimentione di 150 righe, in modo da non appesantire i calcoli all'interno del metodo *k2*.

### Node.py
Si occupa di identificare i **campi del nodo**:
* `name`: nome del nodo.
* `value`: identificativo univoco.
* `pi`: insieme dei padri nel nodo.
* `cpt`: vettore delle probabilità condizionate.
* `domain_values`: dominio dei valori ammissibili per il nodo nel dataset.
* `color`: colore, utile per l'ordinamento topologico.
* `f`: tempo di fine, utile per l'ordinamento topologico.

### StructureLearning.py
Il cuore del progetto. 
Implementa la funzione **k2** per l'apprendimento della struttura: prendendo in input un *dataset*, un array contenente i *nodi* della rete, un *upper_bound* che identifica il numero massimo di padri che ogni nodo può avere.
Il metodo *k2* ritorna un **dag** che rappresenta la struttura appresa, idealmente dovrebbe coincidere con la matrice di adiacenza del modello scelto; in pratica tale algoritmo non è perfetto e può riportare alcuni archi in eccesso e/o in difetto.
