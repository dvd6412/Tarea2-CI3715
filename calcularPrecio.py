'''
Created on Jan 25, 2017

@author: Daniel Varela
@author: Carlos Infante

'''

import datetime

class Tarifa(object):
    '''
    Implementacion del objecto 'Tarifa' como una clase cuyos atributos son:
    > tasa_semanal - contiene la tasa en bolivares por hora para dias de semana
    > tasa_finsemana - contiene la tasa en bolivares por hora para dias de fin de semana
    '''

    def __init__(self,semana=0,finde=0):
        '''
        Constructor
        Dado un monto para los dias de semana y los fines de semana, creamos objeto tarifa.
        '''
        self.tasa_semanal = semana
        self.tasa_finsemana = finde
    def semanal(self):
        #Obtener precio en dias de semana comunes..
        return self.tasa_semanal
    def finsemana(self):
        #Obtener precio del fin de semana.
        return self.tasa_finsemana
   

def calcularPrecio(tarifa, tiempoDeServicio):
    #Funcion que, dado un objeto tarifa y un arreglo con dos objetos de tipo datetime,
    #da el monto del costo total de un servicio.
    #datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)
    #timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    difTiempo = tiempoDeServicio[1] - tiempoDeServicio[0]
    assert(difTiempo.days > 0 or difTiempo.seconds >= 900) # Tiempo minimo
    assert(difTiempo.days <= 7) # Tiempo maximo
    assert(tiempoDeServicio[1] > tiempoDeServicio[0]) # Formato correcto el intervalo
    tiempo = tiempoDeServicio[0]
    monto = 0
    
    while(tiempo < tiempoDeServicio[1]):
        if(tiempo.weekday() == 5 or tiempo.weekday() == 6):
            monto += tarifa.finsemana()
        else:
            monto += tarifa.semanal()
        tiempo = tiempo + datetime.timedelta(hours = 1)    
    return monto 