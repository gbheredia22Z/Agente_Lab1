#Autor: Génesis Belén Heredia
#Agente: Tostadora Inteligente
#Inteligencia Aritificial 

#Se establece la función para la tostadora inteligente
def tostadora_inteligente ():
    #Se definen los estados de mi agente
    #Se define el costo inicializado en 0
    # 0 indica Tostar - 1 indica sin tostar
    estado = {'C1':'0', 'C2':'0', 'C3':'0'}
    costo = 0

    #Se realiza el ingreso de la locación de la Tostadora Inteligente
    locacion = input("Ingrese la locación de la tostadora inteligente: ")
    #Se realiza el ingreso del estado de la tostadora: 0 Tostar - 1 Sin Tostar
    estado_agente = input("Ingrese el estado de la Tostado en la: "+locacion+ "")

    if(locacion == 'C1'):
        #La tostadora no realiza el tostado del pan
        print("La Tostadora Inteligente no está tostando")
        #El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada        
        locacion2 = input("Ingrese el estado de la Cocina 2")
        #El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada        
        locacion3 = input("Ingrese el estado de la Cocina 3")
        #Los resultados deseados se muestran
        print("Objetivo:" + str(estado))

        #Se visualiza en que locación se encuentra la tostadora  
        print("La Tostadora está en la Cocina 1")