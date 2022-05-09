from camas import cama
import numpy as np
import csv
from datetime import date
class manejadorcamas:
    __cant=0
    __dimension=30
    __camas=None
    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 30
        self.__camas = np.empty(30, dtype=cama)
    def agregarcama(self,cama):
        self.__camas[self.__cantidad] = cama
        self.__cantidad += 1
    def cargararre(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            unaCama = cama(fila[0],fila[1], fila[2], fila[3], fila[4], fila[5])
            self.agregarcama(unaCama)
        return
    def buscar(self,nombre):
        i = 0
        while i < self.__cantidad and self.__camas[i].getnom().lower() != nombre.lower():
            i += 1
        if i == self.__cantidad:
            i = -1
        print(i)
        return i
    def daralta(self,medicamentos):
        nombre=input("ingrese el nombre y apellido del paciente: ")
        indice=self.buscar(nombre)
        if indice != -1 and self.__camas[indice].getestado():
            fecha=date.today()
            fecha = "{0}/{1}/{2}".format(fecha.day, fecha.month, fecha.year)
            self.__camas[indice].daralta(fecha)
            print(self.__camas[indice])
            print(medicamentos.getmedxcam(self.__camas[indice].getid()))

        return
    def listarinternados(self):
        diagnostico = input("Ingrese el diagnostico: ")
        print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format("Nombre", "Cama", "Habitacion", "Diagnostico", "Fecha de internacion"))
        for unaCama in self.__camas:
            if isinstance(unaCama, cama):
                if unaCama.getestado() and unaCama.getdiag().lower() == diagnostico.lower():
                    print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format(unaCama.getnom(), unaCama.getid(), unaCama.gethabitacion(), unaCama.getdiag(), unaCama.getfechai()))