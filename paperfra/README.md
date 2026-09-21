# Papera Frattale 🦆

Uno script Python che disegna una papera stilizzata usando `turtle`, dove **ogni forma è costruita con tecniche frattali ricorsive**:

- **Corpo, testa e becco**: contorni generati applicando la **curva di Koch** (la stessa alla base del fiocco di neve di Koch) ai lati di un poligono/ellisse.
- **Zampe e coda**: rami generati con la stessa logica ricorsiva dell'**albero di Pitagora** (ogni ramo si divide in due più piccoli).
- **Occhio**: unico elemento non frattale, un semplice cerchio pieno.

## Requisiti

- Python 3.x
- Il modulo `turtle` (incluso nella libreria standard di Python)

## Come eseguirlo

```bash
python paperfra.py
```

Si aprirà una finestra grafica che mostra la papera disegnarsi passo per passo. Clicca sulla finestra per chiuderla a disegno completato.

## Struttura del codice

| Funzione | Cosa fa |
|---|---|
| `punto_koch(p1, p2, ordine)` | Genera ricorsivamente i punti di un segmento "frattale" (curva di Koch) tra due punti |
| `poligono_frattale(vertici, ordine)` | Applica la curva di Koch a ogni lato di un poligono chiuso |
| `vertici_ellisse(cx, cy, rx, ry, lati)` | Calcola i vertici di un'ellisse (o cerchio) approssimata a poligono |
| `disegna_forma(t, punti, colore)` | Disegna e riempie una forma chiusa a partire da una lista di punti |
| `disegna_corpo` / `disegna_testa` / `disegna_becco` | Costruiscono le parti principali della papera usando ellissi/triangoli con contorno frattale |
| `disegna_macchia` | Disegna la macchia chiara sul corpo (contorno liscio, non frattale) |
| `disegna_occhio` | Disegna l'occhio come cerchio pieno semplice |
| `ramo_pitagora(t, lunghezza, livello, angolo)` | Disegna ricorsivamente un ramo che si biforca in due, secondo la logica dell'albero di Pitagora |
| `disegna_zampe` / `disegna_coda` | Usano `ramo_pitagora` per generare zampe e coda in nero |
| `crea_schermo` / `crea_turtle` | Impostano finestra grafica e turtle (colori, velocità, aggiornamento a ogni passo) |
| `main` | Orchestra il disegno completo, nell'ordine corretto (dal basso verso l'alto) |

## Parametri regolabili

- **`ordine`** (in `poligono_frattale`): livello di ricorsione della curva di Koch. Valori più alti = bordi più frastagliati.
    - `ordine=1`: bordo leggermente ondulato (usato per il becco)
    - `ordine=2`: bordo più marcatamente frattale (usato per corpo e testa)
- **`livello`** (in `ramo_pitagora`): profondità di ricorsione dei rami di zampe/coda. Valori più alti = più diramazioni.
- **`t.speed()`** e **`screen.tracer()`** (in `crea_turtle`/`crea_schermo`): controllano quanto velocemente si vede disegnare la papera. Utile da rallentare per registrazioni/reel.

## Personalizzazione

I colori sono definiti come costanti all'inizio del file (`COLORE_CORPO`, `COLORE_TESTA`, `COLORE_BECCO`, ecc.) e possono essere modificati liberamente per ottenere varianti diverse della papera.