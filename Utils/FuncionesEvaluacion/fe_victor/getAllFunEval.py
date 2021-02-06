import chess

from .victor_utils import obtener_casillas_debiles_blancas, obtener_casillas_debiles_negras, obtener_movilidad_caballo, bishop_mobility, casillas_adyacentes

# 1
def obtener_cantidad_casillas_debiles(tablero):
    juegan_blancas = !tablero.turn
    casillas_debiles = obtener_casillas_debiles_blancas(tablero) if juegan_blancas else obtener_casillas_debiles_negras(tablero)
    
    cantidad_casillas_debiles = len(casillas_debiles)
    
    return cantidad_casillas_debiles

    
# 2
# In[34]:
def countEnemyKnightsOnWeak(board: chess.Board):
    turno = !board.turn
    enemyKnightsCasillas = list(board.pieces(chess.KNIGHT, not turno))
    casillasMisPeones = list(board.pieces(chess.PAWN, turno))
    
    knights_enemies_on_weak = 0
    
    if turno:
        miZona = list(range(8,32))
    else:
        miZona = list(range(32,56))
        
    for casillaCaballo in enemyKnightsCasillas:
        origen_amenazas = []
        
        fila = chess.square_rank(casillaCaballo)
        columna = chess.square_file(casillaCaballo)
        
        if turno:
            if columna > 0:
                origen_amenazas.append(casillaCaballo - 8 - 1)
            if columna < 7:
                origen_amenazas.append(casillaCaballo - 8 + 1)
        else:
            if columna > 0:
                origen_amenazas.append(casillaCaballo + 8 - 1)
            if columna < 7:
                origen_amenazas.append(casillaCaballo + 8 + 1)

        if any([origen_amenaza in miZona for origen_amenaza in origen_amenazas]):
            if not any([origen_amenaza in casillasMisPeones for origen_amenaza in origen_amenazas]):
                # print(f"CASILLA {chess.square_name(casillaCaballo)}")
                # print(f"origen amenazas: {origen_amenazas}")
                knights_enemies_on_weak += 1
    
    return knights_enemies_on_weak

# 3
def obtener_cantidad_peones_centrales(tablero):
    cantidad_peones_en_el_centro = 0
    color_turno = !tablero.turn
    casillas_centrales = [27,28,35,36]
    casillas_peones = list(tablero.pieces(chess.PAWN, color_turno))
    
    for casilla in casillas_centrales:
        if casilla in casillas_peones:
            cantidad_peones_en_el_centro += 1
    return cantidad_peones_en_el_centro

# 4
def get_pawns_around_king(tablero):
    cantida_peones_alrededor_del_rey = 0
    turno = !tablero.turn
    casilla_rey = tablero.king(turno)
    casillas_adyacentes_al_rey = casillas_adyacentes(casilla_rey)
    
    casillas_peones = list(tablero.pieces(chess.PAWN, turno))
    
    for casilla in casillas_adyacentes_al_rey:
        if casilla in casillas_peones:
            cantida_peones_alrededor_del_rey += 1
    
    return cantida_peones_alrededor_del_rey

# 8
def get_bishop_mob(tablero):
    movilidad_alfiles_acumulada = 0
    turno = !tablero.turn    
    casillas_alfiles = list(tablero.pieces(chess.BISHOP, turno))
    
    for casilla_alfil in casillas_alfiles:
        movilidad_alfiles_acumulada += bishop_mobility(tablero, casilla_alfil)
    
    return movilidad_alfiles_acumulada


# 9
def cantidad_alfiles_in_big_diagonal(tablero):
    cantidad_alfiles_big_diagonal = 0
    color_turno = !tablero.turn
    casillas_alfiles = list(tablero.pieces(chess.BISHOP, color_turno))
    
    for casilla in casillas_alfiles:
        fila = chess.square_rank(casilla)
        columna = chess.square_file(casilla)
        
        # print(f"fila {fila}  columna {columna}")
        
        if fila == columna or abs(fila + columna) == 7:
            cantidad_alfiles_big_diagonal += 1
    
    return cantidad_alfiles_big_diagonal


