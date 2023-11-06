from tkinter import *
from PIL import ImageTk, Image

global ventana
ventana = Tk()
frame = LabelFrame(ventana)
numeroFoto = 0



listaImagenes = [
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\1.png")),
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\2.png")),
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\3.png")),
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\4.png")),
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\5.png")),
    ImageTk.PhotoImage(Image.open(r"C:\Users\erikc\Documents\TKINTER\imagenesTK13\6.png"))]
def canMove():
    if (numeroFoto == 0):
        botonPrev['state'] = DISABLED
    else:
        botonPrev['state'] = NORMAL
    if (numeroFoto == len(listaImagenes)-1):
        botonNext['state'] = DISABLED
    else:
        botonNext['state'] = NORMAL

def moveNext():
    global numeroFoto
    global label
    global listaImagenes
    if numeroFoto < len(listaImagenes) - 1:
        numeroFoto+=1
        canMove()
    muestraFoto()


def muestraFoto():
        global label
        global listaImagenes
        label.grid_forget()
        label = Label(ventana,image=listaImagenes[numeroFoto])
        label.grid(row = 1, column = 3)
        labelProgreso()

def movePrev():
    global numeroFoto
    global label
    global listaImagenes

    if numeroFoto != 0:
        numeroFoto -= 1
        canMove()
    muestraFoto()

def labelProgreso():
    global listaImagenes
    labelProgreso = Label(ventana,text=str(numeroFoto + 1) + "/" + str(len(listaImagenes)), anchor=E)
    labelProgreso.grid(row = 1, sticky= W+ E)

botonQuit = Button(ventana,fg='red',bg='grey',font=("Comic Sans MS", 14),borderwidth='1',padx='1',pady='1',height='1', text="SORTIR", state="normal", command=ventana.quit)

botonNext = Button(ventana,fg='red',bg='grey',font=("Comic Sans MS", 14),borderwidth='1',padx='1',pady='1',height='1', text="->", state="normal", command=moveNext)

botonPrev = Button(ventana,fg='red',bg='grey',font=("Comic Sans MS", 14),borderwidth='1',padx='1',pady='1',height='1', text="<-", state="normal", command=movePrev)

canMove()
# for i in range(1, 9):
#     img = "C:/Users/erikc/Documents/TKINTER/imagenesTK13/" + str(i) + ".png"
#     # rawImg = r"{}".format(img)
#     listaImagenes.append(img)

for i in listaImagenes:
    print(i)


botonQuit.grid(row = 5, column = 3)
botonNext.grid(row = 5, column = 4)
botonPrev.grid(row = 5, column = 2)

label = Label(ventana)
label.grid(row = 1, column = 3)
muestraFoto()
ventana.mainloop()
