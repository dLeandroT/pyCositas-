import os
import random

def imprimir(archivo):
    """
    archivo = "ruta del archivo entre comillas"
     ej.:    imprimir("./directorio/archivo.txt") 
    """
    with open(archivo, "r", encoding="utf-8") as f:
        for line in f:
            print(line)
        f.close()


def draw_bienvenida():
    os.system("clear")
    imprimir("./bienvenida.txt")
    input("\n\n\nPresiona ENTER para continuar...")
    print("_______________________________________")
        
    # Imprimir instrucciones
    os.system("clear")
    print("\n")
    imprimir("./instrucciones.txt")
    input("\n\nPresiona ENTER para continuar...")


def choose_word():
    with open("./palabras.txt", "r", encoding="utf-8") as f:
        secret_words = [line.strip() for line in f]
    return random.choice(secret_words)

    
    

#  Funcion Principal
def run():
    draw_bienvenida()
    secret_word = choose_word()
    # Gamelooop 
    is_gameover = False
    while not is_gameover:
        os.system("clear")
        # Pendiente imprimir el estado del colgado
        letra = input(" Ingresa una letra:  ")
       

        




#Entry Point
if __name__ == '__main__':
    run()