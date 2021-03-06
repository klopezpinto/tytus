#Esta es la creación de la ventana principal , la raíz es en donde va la ventana 
#con .config logramos personalizar cada elemento de la ventana 
from tkinter import* 
raiz = Tk()
VentanaPrincipal = Frame(raiz, width = 1200, height=600)
VentanaPrincipal.config(background = "#f9e0ae")
raiz.config(background = "#f9e0ae")
VentanaPrincipal.pack()


#......................Creaci[on de Campos para Bases de DATOS

nomBaseDatos2 = Entry(VentanaPrincipal)
nomBaseDatos2.place(x = 810 , y = 170)
nomBaseDatos2.config(relief = "sunken", borderwidth = 4)
nomBaseDatos2Label = Label(VentanaPrincipal, text="Nombre BD:")
nomBaseDatos2Label.place(x = 730 , y = 170)
nomBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

RenomBaseDatos2 = Entry(VentanaPrincipal)
RenomBaseDatos2.place(x = 810 , y = 240)
RenomBaseDatos2.config(relief = "sunken", borderwidth = 4)
RenomBaseDatos2Label = Label(VentanaPrincipal, text="Renombrar:")
RenomBaseDatos2Label.place(x = 730 , y = 240)
RenomBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

BuscarBaseDatos2 = Entry(VentanaPrincipal)
BuscarBaseDatos2.place(x = 810 , y = 205)
BuscarBaseDatos2.config(relief = "sunken", borderwidth = 4)
BuscarBaseDatos2Label = Label(VentanaPrincipal, text="Buscar:")
BuscarBaseDatos2Label.place(x = 730 , y = 205)
BuscarBaseDatos2Label.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

#--------------------CREACIÓN DE CAMPOS PARA Tuplas

nomTabla = Entry(VentanaPrincipal)
nomTabla.place( x = 1050 , y = 170)
nomTabla.config(relief = "sunken", borderwidth = 4)
nomTablaLabel = Label(VentanaPrincipal, text="Nombre Tabla:")
nomTablaLabel.place (x = 960 , y = 170)
nomTablaLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

nomBaseDatos = Entry(VentanaPrincipal)
nomBaseDatos.place(x = 1050 , y = 205)
nomBaseDatos.config(relief = "sunken", borderwidth = 4)
nomBaseDatosLabel = Label(VentanaPrincipal, text="Nombre BD:")
nomBaseDatosLabel.place(x = 960 , y = 205)
nomBaseDatosLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

Registro = Entry(VentanaPrincipal)
Registro.place (x = 1050 ,  y = 240)
Registro.config(relief = "sunken", borderwidth = 4)
RegistroLabel = Label(VentanaPrincipal, text="Registro:" )
RegistroLabel.place (x =960 , y = 240)
RegistroLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold") )

#---------------CREACIÓN DE CAMPOS PARA LAS Tablas ---------- 

#**************NOMBRE DE LA TABLA****************
nomTabla = Entry(VentanaPrincipal)
nomTabla.place( x = 560 , y = 170)
nomTabla.config(relief = "sunken", borderwidth = 4)
nomTablaLabel = Label(VentanaPrincipal, text="Nombre Tabla:")
nomTablaLabel.place (x = 460 , y = 170)
nomTablaLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

#*************NOMBRE DE LA BASE DE DATOS ************** 

nomBaseDatos = Entry(VentanaPrincipal)
nomBaseDatos.place(x = 560 , y = 205)
nomBaseDatos.config(relief = "sunken", borderwidth = 4)
nomBaseDatosLabel = Label(VentanaPrincipal, text="Nombre BD:")
nomBaseDatosLabel.place(x = 460 , y = 205)
nomBaseDatosLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold"))

