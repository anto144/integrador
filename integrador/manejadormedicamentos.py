from medicamentos import medicamentos
import csv
class manejadormed:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargarlista(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            medicamento=medicamentos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],float(fila[6]))
            self.__lista.append(medicamento)
        return
    def getmedxcam(self,id):
        cadena = "{0:<15}{1:^15}{2:^10}{3:^10}{4:^7}\n".format("Medicamento", "Monodroga", "Presentacion", "Cantidad", "Precio")
        totalapagar=0
        for medicamento in self.__lista:
            if medicamento.getidcam()==id:
                cadena +="{0:<15}{1:^15}{2:^10}{3:^10}{4:^7}\n".format(medicamento.getNombreComercial(), medicamento.getMonodroga(), medicamento.getPresentacion(), medicamento.getCantidadAplicada(), medicamento.getPrecioTotal())
                totalapagar+=medicamento.getPrecioTotal()
        cadena += "Total adeudado:{0:>43.2f}".format(totalapagar)
        return cadena