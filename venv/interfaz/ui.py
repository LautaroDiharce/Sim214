from tkinter import * 
import simulacion 
from tkinter import ttk
import funciones.calculos as cal


def agregar_elemento_a_grid(tree:ttk.Treeview, x):
    tree.insert('', 'end', text="1", values=x)
    #tree.update()

def init_result(n_baja,n_sube,pas_actuales,iteraciones):
    result=simulacion.iniciar_simulacion(n_baja,n_sube,pas_actuales,iteraciones)
    ventana = Tk()
    ventana.geometry("400x200+500+200")
    ventana.title("Fin de la simulacion")
    sumandos=cal.resumir_resultados(result)
    etiqueta1 = Label(ventana, text="Tiempo de permanencia en minutos:" + str(sumandos[1]))
    etiqueta1.pack()
    etiqueta2 = Label(ventana, text="Tiempo total en minutos:" + str(sumandos[0]))
    etiqueta2.pack()

def click():
    iteraciones=input1.get()
    #print(iteraciones)
    pas_actuales=input2.get()
    #print(pas_actuales)
    n_sube=input3.get()
    #print(n_sube)
    n_baja=input4.get()
    #print(n_baja)
    aux_iter=validar_iter(iteraciones)
    aux1= validar_inputs(pas_actuales)
    aux2= validar_inputs(n_sube)
    aux3= validar_inputs(n_baja)
    if aux1 in (1,2) or aux2 in (1,2) or aux3 in (1,2) or aux_iter in (1,2):
        ventanaAux = Tk()
        ventanaAux.title("Error")
        label_aux=Label(ventanaAux,text="Error en los valores ingresados, ingrese valores validos")
        label_aux.pack()
        ventanaAux.protocol("WM_DELETE_WINDOW",ventanaAux.destroy)
        return [False,aux1,aux2,aux3,aux_iter]
    elif aux_iter == 3:
        ventanaAux_iter = Tk()
        ventanaAux_iter.title("Error")
        label_aux_iter=Label(ventanaAux_iter,text="La cantidad de iteraciones es demasiado elevada, ingrese como maximo 2200000")
        label_aux_iter.pack()
        ventanaAux_iter.protocol("WM_DELETE_WINDOW",ventanaAux_iter.destroy)
        return [False,aux1,aux2,aux3,aux_iter]
    else:
        return [True,n_baja,n_sube,pas_actuales,iteraciones]



def validar_iter(iteraciones):
        if not iteraciones:
            return 1  # No permitir cadenas vacías
        try:
            value = int(iteraciones)
            if value <=0:
                return 1
            if value >2200000:
                return 3
        except ValueError:
            #print("error transformada")
            return 2         
        #return 0   

def validar_inputs(entrada):
        if not entrada:
            return 1  # No permitir cadenas vacías
        try:
            value = int(entrada)
            if value <0:
                return 1
            return 0
        except ValueError:
            return 2      
    #return 0

