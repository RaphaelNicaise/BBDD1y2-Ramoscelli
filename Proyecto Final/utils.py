import os

def clear_console():
    """
    funcion que limpia la consola de acuerdo al sistema operativo.
    """
    if os.name == 'nt':
        os.system('cls')
    # Para sistemas Unix (Linux, MacOS)
    else:
        os.system('clear')
        
def espera_tecla():
    input("Presione una tecla para continuar...")