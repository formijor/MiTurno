'''
Created on 1 mar. 2018

@author: Jorge
'''
import logica_moneda_operaciones as LMO


def agregar_digito(numero, digito, posicion, opciones):
    numero = LMO.agregar_digito(numero, digito, posicion, opciones['separador entero'],
                        opciones['separador_decimales'], opciones['cantidad_decimales'])
    return LMO.agrupar_numero(numero, opciones['separador entero'], opciones['separador_decimales'])

def multiplicar(numero1, numero2, opciones):
    numeros = LMO.convertir_numeros(numero1, numero2, opciones['cantidad_decimales'])
    resultado = numeros[0] * numeros[1]
    numero = LMO.agregar_separador_decimales(resultado, opciones['separador_decimales'],
                                           opciones['cantidad_decimales'])
    return LMO.agrupar_numero(numero, opciones['separador entero'], opciones['separador_decimales'])

def sumar(numero1, numero2, opciones):
    numeros = LMO.convertir_numeros(numero1, numero2, opciones['cantidad_decimales'])
    resultado = numeros[0] + numeros[1]
    numero = LMO.agregar_separador_decimales(resultado, opciones['separador_decimales'],
                                           opciones['cantidad_decimales'])
    return LMO.agrupar_numero(numero, opciones['separador entero'], opciones['separador_decimales'])

def restar(numero1, numero2, opciones):
    numeros = LMO.convertir_numeros(numero1, numero2, opciones['cantidad_decimales'])
    resultado = numeros[0] - numeros[1]
    numero = LMO.agregar_separador_decimales(resultado, opciones['separador_decimales'],
                                           opciones['cantidad_decimales'])
    return LMO.agrupar_numero(numero, opciones['separador entero'], opciones['separador_decimales'])

def dividir(numero1, numero2, opciones):
    numeros = LMO.convertir_numeros(numero1, numero2, opciones['cantidad_decimales'])
    resultado = numeros[0] / numeros[1]
    numero = LMO.agregar_separador_decimales(resultado, opciones['separador_decimales'],
                                           opciones['cantidad_decimales'])
    return LMO.agrupar_numero(numero, opciones['separador entero'], opciones['separador_decimales'])

def reservar_turno(persona, fecha, medico):
    'verificar que sea dia laboral'
    'verificar medico trabaja ese dia'
    'verificar que no este ocupado el turno'
    'reservar turno'
    return 'mensaje reservado'

def cancelar_turno(turno):
    'cancelar turno'
    return 'mensaje de cancelacion'

def modificar_turno(turno, persona, fecha, medico):
    reservado = reservar_turno(persona, fecha, medico)
    'si se pudo reservar el nuevo turno cancelar el anterior'
    return 'mensaje de modificacion de turno'

'-----------------------------------OPCIONES----------------------------------'

def modificar_separador_enteros(separador):
    pass
    
print ('hola')