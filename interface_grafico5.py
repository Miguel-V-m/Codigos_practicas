from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame,textvariable=minombre)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg='red',justify='center')

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=10)
cuadroPass.config(show='*')

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

textcomentario = Text(miFrame,width=16,height=5)
textcomentario.grid(row=4,column=1,padx=10,pady=10)

scrollVert= Scrollbar(miFrame, command=textcomentario.yview)
scrollVert.grid(row=4,column=2,sticky='nsew')
textcomentario.config(yscrollcommand=scrollVert.set)

nomnreLabel=Label(miFrame,text='Nombre:')
nomnreLabel.grid(row=0,column=0,sticky='e',padx=10,pady=10)

apellidoLabel=Label(miFrame,text='Apellido:')
apellidoLabel.grid(row=2,column=0,sticky='e',padx=10,pady=10)

direccionLabel=Label(miFrame,text='Direccion:')
direccionLabel.grid(row=3,column=0,sticky='e',padx=10,pady=10)

passLabel=Label(miFrame,text='Password:')
passLabel.grid(row=1,column=0,sticky='e',padx=10,pady=10)

comentariosLabel=Label(miFrame,text='Comentarios:')
comentariosLabel.grid(row=4,column=0,sticky='e',padx=10,pady=10)

def codigoBoton():
    minombre.set('Miguel')

botonEnvio=Button(raiz, text='Enviar',command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()