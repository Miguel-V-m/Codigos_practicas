from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo('Procesador de Miguel','Procesador de texto versión 2021')

def avisoLIcencia():
    messagebox.showwarning('Licencia', 'Producto bajo licencia GNU')

def salirAplicacion():
    #alor=messagebox.askquestion('salir','deseas salir de la aplicación?')
    valor=messagebox.askokcancel('salir','deseas salir de la aplicación?')

    #if valor=='yes':
    if valor==True:
        root.destroy()

def cerrarDocumento():
    valor=messagebox.askokcancel('Reintentar','No es posible cerrar. Documento bloqueado')
    if valor==False:
        root.destroy()





barraMenu= Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu= Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label='nuevo')
archivoMenu.add_command(label='guardar')
archivoMenu.add_command(label='guardar como')
archivoMenu.add_separator()
archivoMenu.add_command(label='cerrar',command=cerrarDocumento)
archivoMenu.add_command(label='salir',command=salirAplicacion)


archivoEdicion= Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label='copiar')
archivoEdicion.add_command(label='pegar')


archivoHerramientas= Menu(barraMenu)

archivoAyuda= Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label='Licencia',command=avisoLIcencia)
archivoAyuda.add_command(label='Acerca de...',command=infoAdicional)

barraMenu.add_cascade(label='Archivo',menu=archivoMenu)
barraMenu.add_cascade(label='Edición',menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas',menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)



root.mainloop()