# 10
def got_bishop_pair(tablero):
    color_turno = !tablero.turn
    
    casillas_alfiles = list(tablero.pieces(chess.BISHOP, color_turno))
    
    if len(casillas_alfiles) >= 2:
        return 1
    else:
        return 0

# 11
def get_knightMob(board: chess.Board):
    movilidad_caballos_acumulada = 0
    turno = !board.turn
    
    casillas_caballos = list(board.pieces(chess.KNIGHT, turno))
    
    for casilla_caballo in casillas_caballos:
        movilidad_caballos_acumulada += obtener_movilidad_caballo(casilla_caballo, board)
        
    return movilidad_caballos_acumulada


# 12
def caballos_apoyados_por_peones(tablero):
    cantidad_caballos_apoyados_por_peones = 0
    juegan_blancas = !tablero.turn
    casillas_caballos = list(tablero.pieces(chess.KNIGHT, juegan_blancas))
    casillas_peones = list(tablero.pieces(chess.PAWN, juegan_blancas))
    
    if juegan_blancas:        
        for casilla_caballo in casillas_caballos:
            fila = chess.square_rank(casilla_caballo)
            columna = chess.square_file(casilla_caballo)

            if fila > 1:
                diag_inferior_izquierda = None
                diag_inferior_derecha = None

                if columna > 0:
                    diag_inferior_izquierda = casilla_caballo - 8 - 1
                if columna < 7:
                    diag_inferior_derecha = casilla_caballo - 8 + 1
                    
                # print(f"Casilla diagonal inferior izquierda de la casilla {casilla_caballo}: {diag_inferior_izquierda}")
                # print(f"Casilla diagonal inferior derecha de la casilla {casilla_caballo}: {diag_inferior_derecha}")

                
                if diag_inferior_izquierda in casillas_peones or diag_inferior_derecha in casillas_peones:
                    cantidad_caballos_apoyados_por_peones += 1
    else:
        for casilla_caballo in casillas_caballos:
            fila = chess.square_rank(casilla_caballo)
            columna = chess.square_file(casilla_caballo)

            if fila < 6:
                diag_superior_izquierda = None
                diag_superior_derecha = None

                if columna > 0:
                    diag_superior_izquierda = casilla_caballo + 8 - 1
                if columna < 7:
                    diag_superior_derecha = casilla_caballo + 8 + 1
                    
                if diag_superior_izquierda in casillas_peones or diag_superior_derecha in casillas_peones:
                    cantidad_caballos_apoyados_por_peones += 1
    return cantidad_caballos_apoyados_por_peones



# In[31]:
def get_all_fun_eval_v(tablero):
    cantidad_casilas_debiles = obtener_cantidad_casillas_debiles(tablero)
    caballos_enemigos_en_casillas_debiles = countEnemyKnightsOnWeak(tablero)
    peones_centrales = obtener_cantidad_peones_centrales(tablero)
    cantidad_peones_alrededor_rey = get_pawns_around_king(tablero)
    movilidad_alfiles_acumulada = get_bishop_mob(tablero)
    alfiles_en_gran_diagonal = cantidad_alfiles_in_big_diagonal(tablero)
    pareja_de_alfiles = got_bishop_pair(tablero)
    movilidad_caballos_acumulada = get_knightMob(tablero)
    caballos_suporteados_por_peones = caballos_apoyados_por_peones(tablero)
    
    return [
        cantidad_casilas_debiles,
        caballos_enemigos_en_casillas_debiles,
        peones_centrales,
        cantidad_peones_alrededor_rey,
        movilidad_alfiles_acumulada,
        alfiles_en_gran_diagonal,
        pareja_de_alfiles,
        movilidad_caballos_acumulada,
        caballos_suporteados_por_peones
    ]






