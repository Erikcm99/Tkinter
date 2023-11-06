import sqlite3
import tkinter as tk
import os

if not os.path.exists("subdirectori"):
    os.makedirs("subdirectori")

var_BD = sqlite3.connect("subdirectori/basquet.db")

cur_BD = var_BD.cursor()

cur_BD.execute('''CREATE TABLE IF NOT EXISTS jugadors (
                  nom TEXT,
                  cognom TEXT,
                  alcada REAL,
                  edat INTEGER
                )''')

var_BD.commit()

def afegir_a_bd():
    var_BD = sqlite3.connect("subdirectori/basquet.db")
    cur_BD = var_BD.cursor()

    nom = entry_nom.get()
    cognom = entry_cognom.get()
    alcada = entry_alcada.get()
    edat = entry_edat.get()

    cur_BD.execute("INSERT INTO jugadors VALUES (:z_nom, :z_cognom, :z_alcada, :z_edat)",
                   {'z_nom': nom, 'z_cognom': cognom, 'z_alcada': alcada, 'z_edat': edat})

    var_BD.commit()

    entry_nom.delete(0, tk.END)
    entry_cognom.delete(0, tk.END)
    entry_alcada.delete(0, tk.END)
    entry_edat.delete(0, tk.END)

def comprovar_dades():
    var_BD = sqlite3.connect("subdirectori/basquet.db")
    cur_BD = var_BD.cursor()

    cur_BD.execute("SELECT * FROM jugadors")

    resultats = cur_BD.fetchall()

    for fila in resultats:
        print(fila)

    var_BD.close()

finestra = tk.Tk()
finestra.title("Introduir Dades a la Base de Dades")

label_nom = tk.Label(finestra, text="Nom:")
label_nom.grid(row=0, column=0)
entry_nom = tk.Entry(finestra)
entry_nom.grid(row=0, column=1)

label_cognom = tk.Label(finestra, text="Cognom:")
label_cognom.grid(row=1, column=0)
entry_cognom = tk.Entry(finestra)
entry_cognom.grid(row=1, column=1)

label_alcada = tk.Label(finestra, text="Alçada:")
label_alcada.grid(row=2, column=0)
entry_alcada = tk.Entry(finestra)
entry_alcada.grid(row=2, column=1)

label_edat = tk.Label(finestra, text="Edat:")
label_edat.grid(row=3, column=0)
entry_edat = tk.Entry(finestra)
entry_edat.grid(row=3, column=1)

btn_afegir = tk.Button(finestra, text="Afegir a la Base de Dades", command=afegir_a_bd)
btn_afegir.grid(row=4, column=0, columnspan=2)

btn_comprovar = tk.Button(finestra, text="Comprovar Dades", command=comprovar_dades)
btn_comprovar.grid(row=5, column=0, columnspan=2)

finestra.mainloop()
