import turtle
import math

# Colori ripresi dal disegno di riferimento della papera
COLORE_CORPO = "#e0982e"
COLORE_TESTA = "#e0982e"
COLORE_MACCHIA = "#ffca6b"
COLORE_BECCO = "#3f8546"
COLORE_CONTORNO = "#1e1f22"
COLORE_OCCHIO = "#1e1f22"


def punto_koch(p1, p2, ordine):
    """Punti di un segmento 'frattale' (curva di Koch) tra p1 e p2.

    Ogni segmento viene diviso in 3 parti uguali; sulla parte centrale
    viene costruita una 'gobba' triangolare equilatera, e lo stesso
    procedimento si ripete ricorsivamente sui 4 nuovi segmenti generati,
    finché non si raggiunge il caso base (ordine == 0)."""
    if ordine == 0:
        # Caso base della ricorsione: nessuna suddivisione,
        # il segmento resta una semplice linea retta
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2
    # Divido il segmento in tre parti uguali
    dx, dy = (x2 - x1) / 3, (y2 - y1) / 3

    # Punti che segnano il primo e il secondo terzo del segmento
    pa = (x1 + dx, y1 + dy)
    pb = (x1 + 2 * dx, y1 + 2 * dy)

    # Calcolo il punto di "picco" del triangolino centrale,
    # ruotando di 60° la direzione tra pa e pb
    angolo = math.atan2(pb[1] - pa[1], pb[0] - pa[0]) - math.radians(60)
    lato = math.hypot(pb[0] - pa[0], pb[1] - pa[1])
    picco = (pa[0] + lato * math.cos(angolo), pa[1] + lato * math.sin(angolo))

    # Applico ricorsivamente la stessa suddivisione ai 4 nuovi segmenti
    # (p1-pa, pa-picco, picco-pb, pb-p2), concatenando i punti risultanti
    punti = []
    for a, b in [(p1, pa), (pa, picco), (picco, pb), (pb, p2)]:
        punti.extend(punto_koch(a, b, ordine - 1)[:-1])
    punti.append(p2)
    return punti


def poligono_frattale(vertici, ordine):
    """Applica la curva di Koch a ogni lato di un poligono chiuso,
    trasformando ogni lato dritto in un contorno frastagliato."""
    punti = []
    n = len(vertici)
    for i in range(n):
        # Prendo ogni coppia di vertici consecutivi (l'ultimo si ricollega al primo)
        p1, p2 = vertici[i], vertici[(i + 1) % n]
        punti.extend(punto_koch(p1, p2, ordine)[:-1])
    return punti


def vertici_ellisse(cx, cy, rx, ry, lati):
    """Genera i vertici di un'ellisse (o cerchio, se rx == ry)
    centrata in (cx, cy), approssimata con un poligono di N lati."""
    return [
        (cx + rx * math.cos(2 * math.pi * i / lati),
         cy + ry * math.sin(2 * math.pi * i / lati))
        for i in range(lati)
    ]


def disegna_forma(t, punti, colore):
    """Disegna e riempie una forma chiusa a partire da una lista di punti."""
    t.penup()
    t.goto(punti[0])  # mi sposto al primo punto senza tracciare
    t.pendown()
    t.fillcolor(colore)
    t.pencolor(COLORE_CONTORNO)
    t.pensize(2)
    t.begin_fill()
    for p in punti[1:]:
        t.goto(p)  # collego i punti in sequenza
    t.goto(punti[0])  # richiudo la forma tornando al punto di partenza
    t.end_fill()


def disegna_corpo(t):
    # Il corpo è un'ellisse (ovale orizzontale) con contorno frattale
    vertici = vertici_ellisse(cx=-10, cy=0, rx=95, ry=48, lati=10)
    punti = poligono_frattale(vertici, ordine=2)
    disegna_forma(t, punti, COLORE_CORPO)


def disegna_macchia(t):
    # Macchia chiara sul corpo: qui il contorno resta liscio (nessuna curva di Koch)
    vertici = vertici_ellisse(cx=-55, cy=10, rx=25, ry=15, lati=10)
    disegna_forma(t, vertici, COLORE_MACCHIA)  # macchia liscia, non frattale


