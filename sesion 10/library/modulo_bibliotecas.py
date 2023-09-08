"""
        Módulo de funciones para automatizar inventario de biblioteca:
        
        Funciones del módulo:
        
         - add_book() :
            Agregar libro ->
            Función que agregar libros al inventario.
            
         - show_book():
            Mostrar libro -> Función que muestra los libros del inventario.
         
         - search_book():
            Buscar libro -> Función que busca los libros del inventario.
            
        - del_book():
            Borrar libro -> Función que borra los libros del inventario.
"""

# Lista que guarda la informacion de los libros
libros = []


def add_book(titulo, autor, fecha):
    """_summary_

    Args:
        titulo (str): Parametro tipo cadena que guarda el nombre del libro.
        autor (str): Parametro tipo cadena que guarda el nombre del autor
        fecha (str): Parametro tipo cadena que guarda la fecha de publicacion del libro.
    """

    libros.append({'Titulo': titulo,
                   'Autor': autor,
                   'Fecha': fecha})


def show_book():
    """_summary_
         Funcion que imprime los libros guardados.
    """
    for libro in libros:
        # print('Título: ', libro['Titulo'], ' Autor: ',
        # libro['Autor'], 'Fecha de Publicación: ', libro['Fecha']
        print(
            f"Título: {libro['Titulo']} Autor: {libro['Autor']} Fecha de Publicación:{ libro['Fecha']}")


def search_book(titulo_libro):
    """_summary_
    Esta función busxca libros en el inventario.

     Args:
       tituloLibro (str): Parametro tipo cadena que guarda el nombre del libro.
     """
    encontrado = False
    for libro in libros:
        if titulo_libro.lower() in libro['Titulo'].lower():
            print('Libro encontrado con éxito!!! \n')
            print(
                f"Título: {libro['Titulo']} Autor: {libro['Autor']} Fecha de Publicación:{ libro['Fecha']}")
            encontrado = True
            break
    if not encontrado:

        print(f'\n El libro "{titulo_libro}" no existe,  favor  verificar')


def del_book(titulo_libro):
    """_summary_
       Esta función elimina libros del invetario.
      Args:
        tituloLibro (str): Parametro tipo cadena que guarda el nombre del libro.
      """
    encontrado = False
    for libro in libros:
        if titulo_libro.lower() in libro['Titulo'].lower():
            print(f'\n Elminando libro de titulo {titulo_libro}')
            print(
                f"Título: {libro['Titulo']} Autor: {libro['Autor']} Fecha de Publicación:{ libro['Fecha']}")
            libros.remove(libro)
            encontrado = True
            break

    if not encontrado:
        print(f'\n El libro "{titulo_libro}" no existe,  favor  verificar')
