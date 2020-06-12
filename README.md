# Structure-Learning-Bayesian-Network
Progetto sull'apprendimento della struttura di reti Bayesiane per l'esame di Intelligenza Artificiale.

## Riferimenti a fonti esterne
I riferimenti a fonti esterne possono essere consultati nel file **Structure_Learning_in_Bayesian_Network.pdf**.

## Utilizzo
Per riprodurre i test effettuati sarà sufficente eseguire il codice contenuto nel file **Main.py**, nella sezione omonima di questo file viene descritto in particolare la signature dei metodi chiamati.\
Breve descrizione dei vari file di progetto:

### BayesianNet.py
Questo file si occupa della generazione della rete Bayesiana e della sua **matrice di adiacenza** partendo da un modello.\
In questo caso viene utilizzato il modello *Alarm* contenuto nel file *Earthquake.py*.

### Dataset.py
In questa sezione del programma viene generato un **dataset pseudocasuale**.\
La classe omonima a questo file prende in input un oggetto di tipo *BayesianNet* e un numero di casi da generare.\
Il metodo `get_prob` si occupa di ritornare la probabilità che un evento si verifichi, in funzione del verificarsi o meno dei nodi da cui tale evento dipende.

### DFS.py
La funzione `dfs` si occupa dell'**ordinamento topologico** dei nodi della rete, in modo da impedire che un nodo venga analizzato prima dei suoi padri.

### Earthquake.py
Contiene il modello utilizzato per il test del codice.\
**Alarm** è un modello molto utilizzato nell'ambito delle reti Bayesiane.

### Main.py
Il file principale per l'eseguzione del programma.\
È possibile notare l'uso delle istanze necessarie al funzionamento del programma.\
L'apprendimento della struttura viene calcolato 1000 volte su dataset della dimentione di 150 righe, in modo da non appesantire i calcoli all'interno del metodo *k2*.\
Signatures dei metodi chiamati per eseguire il test di funzionamento:
* `BayesianNet()`: ritorna un istanza di rete Bayesiana.
* `Dataset(bn, num_cases)`: prende in input una rete bayesiana e un numero di test da effettuare, restituisce in output un oggetto di tipo Dataset da cui è possibile recuperare la matrice del dataset accedendo al campo `.dataset` dell'oggetto.
* `k2(data.dataset, data.ordered_array, 2)`: prende in input la matrice del dataset, una lista di nodi ordinati topologicamente, e un upper bound che identifica il numero massimo di padri che può avere ogni nodo. Rende in output la matrice di adiacenza del dag appreso.

### Node.py
Si occupa di identificare i **campi del nodo**:
* `.name`: nome del nodo.
* `.value`: identificativo univoco.
* `.pi`: insieme dei padri nel nodo.
* `.cpt`: vettore delle probabilità condizionate.
* `.domain_values`: dominio dei valori ammissibili per il nodo nel dataset.
* `.color`: colore, utile per l'ordinamento topologico.
* `.f`: tempo di fine scoperta, utile per l'ordinamento topologico.

### StructureLearning.py
Il cuore del progetto.\
Implementa la funzione **k2** per l'apprendimento della struttura: prendendo in input un *dataset*, un array contenente i *nodi* della rete, un *upper_bound* che identifica il numero massimo di padri che ogni nodo può avere.\
Il metodo *k2* ritorna un **dag** che rappresenta la struttura appresa, idealmente dovrebbe coincidere con la matrice di adiacenza del modello scelto; in pratica tale algoritmo non è perfetto e può riportare alcuni archi in eccesso e/o in difetto.
