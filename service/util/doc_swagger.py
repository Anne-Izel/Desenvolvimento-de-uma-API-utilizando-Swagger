from flask_restplus import fields
from service.restplus import api

# altera os campos do json
INPUT_MAIN_SERVICE = api.model( 
  'input_main_service', {
    # 'textoMensagem': fields.List(fields.String(), required=True, description= "Frase em inglês a ser classificada")})
    'operacao': fields.List(fields.String(), required=True, description= 'Operacao'), 
    'number1': fields.List(fields.Float(), required=True, description= 'Valor 1'),
    'number2': fields.List(fields.Float(), required=True, description= 'Valor 2')})
     
# integer