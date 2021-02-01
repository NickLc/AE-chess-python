import chess

def obtener_casillas_debiles_blancas(tablero):
    casillas_debiles = []
    CASILLAS_BLANCAS = list(range(8,32))
    juegan_blancas = True
    CASILLAS_BLANCAS_OCUPADAS_POR_PEONES = list(tablero.pieces(chess.PAWN, juegan_blancas))
    for casilla in CASILLAS_BLANCAS:
        casilla_debil = False
        ocupada_por_peon = False
        protegida_por_peon = False
        alcanzable_por_peon = False
        protegible_por_peon_futuro = False

        CASILLAS_DERECHAS_ADYACENTES_DEBAJO_DE_LA_CASILLA = []
        CASILLAS_IZQUIERDAS_ADYACENTES_DEBAJO_DE_LA_CASILLA = []
        diag_inferior_derecha = None
        diag_inferior_izquierda = None

        fila = chess.square_rank(casilla)
        columna = chess.square_file(casilla)

        if casilla in CASILLAS_BLANCAS_OCUPADAS_POR_PEONES:
            ocupada_por_peon = True
            casilla_debil = False


        if columna < 7:
            diag_inferior_derecha = casilla - 8 + 1
            CASILLAS_DERECHAS_ADYACENTES_DEBAJO_DE_LA_CASILLA = list(range(casilla+1, 7, -8))[1:]
        if columna > 0:
            diag_inferior_izquierda = casilla - 8 - 1
            CASILLAS_IZQUIERDAS_ADYACENTES_DEBAJO_DE_LA_CASILLA = list(range(casilla-1, 7, -8))[1:]

        if diag_inferior_derecha in CASILLAS_BLANCAS_OCUPADAS_POR_PEONES or diag_inferior_izquierda in CASILLAS_BLANCAS_OCUPADAS_POR_PEONES:
            protegida_por_peon = True
            casilla_debil = False

        protegible_por_peon_futuro = any(check in CASILLAS_DERECHAS_ADYACENTES_DEBAJO_DE_LA_CASILLA + CASILLAS_IZQUIERDAS_ADYACENTES_DEBAJO_DE_LA_CASILLA for check in CASILLAS_BLANCAS_OCUPADAS_POR_PEONES)

        CASILLAS_DEBAJO_DE_LA_CASILLA = list(range(casilla, 7, -8))[1:]
        alcanzable_por_peon = any(check in CASILLAS_DEBAJO_DE_LA_CASILLA for check in CASILLAS_BLANCAS_OCUPADAS_POR_PEONES)

        if not ocupada_por_peon and not protegida_por_peon and not alcanzable_por_peon and not protegible_por_peon_futuro:
            casilla_debil = True

        if casilla_debil:
            casillas_debiles.append(casilla)
            
    return casillas_debiles


def obtener_casillas_debiles_negras(tablero):
    CASILLAS_NEGRAS = list(range(32,56))
    juegan_negras = True
    CASILLAS_NEGRAS_OCUPADAS_POR_PEONES = list(tablero.pieces(chess.PAWN, False))
    casillas_debiles = []
    
    for casilla in CASILLAS_NEGRAS:
        casilla_debil = False
        ocupada_por_peon = False
        protegida_por_peon = False
        alcanzable_por_peon = False
        protegible_por_peon_futuro = False

        CASILLAS_DERECHAS_ADYACENTES_ENCIMA_DE_LA_CASILLA = []
        CASILLAS_IZQUIERDAS_ADYACENTES_ENCIMA_DE_LA_CASILLA = []
        diag_superior_derecha = None
        diag_superior_izquierda = None

        fila = chess.square_rank(casilla)
        columna = chess.square_file(casilla)

        if casilla in CASILLAS_NEGRAS_OCUPADAS_POR_PEONES:
            ocupada_por_peon = True

        if columna < 7:
            diag_superior_derecha = casilla + 8 + 1
            CASILLAS_DERECHAS_ADYACENTES_ENCIMA_DE_LA_CASILLA = list(range(casilla + 1, 55, 8))[1:]
        if columna > 0:
            diag_superior_izquierda = casilla + 8 - 1
            CASILLAS_IZQUIERDAS_ADYACENTES_ENCIMA_DE_LA_CASILLA = list(range(casilla - 1, 55, 8))[1:]

        if diag_superior_derecha in CASILLAS_NEGRAS_OCUPADAS_POR_PEONES or diag_superior_izquierda in CASILLAS_NEGRAS_OCUPADAS_POR_PEONES:
            protegida_por_peon = True
            casilla_debil = False

        protegible_por_peon_futuro = any(check in CASILLAS_DERECHAS_ADYACENTES_ENCIMA_DE_LA_CASILLA + CASILLAS_IZQUIERDAS_ADYACENTES_ENCIMA_DE_LA_CASILLA for check in CASILLAS_NEGRAS_OCUPADAS_POR_PEONES)

        CASILLAS_ENCIMA_DE_LA_CASILLA = list(range(casilla, 55, 8))[1:]
        alcanzable_por_peon = any(check in CASILLAS_ENCIMA_DE_LA_CASILLA for check in CASILLAS_NEGRAS_OCUPADAS_POR_PEONES)

        if not ocupada_por_peon and not protegida_por_peon and not alcanzable_por_peon and not protegible_por_peon_futuro:
            casilla_debil = True

        if casilla_debil:
            casillas_debiles.append(casilla)
            # print(f"casilla {chess.square_name(casilla)} es debil: {casilla_debil}")
            
    return casillas_debiles

