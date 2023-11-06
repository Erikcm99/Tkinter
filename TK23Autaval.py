import os
from tkinter import filedialog as quelcom
import tkinter as tk
from PIL import Image, ImageTk

parte1 = os.getcwd()
path_imatges = os.path.join(parte1,"imagenesTK13")

parte1 = os.getcwd()
directori_desti = os.path.join(parte1,"imagenesCopia")
if not os.path.exists(directori_desti):
    os.makedirs(directori_desti)

imatge_seleccionada = None
path_imatge_seleccionada = None

def copiar_arxiu(arxiu_origen, arxiu_desti):
    with open(arxiu_origen, 'rb') as origen, open(arxiu_desti, 'wb') as desti:
        desti.write(origen.read())

def seleccionar_i_obrir_imatge():
    global imatge_seleccionada, path_imatge_seleccionada
    tipus_arxius = (
        ('Tots els arxius', '*.*'),
        ('Imatges tipus jpg', '*.jpg')
    )
    arxiu_seleccionat = quelcom.askopenfilename(
        initialdir=path_imatges,
        title='Selecciona una imatge',
        filetypes=tipus_arxius
    )
    if arxiu_seleccionat:
        path_imatge_seleccionada = arxiu_seleccionat
        imatge_seleccionada = Image.open(arxiu_seleccionat)
        mostrar_imatge()

def mostrar_imatge():
    if imatge_seleccionada:
        finestra_secundaria = tk.Toplevel()
        finestra_secundaria.title('Imatge Seleccionada')
        etiqueta_imatge = tk.Label(finestra_secundaria)
        etiqueta_imatge.pack()
        etiqueta_path = tk.Label(finestra_secundaria, text=f'Path de la imatge: {path_imatge_seleccionada}')
        etiqueta_path.pack()
        etiqueta_imatge.img = ImageTk.PhotoImage(imatge_seleccionada)
        etiqueta_imatge.config(image=etiqueta_imatge.img)

        guardar_boton = tk.Button(finestra_secundaria, text="Guardar Imatge", command=guardar_imatge)
        guardar_boton.pack()

def guardar_imatge():
    if imatge_seleccionada:
        guardar_como = quelcom.asksaveasfile(
            initialdir=directori_desti,
            defaultextension=".png",
            filetypes=[("Imatges PNG", "*.png"), ("Tots els arxius", "*.*")]
        )
        if guardar_como:
            imatge_seleccionada.save(guardar_como.name)
            guardar_como.close()

finestra = tk.Tk()
finestra.title('Selector d\'Imatges')


boton = tk.Button(finestra, text='Seleccionar i Obrir Imatge', command=seleccionar_i_obrir_imatge)
boton.pack()

finestra.mainloop()
