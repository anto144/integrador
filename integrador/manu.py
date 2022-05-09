from manejadorcamas import manejadorcamas
from manejadormedicamentos import manejadormed
class menuu:
    __switcher=None
    __M=None
    __Mc=None

    def __init__(self):
        self.__switcher = { 
            'a':self.opcion1,
            'b':self.opcion2,
            'c':self.salir,
            }
        self.__M=manejadormed()
        self.__M.cargarlista()
        self.__Mc=manejadorcamas()
        self.__Mc.cargararre()

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    def salir(self):
        print('Salir')

    def opcion1(self):
        print("opcion a")
        self.__Mc.daralta(self.__M)
       
        
    def opcion2(self):
        print("opcion b")
        self.__Mc.listarinternados()