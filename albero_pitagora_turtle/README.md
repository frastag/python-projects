# Albero di Pitagora con Turtle

Uno script Python che disegna un albero frattale ricorsivo (simile all'albero di Pitagora) usando il modulo `turtle`.

## Come funziona

Lo script disegna un ramo, poi si ramifica in due rami più corti (sinistro e destro), ognuno dei quali si ramifica a sua volta, fino a raggiungere il livello 0. Ad ogni livello il colore del tratto sfuma dal marrone al verde, per dare l'idea di un tronco che si trasforma in chioma.

Parametri principali della funzione `albero`:

- `lunghezza`: lunghezza del ramo corrente
- `livello`: numero di ramificazioni rimanenti (la ricorsione si ferma a `livello == 0`)
- `angolo`: angolo di apertura tra i due rami figli (default 35°)

Ad ogni chiamata ricorsiva la lunghezza del ramo si riduce al 75% di quella precedente.

## Requisiti

- Python 3
- Il modulo `turtle` (incluso nella libreria standard di Python)

## Esecuzione

```bash
python3 albero_pitagora_turtle.py
```

Si aprirà una finestra grafica con sfondo nero che disegna l'albero. Clicca sulla finestra per chiuderla.

## Personalizzazione

Nel file `albero_pitagora_turtle.py` puoi modificare la chiamata finale:

```python
albero(t, 100, 10)
```

- Il primo valore (`100`) è la lunghezza iniziale del ramo.
- Il secondo valore (`10`) è il numero di livelli di ricorsione (più alto = albero più dettagliato, ma più lento da disegnare).

Puoi anche passare un valore diverso di `angolo` per cambiare la forma dell'albero, ad esempio `albero(t, 100, 10, angolo=25)`.