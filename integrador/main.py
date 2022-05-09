from manu import menuu

if __name__=='__main__':
    bandera = False
    m=menuu()
    while not bandera:
        print("")
        print("a dar de baja al paciente y listar los medicamentos que deberá devolver ")
        print("b listar pacientes internados por diagnostico")
        print("c para salir")
        opcion= input("Ingrese una opción: ")
        m.opcion(opcion)
        bandera =(opcion)=='c'