def disegna_testa(t):
    # La testa è un cerchio (rx == ry) con lo stesso trattamento frattale del corpo
    vertici = vertici_ellisse(cx=65, cy=30, rx=45, ry=45, lati=10)
    punti = poligono_frattale(vertici, ordine=2)
    disegna_forma(t, punti, COLORE_TESTA)


def disegna_becco(t):
    # Il becco è un triangolo i cui lati vengono resi frattali con ordine basso
    # (per restare riconoscibile come triangolo, non troppo frastagliato)
    vertici = [(100, 40), (100, 18), (145, 29)]
    punti = poligono_frattale(vertici, ordine=1)
    disegna_forma(t, punti, COLORE_BECCO)


def disegna_occhio(t):
    # Occhio: semplice cerchio pieno, disegnato con la primitiva di turtle
    # (nessuna suddivisione frattale, per restare pulito e leggibile)
    t.penup()
    t.goto(70, 55)
    t.pendown()
    t.pensize(1)
    t.fillcolor(COLORE_OCCHIO)
    t.pencolor(COLORE_OCCHIO)
    t.begin_fill()
    t.circle(10, steps=30)  # steps alto = cerchio ben arrotondato anche se piccolo
    t.end_fill()


def ramo_pitagora(t, lunghezza, livello, angolo=30):
    """Stessa logica dell'albero di Pitagora: un ramo che si divide in due
    più piccoli, ricorsivamente, finché non arriva al caso base."""
    if livello == 0:
        # Caso base: livello 0 significa "nessun ramo da disegnare", mi fermo
        return

    t.forward(lunghezza)  # disegno il tronco/ramo attuale
    pos = t.pos()          # salvo posizione...
    head = t.heading()     # ...e orientamento, per poterci tornare dopo

    # Ramo verso sinistra, più corto del precedente (lunghezza * 0.7)
    t.left(angolo)
    ramo_pitagora(t, lunghezza * 0.7, livello - 1, angolo)

    # Torno al punto di diramazione e disegno il ramo verso destra
    t.setpos(pos)
    t.setheading(head)
    t.right(angolo)
    ramo_pitagora(t, lunghezza * 0.7, livello - 1, angolo)

    # Torno indietro (backtracking) per lasciare la turtle
    # nello stato in cui era prima di disegnare questo ramo
    t.setpos(pos)
    t.setheading(head)
    t.backward(lunghezza)


def disegna_zampe(t):
    # Le zampe sono due piccoli "alberi di Pitagora" neri,
    # posizionati sul bordo inferiore del corpo
    t.pencolor("black")
    t.pensize(2)

    # zampa sinistra
    t.penup()
    t.goto(-25, -47)
    t.setheading(-90)  # punta verso il basso
    t.pendown()
    ramo_pitagora(t, lunghezza=12, livello=3, angolo=35)

    # zampa destra
    t.penup()
    t.goto(10, -47)
    t.setheading(-90)
    t.pendown()
    ramo_pitagora(t, lunghezza=12, livello=3, angolo=35)


def disegna_coda(t):
    # La coda è un altro ramo frattale, orientato verso l'alto-sinistra,
    # con un livello di ricorsione leggermente più alto delle zampe
    t.pencolor("black")
    t.pensize(2)

    t.penup()
    t.goto(-100, 5)
    t.setheading(160)  # verso sinistra e leggermente in alto
    t.pendown()
    ramo_pitagora(t, lunghezza=14, livello=4, angolo=28)


def crea_schermo():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.tracer(1)  # aggiorna lo schermo a ogni passo, per vedere il disegno crescere
    return screen


def crea_turtle():
    t = turtle.Turtle()
    t.speed(6)  # velocità moderata: visibile ma non troppo lenta
    return t


def main():
    screen = crea_schermo()
    t = crea_turtle()

    # Ordine di disegno: prima gli elementi "sotto" (corpo, zampe, coda),
    # poi quelli sopra (macchia, testa, becco, occhio)
    disegna_corpo(t)
    disegna_zampe(t)
    disegna_coda(t)
    disegna_macchia(t)
    disegna_testa(t)
    disegna_becco(t)
    disegna_occhio(t)

    t.hideturtle()  # nascondo il cursore a forma di freccia a fine disegno
    screen.exitonclick()  # la finestra resta aperta finché non si clicca


if __name__ == "__main__":
    main()