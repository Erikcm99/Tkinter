from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

ventana = Tk()
frame = LabelFrame(ventana)

pizza= StringVar()


INGREDIENTS = [
('Pepperoni', 'pepperoni'),
('Ceba', 'ceba')
]

def funcio():
    global labelRes
    yesno = messagebox.askquestion("titol finestra", "missatge")
    labelRes = Label(ventana, text='Has clicat si')
    if (yesno == 'yes'):
        labelRes['text']= "Has clicat si"
    else:
        labelRes['text']= "Has clicat no"
    labelRes.grid(column=1, row=5)


valor = 0
for text1, text2 in INGREDIENTS:
    Radiobutton(ventana, text=text1, variable=pizza, value=text2, command=funcio).grid(column=1, row=valor)
    valor += 1

labelRes = Label(ventana, text='')
labelRes.grid(column=1, row=5)
ventana.mainloop()