def obtener_movilidad_caballo(casilla_caballo, tablero):
    turno = tablero.turn
    fila = chess.square_rank(casilla_caballo)
    columna = chess.square_file(casilla_caballo)
    
    posibles_destinos_del_caballo = []
    destinos_definitivos_caballo = []
    
    if fila + 2 <= 7:
        if columna - 1 >= 0:
            posibles_destinos_del_caballo.append(chess.square(columna - 1, fila + 2))
        if columna + 1 <= 7:
            posibles_destinos_del_caballo.append(chess.square(columna + 1, fila + 2))

    if fila + 1 <= 7:
        if columna - 2 >= 0:
            posibles_destinos_del_caballo.append(chess.square(columna - 2, fila + 1))
        if columna + 2 <= 7:
            posibles_destinos_del_caballo.append(chess.square(columna + 2, fila + 1))
            
    if fila - 2 >= 0:
        if columna - 1 >= 0:
            posibles_destinos_del_caballo.append(chess.square(columna - 1, fila - 2))
        if columna + 1 <= 7:
            posibles_destinos_del_caballo.append(chess.square(columna + 1, fila - 2))
            
    if fila - 1 >= 0:
        if columna - 2 >= 0:
            posibles_destinos_del_caballo.append(chess.square(columna - 2, fila - 1))
        if columna + 2 <= 7:
            posibles_destinos_del_caballo.append(chess.square(columna + 2, fila - 1))
            
    for destino in posibles_destinos_del_caballo:
        if tablero.piece_at(destino) != None:
            if tablero.piece_at(destino).color != turno:
                destinos_definitivos_caballo.append(destino)
        else:
            destinos_definitivos_caballo.append(destino)
    
    movilidad_caballo = len(destinos_definitivos_caballo)
    
    return movilidad_caballo

def bishop_mobility(tablero, casilla_alfil):
    turno = tablero.turn
    fila_origen = chess.square_rank(casilla_alfil)
    columna_origen = chess.square_file(casilla_alfil)
    
    ur = 0
    ul = 0
    dr = 0
    dl = 0

    for i in range(1,8):
        fila = fila_origen - i
        columna = columna_origen + i
        # print(f"down right fila {fila} columna: {columna}")
        if fila >= 0 and columna < 8:
            if tablero.piece_type_at(chess.square(columna, fila)) != None:
                # print(tablero.piece_type_at(chess.square(columna, fila)))
                break
            dr += 1
        else:
            break
            
    for i in range(1,8):
        fila = fila_origen + i
        columna = columna_origen + i
       
        if fila < 8 and columna < 8:
            if tablero.piece_type_at(chess.square(columna, fila)) != None:
                break
            ur += 1
        else:
            break
            
    for i in range(1,8):
        fila = fila_origen - i
        columna = columna_origen - i
        # print(f"down left fila {fila} columna: {columna} tipo pieza: {tablero.piece_type_at(chess.square(columna, fila))}")        
        if fila >= 0 and columna >= 0:
            if tablero.piece_type_at(chess.square(columna, fila)) != None:
                break
            dl += 1
        else:
            break
            
    for i in range(1,8):
        fila = fila_origen + i
        columna = columna_origen - i
        
        if fila < 8 and columna >= 0:
            if tablero.piece_type_at(chess.square(columna, fila)) != None:
                break
            ul += 1
        else:
            break

        
    # print(f"ur = {ur} ul = {ul} dl = {dl} dr = {dr}")
    return ul + ur + dl + dr


def casillas_adyacentes(casilla : int) -> list:
    lista_casillas_adyacentes = []
    
    fila = chess.square_rank(casilla)
    columna = chess.square_file(casilla)
    
    if fila > 0:
        lista_casillas_adyacentes.append(casilla - 8)
        if columna > 0:
            lista_casillas_adyacentes.append(casilla -8 - 1)
        if columna < 7:
            lista_casillas_adyacentes.append(casilla -8 + 1)
        
    if fila < 7:
        lista_casillas_adyacentes.append(casilla + 8)
        
        if columna > 0:
            lista_casillas_adyacentes.append(casilla + 8 - 1)
        if columna < 7:
            lista_casillas_adyacentes.append(casilla + 8 + 1)
        
    if columna > 0:
        lista_casillas_adyacentes.append(casilla - 1)
    if columna < 7:
        lista_casillas_adyacentes.append(casilla + 1)
        
    return lista_casillas_adyacentes