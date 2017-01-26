'''
Created on Jan 26, 2017

@author: daniel
'''
import unittest
import datetime
import sys
from calcularPrecio import *

class TestServicio(unittest.TestCase):

    ''' Pruebas para la verificacion del manejo de las fechas
    y el calculo apropiado del monto por hora, para fines
    practicos, el monto de la tarifa es fijo en estas pruebas.
    '''
    def testOnlyWeekdaySameHour(self):
        #Prueba para solo dias de semana, en horas iguales
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
        
    def testOnlyWeekdayDiffHour(self):
        # Prueba para solo dias de semana, en horas distintas
        fecha1 = datetime.datetime(2017,3,6,3,0,0)
        fecha2 = datetime.datetime(2017,3,10,22,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,575,"Fallo en la prueba testOnlyWeekendDiffHour")
        
    def testOnlyWeekendDiffHour(self):
        # Prueba para solo dias de fin de semana, en horas distintas
        fecha1 = datetime.datetime(2017,1,7,14,0,0)
        fecha2 = datetime.datetime(2017,1,8,5,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,90,"Fallo en la prueba testOnlyWeekendDiffHour")
        
    def testWeekdaytoWeekend(self):
        # Prueba donde se parte de un dia de semana, y se termina 
        # en un dia de fin de semana
        fecha1 = datetime.datetime(2017,4,6,23,0,0)
        fecha2 = datetime.datetime(2017,4,9,12,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,341,"Fallo en la prueba testWeekdaytoWeekend")
        
    def testWeekendtoWeekday(self):
        # Prueba donde se parte de un dia se fin de semana, y
        # se termina en un dia de semana
        fecha1 = datetime.datetime(2017,12,3,12,0,0)
        fecha2 = datetime.datetime(2017,12,5,12,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,252,"Fallo en la prueba testWeekendtoWeekday")
        
    def test7DaysRange(self):
        # Prueba para el caso borde, donde el servicio es exactamente de 7 dias
        fecha1 = datetime.datetime(2017,5,15,0,0,0)
        fecha2 = datetime.datetime(2017,5,21,23,59,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,888,"Fallo en la prueba test7DaysRange")
        
    def test15MinutesRange(self):
        # Prueba para el caso borde, donde el servicio es exactamente 15 minutos
        fecha1 = datetime.datetime(2017,10,30,13,0,0)
        fecha2 = datetime.datetime(2017,10,30,13,15,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio= [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,5,"Fallo en la prueba test15MinutesRange")
        
    def testMonthChange(self):
        # Prueba sobre un rango de fechas, donde ocurre un cambio de mes
        fecha1 = datetime.datetime(2017,2,28,16,0,0)
        fecha2 = datetime.datetime(2017,3,2,16,0,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,240,"Fallo en la prueba testMonthChange")
        
    def testCompleteHour(self):
        # Prueba sobre el requerimiento de cobro de hora completa, es decir,
        # para 1 hora + 1 minuto, se cobran como si fuesen 2 horas.
        fecha1 = datetime.datetime(2017,1,10,0,0,0)
        fecha2 = datetime.datetime(2017,1,10,12,1,0)
        tarifa = Tarifa(5.0,6.0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,65,"Fallo en la prueba testCompleteHour")
        
    ''' Pruebas para la verificacion de los calculos con tasas
    de tarifa variadas 
    '''
        
    def testCalcDecDec(self):
        # Prueba sobre el calculo del servicio, usando numeros
        # decimales para ambas tasas
        fecha1 = datetime.datetime(2017,1,13,12,0,0)
        fecha2 = datetime.datetime(2017,1,16,12,0,0)
        tarifa = Tarifa(12.45,4.88)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertAlmostEqual(monto,533.04,7,"Fallo en la prueba testCalcDecDec")
        
    def testCalcZero(self):
        # Prueba para el caso borde, ambas tarifas son cero (0)
        fecha1 = datetime.datetime(2017,1,13,12,0,0)
        fecha2 = datetime.datetime(2017,1,16,12,0,0)
        tarifa = Tarifa(0,0)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,0,"Fallo en la prueba testCalcZeroZero")
        
    def testCalcMaxFloat(self):
        # Prueba para el caso borde, ambas tarifas son el maximo
        # numero punto flotante representable por Python
        fecha1 = datetime.datetime(2017,1,13,12,0,0)
        fecha2 = datetime.datetime(2017,1,16,12,0,0)
        tarifa = Tarifa(sys.float_info.max,sys.float_info.max)
        tiempoDeServicio = [fecha1,fecha2]
        monto = calcularPrecio(tarifa, tiempoDeServicio)
        self.assertEqual(monto,(24*sys.float_info.max)+(48*sys.float_info.max),"Fallo en la prueba testCalcMaxFloat")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    