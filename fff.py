import tkinter as tk
from tkinter import Canvas

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)

    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar(nodo.derecha, valor)

    return nodo

def dibujar_arbol(canvas, nodo, x, y, distancia):
    if nodo is not None:
        canvas.create_oval(x, y, x + 30, y + 30, fill='white', outline='black')
        canvas.create_text(x + 15, y + 15, text=str(nodo.valor))
        if nodo.izquierda is not None:
            canvas.create_line(x + 15, y + 30, x - distancia + 15, y + 60)
            dibujar_arbol(canvas, nodo.izquierda, x - distancia, y + 60, distancia // 2)
        if nodo.derecha is not None:
            canvas.create_line(x + 15, y + 30, x + distancia + 15, y + 60)
            dibujar_arbol(canvas, nodo.derecha, x + distancia, y + 60, distancia // 2)

valores = [8, 3, 10, 1, 6, 14, 4, 7, 13]

raiz = Nodo(valores[0])

for valor in valores[1:]:
    insertar(raiz, valor)

ventana = tk.Tk()
ventana.title("Árbol binario")

canvas = Canvas(ventana, width=800, height=400, bg='white')
canvas.pack()

dibujar_arbol(canvas, raiz, 400, 20, 200)

ventana.mainloop()
