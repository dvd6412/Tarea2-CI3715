'''
Created on Jan 26, 2017

@author: daniel
'''
import unittest
import datetime
from calcularPrecio import *

class TestServicio(unittest.TestCase):

    ''' Pruebas para la verificacion del manejo de las fechas
    y el calculo apropiado del monto por hora, para efectos
    practicos, el monto de la tarifa es fijo.
    '''
    def testOnlyWeekdaySameHour(self):
        #Prueba para solo dias de la semana, en horas iguales
        fecha1 = datetime.datetime(2017,1,23,13,0,0)
        fecha2 = datetime.datetime(2017,1,26,13,0,0)
        tiempoDeServicio = [fecha1,fecha2]
        tarifa = Tarifa(5.0,6.0)
        monto = calcularPrecio(tarifa,tiempoDeServicio)
        self.assertEqual(monto,360,"Fallo en la prueba testOnlyWeekdaySameHour")
        
    def testOnlyWeekendSameHour(self):
        # Prueba para solo dias de fin de semana, en horas iguales
        fecha1 = datetime.datetime(2017,2,11,22,0,0)
        fecha2 = datetime.datetime(2017,2,12,22,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,144,"Fallo en la prueba testOnlyWeekendSameHour")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    