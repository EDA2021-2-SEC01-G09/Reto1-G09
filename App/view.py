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
    print("2- ")
    print("0- Salir")

def initCatalog():
    """
    Inicializa el catalogo de obras y artistas
    """
    return controller.initCatalog()

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
            print('ID: ' + artwork['ConstituentID'] + ' Titulo: ' + artwork['Title'] + '  Fecha: ' +
                  artwork['Date'] + ' Artist(as): ' + artwork['CreditLine'] + 
                  'Clasificación: ' + artwork['Classification'])
    else:
        print('No se encontraron obras')
        
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
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
    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
