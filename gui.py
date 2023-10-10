import tkinter as tk
from screen_clean import screen_clean
import menu_profesores
import menu_encargados
import menu_administradores
from validar_identidad import *

def iniciar_sesion(opcion):
    if opcion == "Profesor":
        validar = ValidarProfesor()
        if validar.validar():
            menu_profesores.menu()
    elif opcion == "Encargado":
        validar = ValidarEncargado()
        if validar.validar():
            menu_encargados.menu()
    elif opcion == "Administrador":
        validar = ValidarAdministrador()
        if validar.validar():
            menu_administradores.menu()

def mostrar_menu(opcion):
    screen_clean()
    ventana.destroy()
    iniciar_sesion(opcion)

def salir():
    ventana.destroy()

def mostrar_interfaz_grafica():
    global ventana
    ventana = tk.Tk()
    ventana.title("Sistema de Acceso")

    label = tk.Label(ventana, text="Bienvenido al sistema de acceso:")
    label.pack()

    btn_profesor = tk.Button(ventana, text="Iniciar sesión como Profesor", command=lambda: mostrar_menu("Profesor"))
    btn_profesor.pack()

    btn_encargado = tk.Button(ventana, text="Iniciar sesión como Encargado", command=lambda: mostrar_menu("Encargado"))
    btn_encargado.pack()

    btn_administrador = tk.Button(ventana, text="Iniciar sesión como Administrador", command=lambda: mostrar_menu("Administrador"))
    btn_administrador.pack()

    btn_salir = tk.Button(ventana, text="Salir", command=salir)
    btn_salir.pack()

    ventana.mainloop()
