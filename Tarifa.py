'''
Created on Jan 25, 2017

@author: daniel

Implementacion del objecto 'Tarifa' como una clase cuyos atributos son:
> tasa_semanal - contiene la tasa en bolivares por hora para dias de semana
> tasa_finsemana - contiene la tasa en bolivares por hora para dias de fin de semana
'''

class Tarifa(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tasa_semanal = 10.75
        self.tasa_finsemana = 15.75
        