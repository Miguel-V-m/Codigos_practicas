from tkinter import *

root=Tk()
root.title('Ejemplo')

playa=IntVar()
montanha=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=''
    if playa.get()==1:
        opcionEscogida+='playa'

    if montanha.get()==1:
        opcionEscogida+='montaña'

    if turismoRural.get()==1:
        opcionEscogida+='turismo rural'   

    testoFinal.config(text=opcionEscogida)         

foto=PhotoImage(file='ave.png')
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame,text='elige destino',width=50).pack()

Checkbutton(frame,text='playa',variable=playa,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text='Montaña',variable=montanha, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame,text='Turismo rural',variable=turismoRural, onvalue=1, offvalue=0,command=opcionesViaje).pack()

testoFinal=Label(frame)
testoFinal.pack()



root.mainloop()