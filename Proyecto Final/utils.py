import os
import msvcrt

print(r"""
 _      _  _      _  _         _
| |    (_)| |    | |(_)       | |
| |__   _ | |__  | | _   ___  | |_   ___   ___   __ _
| '_ \ | || '_ \ | || | / _ \ | __| / _ \ / __| / _` |
| |_) || || |_) || || || (_) || |_ |  __/| (__ | (_| |
|_.__/ |_||_.__/ |_||_| \___/  \__| \___| \___| \__,_|

""")

def clear_console():
    """
    funcion que limpia la consola de acuerdo al sistema operativo.
    """
    if os.name == 'nt':
        os.system('cls')
    # Para sistemas Unix (Linux, MacOS)
    else:
        os.system('clear')
        
def espera_enter():
    input("Presione una tecla para continuar...")
    
def espera_input():
    try:
        key = msvcrt.getch().decode('utf-8').lower()
    except UnicodeDecodeError as e:
        print("Error al leer la tecla presionada")
        return None
    
    return key


def show_menu(DICT):
    """
    Funcion que pasandole un diccionario de numeros con opciones y valores, imprime el menu en pantalla.
    Args:
        DICT (dict): Diccionario con las opciones del menu.  
    """
    for key, value in DICT.items():
        print(f"{key}. {value}")
    print("Seleccione una opcion: ", end='\n')