"""Biblioteca
    Desarrollar un sistema para automatizar lso procesos en una bibliotecas;
    el sistema debe de contener las funciones basicas para llevar el control de
    libros dentro de sus bodegas.
    
    El sistema debe de mostrar un menu y que el encargado de la biblioteca decida que 
    opcion realizará.
    
    Funciones a realizar: agegar libros, mostrar libros en inventario,
    buscar libros en inventario, borrar libros y salir.
    
    Además puede hacer uso de una calculadora cuando lo necesite.

"""

import library.modulo_bibliotecas as mb
import library.modulo_calc as mc

print(65*'*')
print('\nBienvenidos al sistemas de Control de inventario de biblioteca.\n')
print(65*'*')

while True:

    print('Digite la opcion que desea:')
    print('1 - Agregar libros al invetario')
    print('2 - Mostrar libros del invetario')
    print('3 - Buscar libros del invetario')
    print('4 - Borrar un libro del inventario')
    print('5 - Usar Calculadora ')
    print('0 - Salir')
    print(65*'*')

    opcion = int(input('\nDigite el número de la opción: '))

    if opcion == 0:
        print('\n Gracias por usar el sistema, Feliz día!')
        break

    elif opcion == 1:
        titulo = input('Ingrese el título del autor del libro: ')
        autor = input('Ingrese el nombre del autor del libro: ')
        fecha = input('Ingrese la fecha de publicación del libro: ')
        mb.add_book(titulo, autor, fecha)

    elif opcion == 2:
        print('EL inventario actual es: \n\n')
        mb.show_book()

    elif opcion == 3:
        busqueda = input('Digite el título del libro a Buscar: ')
        mb.search_book(busqueda)

    elif opcion == 4:
        eliminar = input('Digite el título del libro a eliminar: ')
        mb.del_book(eliminar)
        print('\nLibro eliminado con exito!!\n\n')

    elif opcion == 5:
        print('Bienvenido a la calculadora \n')
        print('LAs operaciones son: sumar , restar , dividir, multiplicar\n')
        op = input(' Digite la operación a utilizar\n')

        a = float(input('Digite el primer numero: '))
        b = float(input('Digite el segundo numero: '))

        if op.lower() == 'sumar':
            print('La suma es ', mc.add_function(a, b))
        elif op.lower() == 'restar':
            print('La resta es ', mc.sus_function(a, b))
        elif op.lower() == 'division':
            print('La division  es ', mc.div_function(a, b))
        elif op.lower() == 'multiplicacion':
            print('La multiplicacion  es ', mc.mult_function(a, b))
        else:
            print('\nOperacion no encontrada')

    else:
        print('\nOpción Inválida intente de nuevo\n')


# mb.add_book('Silabario', 'Anónimo', '1800')
# mb.add_book('Nacho', 'Anónimo', '1900')
# mb.add_book('Pablito', 'Anónimo', '1880')
# mb.add_book('Textito', 'Anónimo', '1890')

# mb.show_book()

# mb.search_book('nacHo')
# mb.search_book('pasta')


# mb.del_book('nacho')
# mb.del_book('pasta')

# suma = mc.add_function(4, 5)

# print('EL resultado de la suma es : ', suma)

# division = mc.div_function(4, 0)

# print('El resultrado de la diviosn es : ', division)
