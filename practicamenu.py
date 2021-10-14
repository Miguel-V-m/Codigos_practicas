from tkinter import *

root=Tk()

barraMenu= Menu(root)
root.config(menu=barraMenu,width=300, height=300)

archivoMenu= Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label='nuevo')
archivoMenu.add_command(label='guardar')
archivoMenu.add_command(label='guardar como')
archivoMenu.add_separator()
archivoMenu.add_command(label='cerrar')
archivoMenu.add_command(label='salir')


archivoEdicion= Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label='copiar')
archivoEdicion.add_command(label='pegar')


archivoHerramientas= Menu(barraMenu)

archivoAyuda= Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label='Licencia')
archivoAyuda.add_command(label='Acerca de...')

barraMenu.add_cascade(label='Archivo',menu=archivoMenu)
barraMenu.add_cascade(label='Edición',menu=archivoEdicion)
barraMenu.add_cascade(label='Herramientas',menu=archivoHerramientas)
barraMenu.add_cascade(label='Ayuda',menu=archivoAyuda)



root.mainloop()