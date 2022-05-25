# Autor: Génesis Belén Heredia
# Agente: Tostadora Inteligente
# Inteligencia Aritificial

# Se establece la función para la tostadora inteligente
def tostadora_inteligente():
    # Se definen los estados de mi agente
    # Se define el costo inicializado en 0
    # 0 indica Tostar - 1 indica sin tostar
    estado = {'C1': '0', 'C2': '0', 'C3': '0'}
    costo = 0

    # Se realiza el ingreso de la locación de la Tostadora
    locacion = input("Ingrese la locación de la Tostadora : ")
    # Se realiza el ingreso del estado de la tostadora: 0 Tostar - 1 Sin Tostar
    estado_agente = input(
        "Ingrese el estado de la Tostadora en la: "+locacion + "")

    if(locacion == 'C1'):
        # El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada
        locacion2 = input("Ingrese el estado de la Cocina 2")
        # El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada
        locacion3 = input("Ingrese el estado de la Cocina 3")
        # Los resultados deseados se muestran
        print("Objetivo:" + str(estado))

        # Se visualiza en que locación se encuentra la tostadora
        print("La Tostadora está en la Cocina 1")

        if(estado_agente == '1'):
            # La tostadora no realiza el tostado del pan
            print("La Tostadora no está tostando")
            # La tostadora realiza el tostado del pan
            estado['C1'] = '0'
            # El costro incrementa cuando la tostadora realice la acción
            costo += 1
            print("La tostadora está tostanto en la Cocina 1")
            # Se visualiza el costo actual
            print("El costo total es: " + str(costo))

            if(locacion2 == '1'):
                # Si la Tostadora se encuentra en la Cocina 2 sin tostar
                print("La Tostadora de la Cocina 2 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 2")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C2'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 2")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 2 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

            if (locacion3 == '1'):
                # Si la Tostadora se encuentra en la Cocina 3 sin tostar
                print("La Tostadora de la Cocina 3 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 3")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C3'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 3")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 3 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

        elif (estado == '0'):
            print("La Tostadora de la Cocina 1 está tostando el pan")
            if (locacion2 == '1'):
                # Si la Tostadora se encuentra en la Cocina 2 sin tostar
                print("La Tostadora de la Cocina 2 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 2")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C2'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 2")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 2 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

            if (locacion3 == '1'):
                    # Si la Tostadora se encuentra en la Cocina 3 sin tostar
                    print("La Tostadora de la Cocina 3 está sin tostar el pan")
                    print("La Tostadora es movida a la Cocina 3")
                    # El costro incrementa cuando la tostadora realice la acción
                    costo += 1
                    # Se visualiza el costo actual
                    print("El costo total es: " + str(costo))
                    # La Tostadora realizará el tostado del pan
                    estado['C3'] = '0'
                    # El costro incrementa cuando la tostadora realice la acción
                    costo += 1
                    print("La Tostadora está tostanto el pan en la Cocina 3")
                    print("El costo actual es: " + str(costo))
            else:
                    # La Tostadora está tostando el pan
                    print("La Tostadora de la Cocina 3 está tostando el pan")
                    print("Ninguna acción realizada. El costo actual es: " + str(costo))
        else:
                print("El estado del agente insertado no tiene")

    elif (locacion == 'C2'):
        # El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada
        locacion2 = input("Ingrese el estado de la Cocina 1")
        # El usuario indica si la tostadora se encuentra tostando o no (0/1) en la ubicación indicada
        locacion3 = input("Ingrese el estado de la Cocina 3")
        # Los resultados deseados se muestran
        print("Objetivo:" + str(estado))
        # Se visualiza en que locación se encuentra la tostadora
        print("La Tostadora está en la Cocina 2")

        if(estado_agente == '1'):
            # La tostadora no realiza el tostado del pan
            print("La Tostadora no está tostando")
            # La tostadora realiza el tostado del pan
            estado['C2'] = '0'
            # El costro incrementa cuando la tostadora realice la acción
            costo += 1
            print("La tostadora está tostanto en la Cocina 2")
            # Se visualiza el costo actual
            print("El costo total es: " + str(costo))

            if(locacion2 == '1'):
                # Si la Tostadora se encuentra en la Cocina 2 sin tostar
                print("La Tostadora de la Cocina 1 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 1")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C1'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 1")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 1 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

            if (locacion3 == '1'):
                # Si la Tostadora se encuentra en la Cocina 3 sin tostar
                print("La Tostadora de la Cocina 3 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 3")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C3'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 3")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 3 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

        elif (estado == '0'):
            print("La Tostadora de la Cocina 2 está tostando el pan")
            if (locacion2 == '1'):
                # Si la Tostadora se encuentra en la Cocina 2 sin tostar
                print("La Tostadora de la Cocina 1 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 1")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C1'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 1")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 1 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))

            if (locacion3 == '1'):
                # Si la Tostadora se encuentra en la Cocina 3 sin tostar
                print("La Tostadora de la Cocina 3 está sin tostar el pan")
                print("La Tostadora es movida a la Cocina 3")
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                # Se visualiza el costo actual
                print("El costo total es: " + str(costo))
                # La Tostadora realizará el tostado del pan
                estado['C3'] = '0'
                # El costro incrementa cuando la tostadora realice la acción
                costo += 1
                print("La Tostadora está tostanto el pan en la Cocina 3")
                print("El costo actual es: " + str(costo))
            else:
                # La Tostadora está tostando el pan
                print("La Tostadora de la Cocina 3 está tostando el pan")
                print("Ninguna acción realizada. El costo actual es: " + str(costo))
        else:
                print("El estado del agente insertado no tiene")

    
tostadora_inteligente()
