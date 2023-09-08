"""
        Módulo de funciones para uso de calculadora al personal de biblioteca:
        
        Funciones del módulo:
        
         - add_function() :
         Función para sumar números.
            
         - mult_function():
        Función para multiplicar números.
         
         - sus_function():
        Función para restar números.
            
        - div_function():
        Funcion para dividir dos numeros
"""


def add_function(x, y):
    """_summary_
     Función para sumar números.

     x (float) - variable tipo float que guarda el primer valor a sumar
     y (float) - variable tipo float que guarda el segundo valor a sumar
    """
    return x + y


def mult_function(x, y):
    """_summary_
     Función para mutliplicar números.

     x (float) - variable tipo float que guarda el primer valor a multiplicar
     y (float) - variable tipo float que guarda el segundo valor a multplicar
    """
    return x * y


def sus_function(x, y):
    """_summary_
 Función para restar números.

 x (float) - variable tipo float que guarda el primer valor a restar
 y (float) - variable tipo float que guarda el segundo valor a restar
"""
    return x - y


def div_function(x, y):
    """_summary_
    Función para restar números.

    x (float) - variable tipo float que guarda el primer valor a restar
    y (float) - variable tipo float que guarda el segundo valor a restar
    """
    return (x / y if y != 0 else print('DivByZero'))
