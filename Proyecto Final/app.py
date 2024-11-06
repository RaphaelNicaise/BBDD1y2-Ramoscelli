import msvcrt
import os # TODO: Clear consola

from database import Database
from entities.usuario import Usuario
from entities.libro import Libro

db = Database()

DICT_OPCIONES = {
    '1': 'Crear usuario',
    '2': 'Eliminar usuario',
    '3': 'Crear libro',
    '4': 'Eliminar libro',
    '5': 'Prestar libro',
    '6': 'Devolver libro',
    'q': 'Salir'
}

def show_menu(): # Muestra el menu de opciones
    
    for key, value in DICT_OPCIONES.items():
        print(f"{key}. {value}")
    print("Seleccione una opcion: ", end='')

def menu(): # Ejecuta el menu de opciones y las acciones correspondientes
    
    while True:
        
        show_menu()        
        
        try:
            key = msvcrt.getch().decode('utf-8').lower()
        except UnicodeDecodeError as e:
            print("Invalid key")
           
        if key in ['1', '2', '3', '4', '5', '6', 'q']:

                match key:
                    case '1':
                        print("Opcion 1")
                    case '2':
                        print("Opcion 2")
                    case '3':
                        print("Opcion 3")
                    case '4':
                        print("Opcion 4")
                    case '5':
                        print("Opcion 5")
                    case '6':
                        print("Opcion 6")
                    case 'q':
                        print("Saliendo")
                        break
            
        else:
            print("Invalid key")

def main(): # Funcion principal
    menu()

if __name__ == "__main__":
    libro1 = Libro.crear_libro(db, "E23452452345543", "234543345", "Fantasiafdfsd", "Minotauro", 1954)
    print(libro1.lid)
    