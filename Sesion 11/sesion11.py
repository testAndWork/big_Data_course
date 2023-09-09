def division_segura(numerador, denominador):

    try:
        resultado = numerador / denominador
        return resultado

    except ZeroDivisionError:
        print('Error: No se puede divir entre cero')

    except:
        print('Error: Ha ocurrido algun problema')


# x = int(input('Digite numerador'))
# y = int(input('DIgite denominador'))


# division_segura(x, y)


def convert_2_int(cadena):

    try:
        entero = int(cadena)
        return entero
    except ValueError:
        print("Error: la cadena no es válida")


cad = '233423423'  # 'fgh'

# intCad = convert_2_int(cad)

# lorem.txt
# print(type(intCad))


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            print("Contenido del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no se encuentra.")


# Prueba de la función
nombre_archivo = input("Ingrese el nombre del archivo para leer: ")
leer_archivo(nombre_archivo)