def init_graf(n_baja,n_sube,pas_actuales,iteraciones):

    ventana = Tk()
    ventana.title("Fin de la simulacion")
    ventana.geometry("400x200+500+200")
    treeframe=Frame(ventana)
    treeframe.pack()
    treescroll=Scrollbar(treeframe)
    treescroll.pack(side=RIGHT,fill=Y)
    result=simulacion.iniciar_simulacion(n_baja,n_sube,pas_actuales,iteraciones)
    tree = ttk.Treeview(treeframe, column=("c1", "c2", "c3","c4","c5","c6","c7","c8","c9","c10","c11","c12","c13","c14","c15","c16"), show='headings', height=len(result),yscrollcommand=treescroll.set)
 

    treescroll.config(command=tree.yview)

    tree.column("# 1", anchor=CENTER, width=50,stretch=NO)
    tree.heading("# 1", text="Iter")
    tree.column("# 2", anchor=CENTER, width=100,stretch=NO)
    tree.heading("# 2", text="Reloj(min)")
    tree.column("# 3", anchor=CENTER, width=100,stretch=NO)
    tree.heading("# 3", text="Evento")
    tree.column("# 4", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 4", text="Direccion Ascensor")
    tree.column("# 5", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 5", text="Prox asc(min)")
    tree.column("# 6", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 6", text="Prox pas(min)")
    tree.column("# 7", anchor=CENTER, width=100,stretch=NO)
    tree.heading("# 7", text="Direc pasajero")
    tree.column("# 8", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 8", text="Pasajeros actual")
    tree.column("# 9", anchor=CENTER, width=80,stretch=NO)
    tree.heading("# 9", text="Pas bajan")
    tree.column("# 10", anchor=CENTER, width=80,stretch=NO)
    tree.heading("# 10", text="Pas suben")
    tree.column("# 11", anchor=CENTER, width=80,stretch=NO)
    tree.heading("# 11", text="Cola Sube")
    tree.column("# 12", anchor=CENTER, width=80,stretch=NO)
    tree.heading("# 12", text="Cola baja")
    tree.column("# 13", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 13", text="Permanencia(min)")
    tree.column("# 14", anchor=CENTER, width=120,stretch=NO)
    tree.heading("# 14", text="Perman acum")
    tree.column("# 15", anchor=CENTER, width=100,stretch=NO)
    tree.heading("# 15", text="Pas total")
    tree.column("# 16", anchor=CENTER, width=100,stretch=NO)
    tree.heading("# 16", text="Pas cerrar puertas")
    
    for i in result:
        #print(i)
        agregar_elemento_a_grid(tree,i)
    tree.update()
    tree.pack()
    ventana_res_final=Tk()
    ventana_res_final.title("Resumen")
    sumandos=cal.resumir_resultados(result)
    etiqueta1 = Label(ventana_res_final, text="Tiempo de permanencia en minutos:" + str(sumandos[1]))
    etiqueta1.pack()
    etiqueta2 = Label(ventana_res_final, text="Tiempo total en minutos:" + str(sumandos[0]))
    etiqueta2.pack()
    etiqueta3= Label(ventana_res_final, text="si cierra esta ventana no podra volverla a abrir")
    etiqueta3.pack()
    ventana_res_final.protocol("WM_DELETE_WINDOW",ventana_res_final.destroy)

def btn_resultado():
    validacion=click()
    if validacion[0] == True:
        init_result(validacion[1],validacion[2],validacion[3],validacion[4])

def btn_grafico():
    validacion=click()
    if validacion[0] == True:
        init_graf(validacion[1],validacion[2],validacion[3],validacion[4])

root = Tk()
root.geometry("600x300+500+200")
root.title("Menu principal")

label1=Label(root,text="Ingresa el numero de iteraciones")
label1.pack()
input1=Entry(root,width=50)
input1.pack()
label2=Label(root,text="Ingresa aca la cantidad de pasajeros en el ascensor")
label2.pack()
input2=Entry(root,width=50)
input2.pack()
label3=Label(root,text="Ingresa aca el numero de pasajeros en la cola para subir")
label3.pack()
input3=Entry(root,width=50)
input3.pack()
label4=Label(root,text="Ingresa aca el numero de pasajeros en la cola para bajar")
label4.pack()
input4=Entry(root,width=50)
input4.pack()
# label5=Label(root,text="Ingresa aca")
# label5.pack()
# input5=Entry(root,width=50)
# input5.pack()
# label6=Label(root,text="Ingresa aca")
# label6.pack()
# input6=Entry(root,width=50)
# input6.pack()
btn_result = Button(root, text="iniciar Sumulacion solo resultado", command=btn_resultado)
btn_result.pack(side=LEFT)
btn_graf = Button(root, text="Iniciar simulacion con visualizacion",command=btn_grafico)
btn_graf.pack(side=LEFT)


root.mainloop()