'''
Created on 27 feb. 2018

@author: Jorge
'''

def separar_numero_entero_decimal(numero, separador):
    try:
        if type(numero) == str and separador in numero:
            numero = numero.split(separador)
        return numero
    except:
        print ('Fallo al separar el numero(string) en parte entera y parte decimal')

def agregar_separacion_numero_entero(numero, separador):
    numero_lista = list(numero)
    numero_agrupado = []
    contador = 0
    for digito in reversed(numero_lista):
        if contador == 3:
            numero_agrupado.insert(0, separador)
            contador = 0
        numero_agrupado.insert(0, digito)
        contador += 1
    return "".join(numero_agrupado)

def agrupar_numero(numero, separador_entero, separador_decimal):
    if separador_decimal in numero:
        numero_separado = numero.split(separador_decimal)
        entero = numero_separado[0]
        decimal = numero_separado[1]
        entero = agregar_separacion_numero_entero(entero, separador_entero)
        numero_agrupado = "".join([entero, separador_decimal, decimal])
    else:
        numero_agrupado = agregar_separacion_numero_entero(numero, separador_entero)
    return numero_agrupado        

def quitar_separadores_numero_entero(numero, separador):
    return numero.replace(separador, '')

def agregar_digitos(numero, cantidad_decimales_total):
        cant_digitos_agregar = cantidad_decimales_total - len(numero)
        numero += '0' * cant_digitos_agregar
        return numero

def agregar_separador_decimales(numero, separador, cantidad_decimales):
    numero_lista = list(numero)
    numero_lista.insert(-cantidad_decimales, separador)
    return "".join(numero_lista)
    
def completar_decimales(numero, cantidad_decimales_total):   
    largo_numero = len(numero)
    if largo_numero == cantidad_decimales_total:
        return numero
    elif largo_numero < cantidad_decimales_total:
        return agregar_digitos(numero, cantidad_decimales_total)
    else:
        return numero

def agregar_digito_decimal(numero, digito, posicion, posicion_separador_decimal, cantidad_decimales_total):
    if len(numero[posicion_separador_decimal:]) -1 < cantidad_decimales_total:
        numero.insert(posicion, digito)
    return numero  

def agregar_digito_entero(numero, digito, posicion):
    numero.insert(posicion, digito)
    return numero

def agregar_digito(numero, digito, posicion, separador_entero, separador_decimales, cantidad_decimales_total):    
    numero.replace(separador_entero, '')
    numero_separado = list(numero)
    if separador_decimales in numero:
        posicion_separador_decimal = numero_separado.index(separador_decimales)
        if posicion > posicion_separador_decimal:
            numero_separado = agregar_digito_decimal(numero_separado, digito, posicion, posicion_separador_decimal, cantidad_decimales_total)
        else:
            numero_separado = agregar_digito_entero(numero_separado, digito, posicion)
    else:
        numero_separado = agregar_digito_entero(numero_separado, digito, posicion)
    return "".join(numero_separado)
                
def convertir_numero_a_entero(numero, separador_entero, separador_decimales, cantidad_decimales_total):
    if type(numero) == str:
        numero = numero.replace(separador_entero,'')
        numero = numero.replace(separador_decimales,'')
    elif type(numero) == float:
        numero = numero * int('1' + '0' * cantidad_decimales_total)      
    numero = int(numero)
    return numero

def convertir_numeros(multiplicando, multiplicador, cantidad_decimales_total):
    if type(multiplicando) != int:
        multiplicando = convertir_numero_a_entero(multiplicando, cantidad_decimales_total)
    if type(multiplicador) != int:
        multiplicador = convertir_numero_a_entero(multiplicador, cantidad_decimales_total)
    return multiplicando, multiplicador




debug = False
if debug == True:    
    numero = agregar_digito(',3', '4', 0, '.', ',', 2) 
    print (agrupar_numero(numero, '.', ',')   ) 
    print (convertir_numero_a_entero(123.45, '.', ',', 2))


    