from tkinter import *

raiz = Tk()

raiz.title('Ventana de pruebas')
#raiz.resizable(True,False)
#raiz.iconbitmap(r"\ imagem_1")
#raiz.geometry('650x350')
raiz.config(bg='blue')
raiz.config(bd=35)
raiz.config(relief='groove') #otro é sustituir groove por sunken tipode borde
raiz.config(cursor='hand2') #hand2

miFrame = Frame()
#miFrame.pack(side='right',anchor='n')
#miFrame.pack(fill='both',expand='True')
miFrame.pack()
miFrame.config(bg='red')
miFrame.config(width=650,height=350)
miFrame.config(bd=35)
miFrame.config(relief='sunken') #otro é sustituir groove por sunken tipode borde
miFrame.config(cursor='pirate') #hand2

#esta instruccion deve estar siempre al final
raiz.mainloop()