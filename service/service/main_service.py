import time
import json
from loguru import logger
from service import responses
from service.constants import mensagens
import pandas as pd
import numpy as np

class CalculadoraService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MODEL)
        self.load_model()

    def load_model(self):

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_calc(self, number):

        response = {}
        
        logger.debug(mensagens.INICIO_CALCULADORA)
        start_time = time.time()

        response_predicts = self.buscar_predicao(number['number1'], number['number2'], number['operacao'])
        

        logger.debug(mensagens.FIM_CALCULADORA)
        logger.debug('Fim de todas as predições em {time.time()-start_time}')
        response = {
                    'Resultado da operacao': response_predicts}

        return response

    def buscar_predicao(self, number1, number2, operacao):
        
        logger.debug('Iniciando a calculadora..')

        if operacao[0] == '+':
            response = number1[0] + number2[0]
            
        elif operacao[0] == '-':
            response = number1[0] - number2[0]
        
        elif operacao[0] == '*':
            response = number1[0] * number2[0]

        elif operacao[0] == '/':
            response = number1[0] / number2[0]

        print(response)

        return response