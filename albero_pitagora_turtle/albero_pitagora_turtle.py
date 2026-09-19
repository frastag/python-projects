import turtle

def albero(t, lunghezza, livello, angolo=35):
    if livello == 0:
        return

    # colore che sfuma dal marrone al verde salendo nei livelli
    t.pencolor(0.5 - livello * 0.03, 0.3 + livello * 0.06, 0.1)
    t.pensize(livello * 0.6)

    t.forward(lunghezza)
    pos = t.pos()
    head = t.heading()

    # ramo sinistro
    t.left(angolo)
    albero(t, lunghezza * 0.75, livello - 1, angolo)

    # torna al punto e ramo destro
    t.setpos(pos)
    t.setheading(head)
    t.right(angolo)
    albero(t, lunghezza * 0.75, livello - 1, angolo)

    # torna indietro (per il disegno ricorsivo)
    t.setpos(pos)
    t.setheading(head)
    t.backward(lunghezza)

def crea_schermo():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.tracer(5)  # velocizza il rendering, utile per i reel
    return screen

def crea_turtle():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -250)
    t.pendown()
    return t

def main():
    screen = crea_schermo()
    t = crea_turtle()

    albero(t, lunghezza=100, livello=10)

    screen.exitonclick()

if __name__ == "__main__":
    main()
