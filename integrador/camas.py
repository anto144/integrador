class cama:
    __idcama=0
    __habitacion=None
    __estado=None
    __nomape=None
    __diagnostico=''
    __fechai=''
    __fechaa=''
    def __init__(self,idcama,hab,estado,nomape,diag,fechai,fechaa=None):
        self.__idcama=idcama
        self.__habitacion=hab
        self.__estado=estado
        self.__nomape=nomape
        self.__diagnostico=diag
        self.__fechai=fechai
        self.__fechaa=fechaa
    def getid(self):
        return self.__idcama
    def getestado(self):
        return self.__estado
    def gethabitacion(self):
        return self.__habitacion
    def getnom(self):
        return self.__nomape
    def getdiag(self):
        return self.__diagnostico
    def getfechai(self):
        return self.__fechai
    def getfechaa(self):
        return self.__fechaa
    def daralta(self,fecha):
        self.__fechaa=fecha
        self.__estado=False
    def __str__(self):
        cadena = "Paciente: {0:<32} Cama: {1:<5} Habitación: {2:<4}\n".format(self.getnom(), self.getid(), self.gethabitacion())
        cadena += "Diagnóstico: {0:<20} Fecha internación: {1:<10}\n".format(self.getdiag(), self.getfechai())
        cadena += "Fecha de alta: {0:<10}\n".format(self.getfechaa())
        return cadena