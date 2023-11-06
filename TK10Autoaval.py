import string
from tkinter import *

ventana = Tk()

op1 = 0.0
op2 = 0.0

def canComma(prompt: Entry):
    if(prompt.get().find(",") == -1 and len(prompt.get()) != 0):
            return True

    elif(buscaSimbolos(prompt.get()) != None):
        finalOp = prompt.get().split(buscaSimbolos(prompt.get()))[1]
        if (finalOp.find(",") == -1 and len(finalOp) != 0):
             return True
    else:
         return False

def creaLabel(ventana: Tk, num: int):
    newLabel = Label(ventana,text=num)
    newLabel.grid(row=0,column=0)

def buscaSimbolos(texto: str):
    for i, char in enumerate(texto[1:],1):
        match (char):
            case ("+"):
                  return "+"
            case ("-"):
                  return "-"
            case ("*"):
                  return "*"
            case ("/"):
                  return "/"
            case():
                  return None


def creaPrompt(ventana: Tk, text: str, prompt: Entry):
    valores = ["1","2","3","4","5","6","7","8","9","0"]
    total = 0
    if (text in valores):
            prompt.insert(len(prompt.get()), text)

    elif (text== "." and canComma(prompt)) :
         prompt.insert(len(prompt.get()) , text)

    elif (text== "<-"):
         prompt.delete(len(prompt.get()) - 1, END)

    elif (text == "C"):
         prompt.delete(0, END)

    elif (text == "+" and prompt.get().find("+") == -1 and len(prompt.get()) != 0):
         prompt.insert(len(prompt.get()) , text)
    elif (text == "-" and prompt.get().find("-") == -1 and len(prompt.get()) != 0):
         prompt.insert(len(prompt.get()) , text)

    elif (text == "*" and prompt.get().find("*") == -1 and len(prompt.get()) != 0):
         prompt.insert(len(prompt.get()) , text)

    elif (text == "/" and prompt.get().find("/") == -1 and len(prompt.get()) != 0):
         prompt.insert(len(prompt.get()) , text)

    elif (text == "=" and buscaSimbolos(prompt.get()) != None):
        for i, char in enumerate(prompt.get()):
            match (char):
                case ("+"):
                    op1 = float(prompt.get().split("+")[0])
                    op2 = float(prompt.get().split("+")[1])
                    total = op1 + op2
                    prompt.delete(0, END)
                    prompt.insert(0 , total)

                case ("-"):
                    op1 = float(prompt.get().split("-")[0])
                    op2 = float(prompt.get().split("-")[1])
                    total = op1 - op2
                    prompt.delete(0, END)
                    prompt.insert(0 , total)

                case ("*"):
                    op1 = float(prompt.get().split("*")[0])
                    op2 = float(prompt.get().split("*")[1])
                    total = op1 * op2
                    prompt.delete(0, END)
                    prompt.insert(0 , total)

                case ("/"):
                    op1 = float(prompt.get().split("/")[0])
                    op2 = float(prompt.get().split("/")[1])
                    total = op1 / op2
                    prompt.delete(0, END)
                    prompt.insert(0 , total)




def deletePrompt(ventana: Tk, text: str, prompt: Entry):
    prompt.insert(len(prompt.get()), text)

def creaBoton(y,x,num):
    boton = Button(ventana, text=num, state="normal", command=lambda:(num))



prompt = Entry(ventana)
boton1 = Button(ventana,text="1",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "1", prompt))
boton2 = Button(ventana,text="2",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "2" , prompt))
boton3 = Button(ventana,text="3",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "3" , prompt))
boton4 = Button(ventana,text="4",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "4" , prompt))
boton5 = Button(ventana,text="5",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "5" , prompt))
boton6 = Button(ventana,text="6",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "6" , prompt))
boton7 = Button(ventana,text="7",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "7" , prompt))
boton8 = Button(ventana,text="8",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "8" , prompt))
boton9 = Button(ventana,text="9",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "9" , prompt))
boton0 = Button(ventana,text="0",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "0" , prompt))
botonComma = Button(ventana,text=",",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, ".", prompt))
botonDelete = Button(ventana,text="<-",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "<-", prompt))
botonErase = Button(ventana,text="C",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "C", prompt))
botonEqual = Button(ventana,text="=",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "=", prompt))
botonSum = Button(ventana,text="+",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "+", prompt))
botonRes = Button(ventana,text="-",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "-", prompt))
botonMult = Button(ventana,text="*",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "*", prompt))
botonDiv = Button(ventana,text="/",fg="white",bg="grey", state="normal",font=("Comic Sans MS", 14), command=lambda:creaPrompt(ventana, "/", prompt))

prompt.grid(row=0,column=2)


boton9.grid(row=1,column=1)
boton8.grid(row=1,column=2)
boton7.grid(row=1,column=3)
boton6.grid(row=2,column=1)
boton5.grid(row=2,column=2)
boton4.grid(row=2,column=3)
boton3.grid(row=3,column=1)
boton2.grid(row=3,column=2)
boton1.grid(row=3,column=3)
boton0.grid(row=4,column=1)
botonComma.grid(row=4,column=2)
botonDelete.grid(row=4,column=3)
botonSum.grid(row=1,column=4)
botonEqual.grid(row=2,column=4)
botonErase.grid(row=3,column=4)
botonRes.grid(row=4,column=4)
botonMult.grid(row=4,column=5)
botonDiv.grid(row=4,column=6)


mainloop()
