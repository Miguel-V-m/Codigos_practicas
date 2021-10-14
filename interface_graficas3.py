from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()
#se puede abreviar
# miLabel = Label(miFrame, text='hola alumnos de python')
# #miLabel.pack()
# miLabel.place(x=100,y=200)
#de la forma
miImagen = PhotoImage(file='imagem.gif')
#Label(miFrame, text='hola alumnos de python',fg='red',font=('comic Sans MS', 18)).place(x=100,y=200)
Label(miFrame, image=miImagen).place(x=0.2,y=0.2)


root.mainloop()