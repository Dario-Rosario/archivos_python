#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    fi = open("notas.txt", "r")

    cantidad_lineas = contar_lineas(fi)

    print("Lineas leidas del texto:", cantidad_lineas)

    fi.seek(0)
    print(fi.read()) #imprimi el texto como practica.

    fi.close() 
    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''

def contar_lineas(fi):
    
    cantidad_lineas = 0

    for line in fi:
        cantidad_lineas +=1

    return cantidad_lineas


def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0
    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)

    fi = open("notas.txt", "r")
    fo = open("notas2.txt", "a")

    for line in fi.readlines():
        fo.write(line)

    fi.seek(0)
    for line in fi.readlines():
        cantidad_lineas +=1
    

    print(cantidad_lineas)

    fi.close()
    fo.close()


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''

    with open("propiedades.csv", "r") as csvfile:
        data = list(csv.DictReader(csvfile))

    ambientes_2 = 0
    ambientes_3 = 0
   
    cantidad_filas = len(data)
    for i in range(cantidad_filas):
        if data[i].get("ambientes") == "2":
            ambientes_2 += 1
        else:
            if data[i].get("ambientes") == "3":
                ambientes_3 += 1   

    print("Cantidad de departamentos de dos ambientes es:", ambientes_2)         
    print("Cantidad de departamentos de tres ambientes es:", ambientes_3)  


def ej4():
    # Ejercicios con diccionarios

    inventario = {'manzanas': 6}
    
    while True:
    
        nuevo_ingreso = str(input("Ingrese una fruta o verdura (Si termino ingrese FIN): \n"))
        
        if nuevo_ingreso in inventario:
            inventario[nuevo_ingreso] += 1
        else:    
            inventario[nuevo_ingreso] = 1    
                
        if nuevo_ingreso == "FIN":
                break
    
    stock = str(input("Ingrese el stock que desea conocer: \n"))
    print("El stock de", stock, "es:", inventario.get(stock))

    '''

    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''

    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"


def ej5():
    # Ejercicios con archivos CSV
    inventario = {}

    while True:
    
        nuevo_ingreso = str(input("Ingrese una fruta o verdura (Si termino ingrese FIN): \n"))
        
        if nuevo_ingreso == "FIN":
            break

        cantidad = float(input("Ingrese la cantidad: \n"))
        
        if nuevo_ingreso in inventario:
            inventario[nuevo_ingreso] += cantidad
        else:    
            inventario[nuevo_ingreso] = cantidad   
                
    

    csv_file =  open("inventario.csv", "w", newline="")
    header = ["Fruta Verdura", "Cantidad"]
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    for k, v in inventario.items():
        row = {'Fruta Verdura': k, 'Cantidad': v}
        writer.writerow(row)
    
    csv_file.close()

    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


if __name__ == '__main__':
    #print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
