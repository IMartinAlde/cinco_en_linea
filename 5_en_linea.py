import gamelib

X_0 = 0
Y_0 = 50
X_MAX = 250
Y_MAX = 300
LADO = 25

CIRCULO = 'O'
CRUZ = 'X'
VACIO = ' '

def juego_crear():
    """Inicializar el estado del juego"""
    inicio = []
    for i in range(10):
        fila = []
        for j in range(10):
            fila.append(VACIO)
        inicio.append(fila)
    return inicio

def decidir_turno(juego):
    """Devuelve el símbolo correspondiente al jugador al cual
    le toca jugar."""
    contador_X = 0
    contador_O = 0

    for i in range(10):
        for j in range(10):
            if juego[i][j] == CRUZ:
                contador_X += 1
            elif juego[i][j] == CIRCULO:
                contador_O += 1

    if contador_O == contador_X:
        return CIRCULO
    else:
        return CRUZ

def juego_actualizar(juego, x, y):
    """Actualizar el estado del juego

    x e y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    turno = decidir_turno(juego)

    for i in range(10):
        inf_x = X_0 + LADO*i
        for j in range(10):
            inf_y = Y_0 + LADO*j
            if (inf_x < x <= inf_x + LADO) and (inf_y < y <= inf_y + LADO) and juego[j][i] == VACIO:
                juego[j][i] = turno

    return juego

def juego_mostrar(juego):
    """Actualizar la ventana"""
    gamelib.draw_text('5 EN LÍNEA', 125, 15, fill = 'white', size = 15)
    gamelib.draw_text('Es el turno de: ', 110, 35, fill = 'white', size = 12)

    if decidir_turno(juego) == CIRCULO:
        gamelib.draw_text(CRUZ, 170, 35, fill = 'black', size = 12)
        gamelib.draw_text(CIRCULO, 170, 35, fill = 'white', size = 12)
    else:
        gamelib.draw_text(CIRCULO, 170, 35, fill = 'black', size = 12)
        gamelib.draw_text(CRUZ, 170, 35, fill = 'white', size = 12)

    for i in range(11):
        gamelib.draw_line(X_0, Y_0 + i*LADO, X_MAX, Y_0 + i*LADO) #Rectas horizontales
        gamelib.draw_line(X_0 + i*LADO, Y_0, X_0 + i*LADO, Y_MAX) #Rectas verticales

    for i in range(10):
        centro_x = (LADO + 2*(X_0 + LADO*i))/2
        for j in range(10):
            centro_y = (LADO + 2*(Y_0 + LADO*j))/2
            if juego[j][i] != VACIO:
                gamelib.draw_text(juego[j][i], centro_x, centro_y, size = 12)


def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(X_MAX, Y_MAX)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)

gamelib.init(main)