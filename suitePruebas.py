'''
Created on Jan 26, 2017

@author: daniel
'''
import unittest
import datetime
from calcularPrecio import *

class TestServicio(unittest.TestCase):


    def testOnlyWeekday(self):
        
        fecha1 = datetime.datetime(2016,1,23,13,0,0)
        fecha2 = datetime.datetime(2016,1,26,13,0,0)
        tiempoDeServicio = [fecha1,fecha2]
        tarifa = Tarifa(5.0,6.0)
        monto = calcularPrecio(tarifa,tiempoDeServicio)
        self.assertEqual(monto,480,"Fallo en la prueba testOnlyWeekday")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()