#***********No de Columna**************
numeroDeColumna = Entry(VentanaPrincipal)
numeroDeColumna.place (x = 560 ,  y = 240)
numeroDeColumna.config(relief = "sunken", borderwidth = 4)
numeroDeColumnaLabel = Label(VentanaPrincipal, text="No. Columna:" )
numeroDeColumnaLabel.place (x =460 , y = 240)
numeroDeColumnaLabel.config(background = "#f9e0ae" , foreground = "#682c0e", font = ("Helvetica", 9, "bold") )

#------------ENTRADA DE TEXTO PARA CARGA MASIVA --------------------- 

cargaNasiva = Text(VentanaPrincipal, width = 55, height = 21)
cargaNasiva.place(x=10, y = 50)

#--------------BOTONES PARA CARGA MASIVA --------- 

botonCarga = Button(VentanaPrincipal , text = "AGREGAR")
botonCarga.place(x=300, y = 400)
botonCarga.config(background = "#682c0e", fg="white", font=("Helvetica", 9 , "bold") )

#------------------------------MENU BAR------------------------------------- 
menubar = Menu(raiz)
raiz.config(menu = menubar)

#------- LOS SUBMENUS --------------------

filemenu = Menu(menubar, tearoff = 0)
editmenu = Menu(menubar, tearoff = 0)
helpmenu = Menu(menubar, tearoff = 0)


#-----------------Añadirlos a la barra ---------- 
menubar.add_cascade(label = "Archivo", menu=filemenu)
menubar.add_cascade(label = "Graficar", menu = editmenu )
menubar.add_cascade(label = "Mostrar", menu = helpmenu)



#---------------AÑADIENDO SUBMENUS--------------------- 
filemenu.add_command(label="Nuevo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")



#-------------------------TITULOS DE SECCIONES-------------------

nomTablasLabel = Label(VentanaPrincipal, text="Tablas")
nomTablasLabel.place(x = 550 , y = 105)
nomTablasLabel.config(background = "#f9e0ae" , foreground = "#c24914", font = ("Helvetica", 15, "bold"))


nomBasesLabel = Label(VentanaPrincipal, text="Bases de Datos")
nomBasesLabel.place(x = 760 , y = 105)
nomBasesLabel.config(background = "#f9e0ae" , foreground = "#c24914", font = ("Helvetica", 15, "bold"))

nomTuplasLabel = Label(VentanaPrincipal, text = "Tuplas")
nomTuplasLabel.place(x=1000, y = 105)
nomTuplasLabel.config(background = "#f9e0ae" , foreground = "#c24914", font = ("Helvetica", 15, "bold"))

#--------------------------MENU DESPLEGABLE PARA LAS TUPLAS

var = StringVar(VentanaPrincipal)
opciones = ['Insertar', 'Actualizar','Eliminar', 'Limpiar Tabla', 'Buscar']
opcion = OptionMenu(VentanaPrincipal, var, *opciones)

opcion.place(x= 1000, y = 300)
opcion.config(background = "#fc8621", fg="white", font = ("Helvetica", 10, "bold"))


#-----------MENU DESPLEGABLE PARA LAS BASES DE DATOS

var2 = StringVar(VentanaPrincipal)
opciones2 = ["Crear", "Mostrar BD", "Renombrar", "Eliminar"]
opciones2 = OptionMenu(VentanaPrincipal, var2, *opciones2)

opciones2.place(x=800 , y = 300 )
opciones2.config(background = "#fc8621", fg="white", font = ("Helvetica", 10, "bold"))


#----------------------MENU DESPLEGABLE PARA TABLAS 

var3 = StringVar(VentanaPrincipal)
opciones3 = ["Crear", "Mostrar", "E.Table", "E.Range", "A.Drop", "A.Add", "A.AddTK", "Renombrar", "Add.Col", "Del.Col", "Eliminar"]
opciones3 = OptionMenu(VentanaPrincipal, var3 , *opciones3)
opciones3.place(x=550, y =300)
opciones3.config(background = "#fc8621", fg="white", font = ("Helvetica", 10, "bold"))

raiz.mainloop()