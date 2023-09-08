
"""
        Este módulo reiventa la rueda, por hace
        lo que debe de hacer una calculadora:
        Suma, resta, multiplicacion, potencia, division.
"""
import math as mth


def sumar(x, y):
    """ Esta funcion toma dos valores y los suma"""
    return x + y


def restar(x, y):
    """ Esta funcion toma dos valores y los resta"""
    return x - y


def multiplicar(x, y):
    """ Esta funcion toma dos valores y los multiplica"""
    return x * y


def dividir(x, y):
    """ Esta funcion toma dos valores y los divide"""
    if y == 0:
        print('DivError')
    else:
        dividir = x / y

    return dividir


def potencia(x, y):
    """ Esta funcion toma dos valores y los eleva"""
    return mth.pow(x, y)
