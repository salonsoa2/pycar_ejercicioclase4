# Import a library of functions called 'pygame'
import pygame
from main_functions import *

# Initialize the game engine
pygame.init()

#call main routine
ancho = int(input("ancho de la ventana: "))
alto = int(input("alto de la ventana: "))
size = (ancho, alto)
rojo = int(input("Nivel de rojo: "))
verde = int(input("nivel de verde: "))
azul = int(input("nivel de azul: "))
color = (rojo, verde, azul)
titulo = input("titulo simulador: ")
main2(size, titulo, color)