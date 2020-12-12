"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from App import controller
assert config
import timeit

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

small = 'taxi-trips-wrvz-psew-subset-small.csv'
medium = 'taxi-trips-wrvz-psew-subset-medium.csv'
large = 'taxi-trips-wrvz-psew-subset-large.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de taxis")
    print("3- Requerimiento 1")
    print("4- Requerimiento 2")
    print("5- Requerimiento 3")
    print("0- Salir")
    print("*******************************************")

def optionTwo():
    print("\nCargando información de taxis....")
    if Afile == "small":
       controller.loadData(cont, small)
    if Afile == "medium":
       controller.loadData(cont, medium)   
    if Afile == "large":
       controller.loadData(cont, large)     


def optionThree():
    res = controller.getTopCompanies(cont, int(numM), int(numN))
    print("El numero de taxis:", res[0])
    print("El numero de compañías:", res[1])
    print("El top de companías con más taxis afiliados:", res[2])
    print("El top de companías que más servicios prestaron:", res[3])

def optionFour():
    res = controller.getTaxisPointsByRange(cont, initialDate, finalDate, int(numN))
    print("Taxis con más puntos: ", res)

def optionFive():
    print("Escriba..")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        Afile = input("Escriba el archivo a utilizar (small, medium o large): ")
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 3:
        numM = input("Número de compañías a retornar con más taxis afiliados: ")
        numN = input("Número de compañías a retornar con más servicios prestados: ")
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 4:
        initialDate = input("Escriba la fecha inicial (Ejm: 2019-10-31): ")
        finalDate = input("Escriba la fecha final ó NA si solo desea la fecha inicial: ")
        if finalDate == "NA":
           finalDate = initialDate 
        numN = input("Número de taxis a retornar con más puntos: ")
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 5:
        executiontime = timeit.timeit(optionFive, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    else:
        sys.exit(0)
sys.exit(0)

