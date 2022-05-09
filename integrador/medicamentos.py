class medicamentos:
    __idcama=0
    __idmed=0
    __nombre=''
    __monodroga=''
    __presentacion=''
    __cant=''
    __precio=0
    def __init__(self,idcam,idmed,nombre,monodr,presen,cant,precio):
        self.__idcama=idcam
        self.__idmed=idmed
        self.__nombre=nombre
        self.__monodroga=monodr
        self.__presentacion=presen
        self.__cant=cant
        self.__precio=precio
    def getidcam(self):
        return self.__idcama
    def getNombreComercial(self):
        return self.__nombre
    def getMonodroga(self):
        return self.__monodroga
    def getPresentacion(self):
        return self.__presentacion
    def getCantidadAplicada(self):
        return self.__cant
    def getPrecioTotal(self):
        return self.__precio