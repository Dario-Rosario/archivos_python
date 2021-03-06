#!/usr/bin/env python


'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    fi = open("texto.txt", "r")
    fi.seek(0)
    
    contenido = fi.read()

    cantidad_letras = len(contenido)
    print(cantidad_letras)
    

    fi.close()    

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open("nuevo.txt", "w")
    print("Ingrese el texto")

    ingreso = []

    while True:
        if ingreso == "":
            break
        else:
            ingreso = str(input())
            fo.write(ingreso)
            fo.write("\n")
            cantidad_letras = len(ingreso) + cantidad_letras

    

    fo.close()


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = "2"

    cantidad_alquileres = 0
    tipo_moneda = "ARS"
    precio = 0
    precio_promedio = 0
    precio_max = 0
    precio_alquiler = 0
    precio_min = 0

    with open("propiedades.csv", "r") as csvfile:
        data = list(csv.DictReader(csvfile))

    filas = len(data)

    for i in range(filas):
        if data[i].get("ambientes") == cantidad_ambientes and data[i].get("moneda") == tipo_moneda:
            cantidad_alquileres = cantidad_alquileres + 1
            row = data[i]
            precio = float(row.get("precio")) + precio
            precio_promedio = precio/cantidad_alquileres
            precio_alquiler = float(row.get("precio"))
            if precio_alquiler > precio_max:
                precio_max = precio_alquiler
            if precio_min == 0:
                precio_min = precio_alquiler    
            if precio_alquiler < precio_min:
                precio_min = precio_alquiler    
            
    print("Para",cantidad_ambientes,"ambientes estos son los resultados: \n1) La cantidad de alquileres en", tipo_moneda,"es",cantidad_alquileres)
    print("2) El precio promedio es:",precio_promedio)
    print("3) El precio maximo es:", precio_max)
    print("4) El precio minimo es:", precio_min)

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''


def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''


if __name__ == '__main__':
    #print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
