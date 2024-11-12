import msvcrt
import os
import datetime as dt
import time

from database import Database
from entities.usuario import Usuario
from entities.libro import Libro
from entities.prestamo import Prestamo

print(r"""
 _      _  _      _  _         _
| |    (_)| |    | |(_)       | |
| |__   _ | |__  | | _   ___  | |_   ___   ___   __ _
| '_ \ | || '_ \ | || | / _ \ | __| / _ \ / __| / _` |
| |_) || || |_) || || || (_) || |_ |  __/| (__ | (_| |
|_.__/ |_||_.__/ |_||_| \___/  \__| \___| \___| \__,_|

""")
time.sleep(2)

def clear_console():
    # Si el sistema es Windows
    if os.name == 'nt':
        os.system('cls')
    # Para sistemas Unix (Linux, MacOS)
    else:
        os.system('clear')
        
db = Database()

DICT_OPCIONES = {
    '1': 'Gestion de Libros',
    '2': 'Gestion de Usuarios',
    '3': 'Reporte de Morosos',
    'q': 'Salir'
}

def show_menu(DICT):
    """
    Funcion que pasandole un diccionario de numeros con opciones y valores, imprime el menu en pantalla.
    Args:
        DICT (dict): Diccionario con las opciones del menu.  
    """
    for key, value in DICT.items():
        print(f"{key}. {value}")
    print("Seleccione una opcion: ", end='\n')

def menu(): # Ejecuta el menu de opciones y las acciones correspondientes
    
    while True:
        
        clear_console()
        show_menu(DICT_OPCIONES)        
        
        try:
            key = msvcrt.getch().decode('utf-8').lower()
        except UnicodeDecodeError as e:
            print("Invalid key")
           
        if key in DICT_OPCIONES.keys():

                match key:
                    case '1':
                        gestion_libros()
                    case '2':
                        gestion_usuarios()
                    case '3': 
                        reporte_morosos()
                    case 'q':
                        print("Chau")
                        break
            
        else:
            print("Invalid key")
            

# -- 1 -- 

def gestion_libros():
    """Agregar, ver, actualizar o eliminar información de usuarios."""
    
    DICT_OPCIONES_LIBROS = {
        '1': 'Registrar nuevo libro',
        '2': 'Ver detalles de un libro',
        '3': 'Actualizar información de un libro',
        '4': 'Eliminar un libro',
        '5': 'Listar libros',
        'q': '<- Volver al menu principal'
    }
    
    DICT_OPCIONES_LIBROS_ACTUALIZAR = {
        '1': 'Actualizar titulo',
        '2': 'Actualizar autor',
        '3': 'Actualizar Genero',
        '4': 'Actualizar editorial',
        '5': 'Actualizar año de publicación',
        'q': '<- Volver al menu anterior'
    }
    while True:
        
        clear_console()
        show_menu(DICT_OPCIONES_LIBROS)
        
        try:
            key = msvcrt.getch().decode('utf-8').lower()
        except UnicodeDecodeError as e:
            print("Invalid key")
            
        if key in DICT_OPCIONES_LIBROS.keys():

                match key:
                    case '1':
                        
                        clear_console()
                        Libro.crear_libro_menu(db)
                        input("Presione una tecla para continuar...")
                    
                    case '2':
                    
                        clear_console()
                        Libro.obtener_libro_menu(db)
                        input("Presione una tecla para continuar...")
                    
                    case '3':
                        
                        clear_console()
                        show_menu(DICT_OPCIONES_LIBROS_ACTUALIZAR)
                        
                        try:
                            key = msvcrt.getch().decode('utf-8').lower()
                        except UnicodeDecodeError as e:
                            print("Invalid key")
                            
                        if key in DICT_OPCIONES_LIBROS_ACTUALIZAR.keys():
                            match key:
                                case '1':
                                    clear_console()
                                    Libro.actualizar_titulo_menu(db)
                                    print("Presione una tecla para continuar...")
                                case '2':
                                    clear_console()
                                    Libro.actualizar_autor_menu(db)
                                    print("Presione una tecla para continuar...")
                                case '3':
                                    clear_console()
                                    Libro.actualizar_genero_menu(db)
                                    print("Presione una tecla para continuar...")
                                case '4':
                                    clear_console()
                                    Libro.actualizar_editorial_menu(db)
                                    print("Presione una tecla para continuar...")
                                case '5':
                                    clear_console()
                                    Libro.actualizar_año_publicacion_menu(db)
                                    print("Presione una tecla para continuar...")
                                case 'q':
                                    break
                    case '4':
                        
                        clear_console()
                        Libro.eliminar_libro_menu(db)
                        input("Presione una tecla para continuar...")
                    
                    case '5':
                        
                        clear_console()
                        Libro.listar_libros_menu(db)
                        input("Presione una tecla para continuar...")
                        
                    case 'q':
                        break      
        else:
            print("Invalid key")
    
def gestion_usuarios():
    """Registrar nuevos libros, ver detalles, actualizar información y eliminar entradas.
    """
    print("Gestion de Usuarios")
    
def reporte_morosos():
    print("Reporte de morosos")


if __name__ == "__main__":
    menu()
    
    