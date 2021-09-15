"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Elegir el tipo de ordenamiento que desea utilizar")
    print("3- Organizar un número dado de obras de arte de acuerdo a su fecha de adquisición")
    print("0- Salir")

def initCatalog(DataStructure):
    """
    Inicializa el catalogo de obras y artistas
    """
    return controller.initCatalog(DataStructure)

def loadData(catalog):
    """
    Carga la información en la estructura de datos
    """
    controller.loadData(catalog)

def printLastArtists(artists):
    size = lt.size(artists)
    if size:
        print(' Estos son los últimos 3 artistas en el archivo cargado: ')
        for artist in lt.iterator(artists):
            print('Nombre: ' + artist['DisplayName'] + '  Bio: ' + artist['ArtistBio'] +
              ' Nacionalidad: ' + artist['Nationality'] + ' Género: ' + artist['Gender'])
    else:
        print('No se encontraron artistas')

def printLastArtworks(artworks):
    size = lt.size(artworks)
    if size:
        print(' Estas son las últimas 3 obras de arte en el archivo cargado: ')
        for artwork in lt.iterator(artworks):
            print('ID: ' + artwork['ObjectID'] + ' Titulo: ' + artwork['Title'] + '  Fecha: ' +
                  artwork['Date'] + ' Artist(as): ' + artwork['CreditLine'] + 
                  ' Clasificación: ' + artwork['Classification'])
    else:
        print('No se encontraron obras')

def print_sortArtworks_adquisition(result, sample=10):
    # TODO completar modificaciones para el laboratorio 4
    size = lt.size(result)
    if size > sample: 
        print("Las primeras ", sample, " obras de arte ordenados son:") 
        i=1 
        while i <= sample:
            artwork = lt.getElement(result,i)
            print('Titulo: ' + artwork['Title'] + ' Fecha de Adquisición: ' + artwork['DateAcquired']) 
            i+=1
    
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print('Estructuras de datos disponibles:')
        print('1)Lista encadenada')
        print('2)Lista ordenada ')
        DataStructure_choice = input('Eliga el tipo de estrucura de datos: ')
        if DataStructure_choice == 1:
            DataStructure = 'SINGLE_LINKED'
        else:
            DataStructure = 'ARRAY_LIST'

        print("Cargando información de los archivos ....")
        catalog = initCatalog(DataStructure)
        loadData(catalog)
        print('')
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print('')
        artists = controller.getLastArtists(catalog, 3)
        printLastArtists(artists)
        print('')
        artworks = controller.getLastArtworks(catalog, 3)
        printLastArtworks(artworks)
        print('')
        print()
    elif int(inputs[0]) == 2:
        print('Algoritmos de ordenamiento disponibles: ')
        print('1) Insertion Sort')
        print('2) Shell Sort')
        print('3) Merge Sort')
        print('4) Quick Sort')
        SortingMethod = input('Ingrese el algoritmo elegido: ')
    elif int(inputs[0]) == 3:
        size = lt.size(catalog['artworks'])
        print('El archivo tiene ', str(size), ' elementos.')
        saple_size = int(input('Ingrese el tamaño de la muestra: '))
        if saple_size > size:
            print('El tamaño de la muestra es mayor que el tamaño de los datos')
        else:
            result = controller.sortArtworks_adquisition(catalog, saple_size, SortingMethod)
            print("Para la muestra de", saple_size, " elementos, el tiempo (mseg) es: ",
                                         str(result[0])) 
            print_sortArtworks_adquisition(result[1])
    else:
        sys.exit(0)
sys.exit(0)
